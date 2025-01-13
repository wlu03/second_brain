## Metrics
____
**Arithmetic Mean**: Average of all individual execution times (seconds)$$(E_1+E_2+E_3+...+E_p)/p$$**Weighted Arithmetic Mean**: Weighted average of execution times (seconds)$$(f_1\cdot E_1+f_2\cdot E_2+...+f_p\cdot E_p)$$ **Geometric Mean**: $n^{th}$ root of the product of all n execution times (seconds) $$(E_1\cdot E_2 \cdot E_3...\cdot E_p)^{1/p}$$**Speedup**: $\frac{\text{Execution Time on Processor B}}{\text{Execution Time on Processor A}}$
**Speedup Improved**: $\frac{ \text{Execution Time Before Improvement}}{\text{Execution Time After Improvement}}$
**Improvement in Execution Time**: $\frac{\text{Old Execution Time - New Execution Time}}{Old Execution Time}$
**Amdahl's Law**: $\text{Time}_{after}=\frac{\text{Time}_{affected}}{\text{Amount of Improvement}} + \text{Time}_{unaffected}$ 

*Example*: A processor spends 20% of its time on ADD instructions.  An engineer proposes to improve the speed of the ADD instruction by 4 times.  What is the speedup achieved by this modification?

$\text{Time} = 0.2/4 +0.8 = 0.85$
$\text{Speedup}=1/0.85=1.18 \space \text{or 18\% improvement}$ 

## Execution Time
___
CPI stands for "Cycles Per Instruction"
Execution Time =  $n$ * $CPI_{avg}$ * clock cycle time, where $n$ is the number of instructions
## Frequency
____
**Static**: Static frequency refers to number of times a particular instruction occurs in compiled code. Impact memory footprint.
**Dynamic**: Dynamic instruction frequency refers to number of times a particular instruction is executed when program is run. Impacts execution time of program.

*Example*: ADD instruction occurs twice in a program that contains a total of 1000 instructions in the compiled code.  All 1000 instructions get executed during a program run.  One of the ADD instructions is in a 5-instruction loop that gets executed 1000 times.

Static Frequency: $\frac{2}{1000} \times 100=0.2\%$  
Dynamic Frequency: $\frac{1+1000}{1000-5 + 5000} \times 100 = 16.69\%$ 