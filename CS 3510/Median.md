Median of a list of numbers is its 50th percentile. Half the number are bigger and half are smaller. Median is used to summarize a set of numbers by a single value. 

## Selection Algorithm
____
This is a [[divide and conquer algorithm]] for selection. For any number $v$ imagine splitting up the list $S$ into three arrays: elements smaller than $v$, elements bigger than $v$, and elements equal to $v$. We can call these $S_L,S_v, S_R$. For instance if an array is equal to: 

| 2   | 36  | 5   | 21  | 8   | 13  | 11  | 20  | 5   | 4   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and you want to split for $v=5$, then $S_L=[2,4,1], S_v=[5,5], \; \text{and} \; S_R=[36, 21, 8, 13, 11, 20]$. 