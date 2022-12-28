from typing import List, Tuple


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0 for _ in range(len(nums))]

        def merge(
            left: List[Tuple[int]], right: List[Tuple[int]]
        ) -> List[Tuple[int]]:
            result = []
            left_idx = right_idx = 0
            while left_idx < len(left) and right_idx < len(right):
                if left[left_idx][1] <= right[right_idx][1]:
                    counts[left[left_idx][0]] += right_idx
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1

            for i in range(left_idx, len(left)):
                counts[left[i][0]] += right_idx
                result.append(left[i])

            for i in range(right_idx, len(right)):
                result.append(right[i])

            return result

        def merge_sort(nums: List[Tuple[int]]) -> List[Tuple[int]]:
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

        merge_sort(list(enumerate(nums)))

        return counts


# print(Solution().countSmaller([5, 2, 6, 1]))

print(
    Solution().countSmaller(
        [
            26,
            78,
            27,
            100,
            33,
            67,
            90,
            23,
            66,
            5,
            38,
            7,
            35,
            23,
            52,
            22,
            83,
            51,
            98,
            69,
            81,
            32,
            78,
            28,
            94,
            13,
            2,
            97,
            3,
            76,
            99,
            51,
            9,
            21,
            84,
            66,
            65,
            36,
            100,
            41,
        ]
    )
)
