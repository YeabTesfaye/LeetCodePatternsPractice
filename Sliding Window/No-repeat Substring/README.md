# Longest Substring Without Repeating Characters

This Python project contains a function to determine the length of the longest substring without repeating characters from a given input string.

## Problem Statement

Given a string `s`, the task is to find the length of the longest substring with no repeating characters.

### Example Scenarios

1. **Input**: `"abcabcbb"`
   - **Output**: `3`
   - **Explanation**: The longest substring without repeating characters is `"abc"`.

2. **Input**: `"pwwkew"`
   - **Output**: `3`
   - **Explanation**: The longest substring without repeating characters is `"wke"`.

3. **Input**: `"bbbb"`
   - **Output**: `1`
   - **Explanation**: The longest substring without repeating characters is `"b"`.

## Solution Approach

This problem is solved using a **sliding window technique** combined with a **dictionary** to track the most recent index of each character as we iterate through the string.

### Detailed Steps
1. Initialize:
   - `char_map`: a dictionary to store the last seen index of each character.
   - `max_len`: an integer to keep track of the maximum length of any valid substring found.
   - `left`: an integer representing the starting position of the sliding window.

2. Iterate through the string using a `right` pointer (which marks the end of the current window):
   - If `s[right]` is already in `char_map`, update the `left` pointer to `char_map[s[right]] + 1` to ensure no duplicates are in the window.
   - Update the last seen index of `s[right]` in `char_map`.
   - Calculate the current window size `(right - left + 1)` and update `max_len` if this window is the largest found.

3. Return `max_len` after iterating through the entire string.

