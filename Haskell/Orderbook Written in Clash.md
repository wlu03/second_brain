# Set up Skeleton Clash Project

``` bash
mkdir clash_orderbook
cd clash_orderbook
```

- Create `flake.nix` file at the root of the project. this sets up the inputs and defines development shell that includes the clash compiler
	- This file creates an environment where the required tools (i.e. Clash Compiler) are installed. By including `devShell` attribute in flake, you can simply run `nix develop`
	- It drops you in a shell where Clash is avaliable
- I will place my HashMap implementation in a Haskell source file `src/HashMap.hs` where I write my hardware design logic
- Once inside the development shell (run `nix develop`) I can build my design in clash using `clash --vhdl src/HashMap.hs -o build`
	- This command tells clash to compile the design into VDHL and outputs into the `build` directory.

## What is the OrderMap?
The **order map** is a lookup table (HashMap) that associates each order's unique ID with its details: price and quantity. In the design mentioned, certain ITCH instructions (`DELETE` or `CANCEL`) only provide the order ID without the associated price or quantity. This is where the order map is important. 

When an instruction like `DELETE` arrives, it only specifies which order to remove. The order map is used to retrieve the missing details to update the book - decrement the depth of the price level. 

The role in the pipeline stage stores order information so the later stages can adjust the order-book state. In a hardware design (FPGA), the order-map must support fast, efficient lookups (`O(1)`/ constant time)  
## What is NIX?
**Nix**: 
- Builds and manages packages using functional programming principles
- Guarantees that builds are consistent by isolating build inputs from system state
- Allows multiple version of packages to coexists without conflicts
- Supports safe system updates with the ability to revert changes
- Enables system configurations to be described and managed as code
**Flake**: 
- Uses `flake.nix` file to encapsulate configurations, packages, and development environments in a consistent format
- Declares inputs and outputs making it easier to manage complex projects

## Study Hardware HashMap Designs
Link: https://github.com/johan92/fpga-hash-table/blob/master/README.md

**Requirements**: 
- **Fixed-Size**: Avoid dynamic memory - hardware designs needs a static memory. Use fixed-sized vectors or arrays to represent hash map storage.
- **Efficient for Lookups and Updates**: lookup, insertion, and deletion
### Collisions
- Linear or Quadratic probing or chaining. Open addressing might be easier for hardware
- Hash Function or order IDs in my case

When two keys produce the same index, a **collision** occurs. 

**Open Addressing**
All entries are stored directly within the array. When a collision occurs, the hash map search for another available slot. 
- **Linear Probing**: If the calculated Index is occupied, the algorithm checks the next slot (index + 1, wrapping if needed) until it finds an empty slot. It could lead to clustering where long runs of occupied slots build up
- **Quadratic Probing**: Instead of checking the next slot, quadratic probing uses quadratic function of the probe number to find the next slot ($1^2,2^2,3^2,...$). This reduces clustering 
- **Deletion**: A marker is used to indicate that a slot was occupied and then deleted, ensuring that lookups can keep probing.

**Chaining** 
Each slot of the table holds a pointer to a linked list of entries that hash to the same index.
- **Insertion**: Add the key-value pair to the list of bucket 
- **Lookup/Deletion**: Traverse the list to find the matching key

## FPGA HashMap
```
hash_table_top
	├─ calc_hash            // Hash computation module
	├─ head_table           // Manages bucket head pointers
	├─ data_table           // Stores key-value entries
	├─ ht_delay             // Pipeline delay matching
	├─ ht_res_mux           // Result multiplexer
	└─ empty_ptr_storage    // Manages free memory pointers
```

In my pipelined order book, the hash computation module is used right after parsing and dequeuing the ITCH message. The computed bucket could then be used to index into the order map or cache when I update the order book state. In the ITCH protocol the `orderID` is is the order reference number. In the message types "A" or "F" (add) and "D" (delete), this field appears at offset 11 and is **8 bytes long (64 bits)**. For example, an Add order message number can be represented as `0x000000000012345678`

## Testing and Verification
- QuickCheck: write property based test to verify your functions work correctly in simulation 