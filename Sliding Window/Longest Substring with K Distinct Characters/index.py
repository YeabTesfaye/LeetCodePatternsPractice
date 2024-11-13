from collections import defaultdict

def findLength(s, k):
    char_frequency_map = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        char_frequency_map[s[right]] += 1

        while len(char_frequency_map) > k:
            char_frequency_map[s[right]] -= 1

            if char_frequency_map[s[right]] == 0:
                del char_frequency_map[s[right]]
            
            left += 1
        max_len = max(max_len, (right-left + 1))

    return max_len


            
# Test cases
print(findLength("araaci", 2))  # Output: 4
print(findLength("araaci", 1))  # Output: 2
print(findLength("cbbebi", 3))  # Output: 5
