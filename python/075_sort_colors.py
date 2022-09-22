from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:  # Red
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:  # White
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


Solution().sortColors([2, 0, 2, 1, 1, 0])
Solution().sortColors([2, 0, 1])
