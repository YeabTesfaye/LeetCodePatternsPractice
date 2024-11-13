# Longest Substring with K Distinct Characters

## Problem Description

Given a string `s` and an integer `k`, find the length of the longest substring that contains **no more than** `k` distinct characters.

### Example

#### Example 1:
- **Input**: `s = "araaci"`, `k = 2`
- **Output**: `4`
- **Explanation**: The longest substring with at most 2 distinct characters is `"araa"`, and its length is `4`.

#### Example 2:
- **Input**: `s = "araaci"`, `k = 1`
- **Output**: `2`
- **Explanation**: The longest substring with exactly 1 distinct character is `"aa"`, and its length is `2`.

#### Example 3:
- **Input**: `s = "cbbebi"`, `k = 3`
- **Output**: `5`
- **Explanation**: The longest substrings with at most 3 distinct characters are `"cbbeb"` and `"bbebi"`, and their lengths are both `5`.

## Approach

To solve this problem efficiently, we use the **Sliding Window** technique:

1. **Initialize the sliding window**: 
   - Use two pointers (`left` and `right`) to define a window within the string. Start both pointers at the beginning of the string.
   - Use a dictionary (`char_frequency_map`) to store the frequency of each character in the current window.

2. **Expand the window**:
   - Iterate through the string using the `right` pointer and add each character to the frequency map.

3. **Shrink the window if needed**:
   - If the number of distinct characters in the window exceeds `k`, move the `left` pointer to the right to shrink the window, while adjusting the frequency of characters in the map.

4. **Track the maximum length**:
   - After every step of expanding or shrinking the window, calculate the length of the current valid window (`right - left + 1`) and update the maximum length found so far.

