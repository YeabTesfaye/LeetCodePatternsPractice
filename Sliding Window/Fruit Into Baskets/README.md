# Longest Subarray with At Most Two Distinct Fruits

## Problem Description

Given an array of integers `fruits` representing different types of fruits in a basket, you need to determine the length of the longest contiguous subarray that contains at most two distinct types of fruits. This problem can be solved using a sliding window approach.

### Example

#### Example 1:
- **Input**: `fruits = [1, 2, 1]`
- **Output**: `3`
- **Explanation**: The longest subarray with at most 2 distinct fruits is the entire array `[1, 2, 1]` which has length 3.

#### Example 2:
- **Input**: `fruits = [0, 1, 2, 2]`
- **Output**: `3`
- **Explanation**: The longest subarray with at most 2 distinct fruits is `[1, 2, 2]` which has length 3.

#### Example 3:
- **Input**: `fruits = [1, 2, 3, 2, 2]`
- **Output**: `4`
- **Explanation**: The longest subarray with at most 2 distinct fruits is `[2, 3, 2, 2]` which has length 4.

## Approach

This problem can be solved using the **sliding window** technique, where we maintain a window of valid subarrays and adjust the window size to keep the number of distinct elements less than or equal to 2.

### Steps:
1. Use two pointers (`left` and `right`) to represent the current sliding window.
2. Expand the window by moving the `right` pointer and keep track of the frequency of each fruit in a hashmap.
3. If the number of distinct fruits exceeds 2, move the `left` pointer to shrink the window until the number of distinct fruits is 2 or fewer.
4. At each step, calculate the length of the current valid window and update the maximum length found.
