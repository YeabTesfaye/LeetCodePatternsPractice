# Maximum Average Subarray I - Solution

## Problem Description
Given an integer array `nums` of `n` elements, and an integer `k`, the task is to find a contiguous subarray of length `k` that has the maximum average value. Return this maximum average value. Any answer with a calculation error less than `10^-5` is accepted.

### Example
#### Example 1
- **Input:** `nums = [1,12,-5,-6,50,3]`, `k = 4`
- **Output:** `12.75000`
- **Explanation:** The maximum average is calculated from the subarray `[12, -5, -6, 50]` with sum `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`.

#### Example 2
- **Input:** `nums = [5]`, `k = 1`
- **Output:** `5.00000`

## Approach
The solution uses a sliding window technique to maintain a sum of a subarray of length `k`:
1. Start by calculating the sum of the first `k` elements.
2. Initialize `max_sum` to this initial window sum.
3. Slide the window across the array from index `k` to `n - 1`, adjusting the window sum by:
   - Adding the new element that enters the window.
   - Subtracting the element that exits the window.
4. Update `max_sum` to the maximum window sum encountered.
5. Return the maximum average as `max_sum / k`.

