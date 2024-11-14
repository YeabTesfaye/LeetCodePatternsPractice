# Longest Substring with Same Letters after Replacement - Solution

## Problem Description
Given a string `s` and an integer `k`, the task is to find the length of the longest substring that can be obtained by replacing at most `k` characters, such that all characters in the substring are the same. 

### Example
#### Example 1
- **Input:** `s = "aabccbb"`, `k = 2`
- **Output:** `5`
- **Explanation:** The longest substring with the same letters after at most 2 replacements is `"bbbbb"`, achieved by replacing the 'a' and 'c' characters.

#### Example 2
- **Input:** `s = "abbcb"`, `k = 1`
- **Output:** `4`
- **Explanation:** The longest substring with the same letters after at most 1 replacement is `"bbbb"`, achieved by replacing the first 'a' with 'b'.

#### Example 3
- **Input:** `s = "abccde"`, `k = 1`
- **Output:** `3`
- **Explanation:** The longest substring with the same letters after at most 1 replacement is `"bcc"`.

## Approach
The solution uses a sliding window technique along with a frequency count of characters to determine the length of the longest valid substring:
1. Initialize two pointers (`left` and `right`) to represent the current sliding window.
2. Maintain a frequency map (`charCount`) to track the count of characters in the window.
3. As we expand the window by moving the `right` pointer, we keep track of the most frequent character (`maxRepeatLetterCount`) in the window.
4. If the window size minus the frequency of the most common character exceeds `k`, it means more than `k` replacements are needed, so we shrink the window from the left by moving the `left` pointer.
5. At each step, update the maximum length of the valid window.

### Steps:
1. Start with both pointers `left` and `right` at the beginning of the string.
2. Expand the window by moving the `right` pointer and update the frequency of the character at the `right` pointer.
3. Check if the window is valid (i.e., if the number of replacements needed is less than or equal to `k`).
4. If the window is invalid, shrink it from the left.
5. Track the maximum length of the valid window as you progress through the string.

### Time Complexity:
The time complexity is **O(n)**, where `n` is the length of the string. The `left` and `right` pointers each traverse the string once, and dictionary operations for counting characters are O(1) on average.

### Space Complexity:
The space complexity is **O(1)**, since the frequency map will store at most 26 characters (for lowercase English letters), making it a constant space operation.


