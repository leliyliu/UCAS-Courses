# Climbing-Broken-Stairs
## Problem Description
You are climbing a stair case. It takes xx steps to reach to the top.

However, not every step you can step on because some steps may be broken.

Given a list of steps' positions in sorted ascending order which contain all steps you can step on (named "unbroken step"), determine if you are able to reach to the top by stepping on the last unbroken step. Initially, you are on the first step and assume the first climb must be 1 step.

If your last climb was k steps, then your next climb must be either k−1, k, or k+1 step. Note that you can only climb in the forward direction.

## Note

1.The number of unbroken steps is ≥ 2 and is < 1,000.

2.Each unbroken steps position will be a non-negative integer < 2^31.

3.The first unbroken step's position is always 0.

## Input
Line1: the length of the list

Line2: the all elements in List and split by spaces

## Output
Line1: true or false
## Sample Input 1:
```
8
0 1 2 4 5 7 11 16
```
## Sample Output 1:
```
true
```
Return true. You can reach to the top by climbing 1 step to the 2nd unbroken step, then 1 step to the 3rd unbroken step, then 2 steps to the 4th unbroken step, then 3 steps to the 6th unbroken step, then 4 steps to the 7th unbroken step, and 5 steps to the 8th unbroken step.
## Sample Input 2:
```
7
0 1 2 3 7 8 12
```
## Sample Output 2:
```
false
```
Return false. You can’t reach to the top as the gap between the 4th and 5th unbroken step is too large.