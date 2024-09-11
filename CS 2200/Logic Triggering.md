# Level Triggering
____
- Outputs change based on inputs
- Gated D Latches only change when the clock is high
- LC-2200 memory reads are level triggered (for cost & complexity reasons)

The following is level triggered
- Memory - Read
- Register File - Read
- ALU
- Other Register reads
- Muxes 
- Decoders
# Edge Triggering
_____
- Outputs change based on inputs only when clock transitions 
- Positive edge-triggered logic when leading edge cause triggering
- Negative edge-triggered when trailing edge causes triggering

The following is edge triggered
- Memory - Write 
- Register File - Write
- Other Register writes 