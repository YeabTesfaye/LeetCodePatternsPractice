
def lengthOfLongestSubstring(s):

    char_map = {}
    max_len = 0
    left = 0

    for right in range(len(s)):

        if s[right] in char_map:
            left = max(left, char_map.get(s[right]) + 1)

        char_map[s[right]] = right
        max_len = max(max_len, (right-left+1))
    return max_len

# Test cases
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("pwwkew"))  # Output: 3
print(lengthOfLongestSubstring("bbbb"))  # Output: 1
