from typing import Literal


def find_duplicate(nums: list[int]) -> int | Literal[False]:

    nums.sort()

    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1] and nums[index] > 0:
            return nums[index]
    return False
