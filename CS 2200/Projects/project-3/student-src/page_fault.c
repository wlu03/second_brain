#include "mmu.h"
#include "pagesim.h"
#include "swapops.h"
#include "stats.h"

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-parameter"

/**
 * --------------------------------- PROBLEM 6 --------------------------------------
 * Checkout PDF section 7 for this problem
 *
 * Page fault handler.
 *
 * When the CPU encounters an invalid address mapping in a page table, it invokes the
 * OS via this handler. Your job is to put a mapping in place so that the translation
 * can succeed.
 *
 * @param addr virtual address in the page that needs to be mapped into main memory.
 *
 * HINTS:
 *      - You will need to use the global variable current_process when
 *      altering the frame table entry.
 *      - Use swap_exists() and swap_read() to update the data in the
 *      frame as it is mapped in.
 * ----------------------------------------------------------------------------------
 */
void page_fault(vaddr_t addr)
{
   // TODO: Get a new frame, then correctly update the page table and frame table

   // Get the page table entry for the faulting virtual address
   vpn_t vpn = vaddr_vpn(addr);
   pte_t *pte = ((pte_t *) (mem + (PTBR * PAGE_SIZE))) + vpn;
   pfn_t new_frame = free_frame();
   paddr_t *swap_addr = (paddr_t *) (mem + PAGE_SIZE * new_frame);

   // Update mapping from VPN to new PFN in the current process page table
   pte->valid = 1;
   pte->pfn = new_frame;

   // Update Flags in the frame table entry
   frame_table[new_frame].ref_count = 0;
   frame_table[new_frame].process = current_process;
   frame_table[new_frame].vpn = vpn;
   frame_table[new_frame].protected = 0;


   // Check to see if there is an existing swap entry for the faulting page table entry
   if (swap_exists(pte)) {
      // If a swap entry exist, use swap_read() to read in the saved_frame into new_frame
      swap_read(pte, swap_addr);
   } else {
      memset(swap_addr, 0, PAGE_SIZE);
   }
   
   //increment page fault
   stats.page_faults++;


}
#pragma GCC diagnostic pop
