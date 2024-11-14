def characterReplacement(s, k):
    charCount = {}
    maxLen = 0
    left = 0
    maxRepeatLetterCount = 0

    for right in range(len(s)):
        charCount[s[right]] = charCount.get(s[right], 0) + 1
        
        maxRepeatLetterCount = max(maxRepeatLetterCount, charCount[s[right]])

        # Check if the current window is valid
        windowSize = right - left + 1
        if windowSize - maxRepeatLetterCount > k:
            charCount[s[left]] -= 1
            left += 1

        # Update the maximum length of the valid window
        maxLen = max(maxLen, right - left + 1)

    return maxLen

# Test cases
print(characterReplacement("aabccbb", 2))  # Output: 5
print(characterReplacement("abbcb", 1))  # Output: 4
print(characterReplacement("abccde", 1))  # Output: 3
