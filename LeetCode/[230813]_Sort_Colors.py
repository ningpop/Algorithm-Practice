class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3
        for i in nums:
            count[i] += 1

        answer_sample = [0] * count[0] + [1] * count[1] + [2] * count[2]

        for i in range(len(nums)):
            nums[i] = answer_sample[i]

        print(nums)



solution = Solution()
solution.sortColors([2, 0, 2, 1, 1, 0])
