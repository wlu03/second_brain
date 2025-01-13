#include "types.h"
#include "pagesim.h"
#include "mmu.h"
#include "swapops.h"
#include "stats.h"
#include "util.h"
#include <stdbool.h>

pfn_t select_victim_frame(void);

pfn_t last_evicted = 0;

/**
 * --------------------------------- PROBLEM 7 --------------------------------------
 * Checkout PDF section 7 for this problem
 *
 * Make a free frame for the system to use. You call the select_victim_frame() method
 * to identify an "available" frame in the system (already given). You will need to
 * check to see if this frame is already mapped in, and if it is, you need to evict it.
 *
 * @return victim_pfn: a phycial frame number to a free frame be used by other functions.
 *
 * HINTS:
 *      - When evicting pages, remember what you checked for to trigger page faults
 *      in mem_access
 *      - If the page table entry has been written to before, you will need to use
 *      swap_write() to save the contents to the swap queue.
 * ----------------------------------------------------------------------------------
 */
pfn_t free_frame(void)
{
    pfn_t victim_pfn;
    victim_pfn = select_victim_frame();

    // TODO: evict any mapped pages.
    if (frame_table[victim_pfn].mapped) 
    {
        // get VPN and Process
        pcb_t *proc = frame_table[victim_pfn].process;
        vpn_t vpn = frame_table[victim_pfn].vpn;

        // get page table of the process
        pte_t *pte = (pte_t *) (mem + frame_table[victim_pfn].process->saved_ptbr * PAGE_SIZE);
        pte = pte + frame_table[victim_pfn].vpn;
        // if the page is dirty, write it to swap
        if (pte->dirty != 0) {
            swap_write(pte, mem + victim_pfn * PAGE_SIZE);
            stats.writebacks++;
        }

        // Invalidate the page table entry
        pte->valid = 0; 
        pte->dirty = 0;

        // Mark the frame as unmapped in the frame table
        frame_table[victim_pfn].mapped = 0;
    }

    return victim_pfn;
}

/**
 * --------------------------------- PROBLEM 9 --------------------------------------
 * Checkout PDF section 7, 9, and 11 for this problem
 *
 * Finds a free physical frame. If none are available, uses either a
 * randomized, FCFS, or clocksweep algorithm to find a used frame for
 * eviction.
 *
 * @return The physical frame number of a victim frame.
 *
 * HINTS:
 *      - Use the global variables MEM_SIZE and PAGE_SIZE to calculate
 *      the number of entries in the frame table.
 *      - Use the global last_evicted to keep track of the pointer into the frame table
 * ----------------------------------------------------------------------------------
 */
pfn_t select_victim_frame()
{
    /* See if there are any free frames first */
    size_t num_entries = MEM_SIZE / PAGE_SIZE;
    for (size_t i = 0; i < num_entries; i++)
    {
        if (!frame_table[i].protected && !frame_table[i].mapped)
        {
            return i;
        }
    }

    // RANDOM implemented for you.
    if (replacement == RANDOM)
    {
        /* Play Russian Roulette to decide which frame to evict */
        pfn_t unprotected_found = NUM_FRAMES;
        for (pfn_t i = 0; i < num_entries; i++)
        {
            if (!frame_table[i].protected)
            {
                unprotected_found = i;
                if (prng_rand() % 2)
                {
                    return i;
                }
            }
        }
        /* If no victim found yet take the last unprotected frame
           seen */
        if (unprotected_found < NUM_FRAMES)
        {
            return unprotected_found;
        }
    }
    else if (replacement == APPROX_LRU) {
        pfn_t victim_pfn = 0;
        uint8_t smallest_ref_count = 0xFF;

        for (pfn_t i = 0; i < num_entries; i++) {
            // skip frames that are protected or unmapped
            if (frame_table[i].protected || !frame_table[i].mapped) {
                continue;
            }
            if (frame_table[i].ref_count < smallest_ref_count) {
                smallest_ref_count = frame_table[i].ref_count;
                victim_pfn = i;
            }
        }
        frame_table[victim_pfn].ref_count = 0;
        return victim_pfn;
    }

    else if (replacement == CLOCKSWEEP)
    {
        while (true) {
            for (pfn_t i = 0; i < num_entries; i++) {
                last_evicted = (last_evicted + 1) % num_entries;
                if (frame_table[last_evicted].protected) {
                    continue;
                }
                pte_t *pte = (pte_t *)(mem + frame_table[last_evicted].process->saved_ptbr * PAGE_SIZE) + frame_table[last_evicted].vpn;
                if (pte->referenced) {
                    pte->referenced = 0;
                } else {
                    return last_evicted;
                }
            }
        }
    }


    /* If every frame is protected, give up. This should never happen
       on the traces we provide you. */
    panic("System ran out of memory\n");
    exit(1);
}

/**
 * --------------------------------- PROBLEM 10.2 --------------------------------------
 * Checkout PDF for this problem
 *
 * Updates the associated variables for the Approximate LRU,
 * called every time the simulator daemon wakes up.
 *
 * ----------------------------------------------------------------------------------
 */

void daemon_update(void)
{
    /** FIX ME */
    // Dumps the MSB of the corresponding per frame reference counters. The cunters are right-shifted
    // into their MSB position.
    // After reading the reference bits, the mem manager clears them. 
    // It repeats this step every time quantum.
    // The Ref Counter with largest value is most recently referenced page. Vice Versa for the smallest.
    
    // Get total entry size
    size_t num_entries = MEM_SIZE / PAGE_SIZE;

    // Iterate through all entries in the frame table
    for (pfn_t i = 0; i < num_entries; i++) {
        if ((frame_table[i].protected == 0) &&(frame_table[i].mapped == 1)) {
            pte_t *pte = (pte_t *)(mem + (frame_table[i].process->saved_ptbr * PAGE_SIZE)) + frame_table[i].vpn;
            frame_table[i].ref_count >>= 1;
            frame_table[i].ref_count |= (pte->referenced << (sizeof(frame_table[i].ref_count) * 8 - 1));
            pte->referenced = 0;
        }
    }
}

