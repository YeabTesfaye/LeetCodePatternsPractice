from collections import defaultdict

def totalFruit(fruits):
    fruits_freq_map = defaultdict(int)
    max_len = 0
    left  = 0

    for right in range(len(fruits)):
        fruits_freq_map[fruits[right]] += 1
        while len(fruits_freq_map) > 2:
            fruits_freq_map[fruits[left]] -= 1

            if fruits_freq_map[fruits[left]] == 0:
                del fruits_freq_map[fruits[left]]
            
            left += 1
        
        max_len = max(max_len, (right-left+1))
    return max_len




# Test cases
print(totalFruit([1,2,1]))  # Output: 3
print(totalFruit([0,1,2,2]))  # Output: 3
print(totalFruit([1,2,3,2,2]))  # Output: 4
