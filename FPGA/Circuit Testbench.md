There are multiple reasons as to why you might want to create a so-called _test bench_ for the generated HDL:

- You want to compare post-synthesis / post-place&route behavior to that of the behavior of the original generated HDL.
- Need representative stimuli for your dynamic power calculations.
- Verify that the HDL output of the Clash compiler has the same behavior as the Haskell / Clash specification.