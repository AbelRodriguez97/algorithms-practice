"""
Problem: Two Sum
Source: LeetCode — #1
Difficulty: Easy

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not
use the same element twice.

Approach:
- Use a hash map to store each number's index as we iterate.
- For each number, check if (target - number) is already in the map.
- If yes, we found the pair. If not, store the current number and continue.

Complexity:
- Time:  O(n) — single pass through the array
- Space: O(n) — the hash map may store up to n entries
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    # Example 1
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Example 2
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Example 3
    assert two_sum([3, 3], 6) == [0, 1]

    print("All tests passed ✅")