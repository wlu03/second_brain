The **edit distance** or **Levenshtein distance** is the minimum number of editing operations needed to transform a string to another string. The following operations are: 
- Insert a character
- remove a character
- modify a character

For example, the edit distance between LOVE and MOVIE is 2 because we can first perform the operation to modify LOVE->MOVE (modify). Then I will add a character to MOVE->MOVIE (insert). Suppose that we are given a string $x$ and a length $n$ and a string $y$ of length $m$, we want to calculate the distance between $x$ and $y$. To solve this problem, I want to define $distance(a,b)$ that gives the edit distance between prefixes $x[0...a]$ and $y[0...b]$. Thus using this function, the edit distance between x and y equals to $distance(n-1,m-1)$. We calculate values of distance as following: $$distance(a,b)=min(distance(a,b-1)+1, distance(a-1,b+1), distance(a-1,b-1) + cost(a,b))$$ The $cost(a,b)=0$ if $x[a]=y[b]$, and otherwise $cost(a,b)=1$. The formula considers different ways to edit the string x:
- $distance(a,b-1)$ inserts a character at the end of x 
- $distance(a-1,b)$ remove a character at the end of x 
- $distance(a-1,b-1)$ match or modify the last character of x
- ![[Screenshot 2025-03-04 at 2.18.14 AM.png | 400]]
- **First Row**
	- To convert an empty string ("") to MOVIE we need to insert each letter which all incur a cost of 1. 
- **First Column**
	- Converting LOVE to an empty string we need to remove each letter which all takes an operation
- **Fill in Rest of Table**
	- Compare each letter, if they match no cost is added
	- If they don't match, choose minimum edit operation

### Row 1: Comparing "L" with "MOVIE"

|     | ""  | M     | O     | V     | I     | E     |
| --- | --- | ----- | ----- | ----- | ----- | ----- |
| ""  | 0   | 1     | 2     | 3     | 4     | 5     |
| L   | 1   | **1** | **2** | **3** | **4** | **5** |

- `"L"` vs. `"M"` → **Replace "L" with "M"** (cost = 1).
- `"L"` vs. `"MO"` → **Insert "O"** (cost = 2).
- `"L"` vs. `"MOV"` → **Insert "V"** (cost = 3).
- `"L"` vs. `"MOVI"` → **Insert "I"** (cost = 4).
- `"L"` vs. `"MOVIE"` → **Insert "E"** (cost = 5).

