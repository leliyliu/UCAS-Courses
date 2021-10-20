# max-Subarray-Sum-with-One-Deletion
## Problem Description
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

All input and output content are within the range of long long.

## Input
An array of integers

## Output
The maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion.

## Sample Input 1:
```
1 -2 0 3
```
## Sample Output 1:
```
4
```
Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
## Sample Input 2:
```
1 -2 -2 3
```
## Sample Output 2:
```
3
```
We just choose [3] and it's the maximum sum.