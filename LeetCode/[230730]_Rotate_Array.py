class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        self.sort(nums, 0, length - 1)
        self.sort(nums, 0, k - 1)
        self.sort(nums, k, length - 1)
        print(nums)

    def sort(self, nums: list, start: int, end: int):
        while (start != end and start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
print(f'case 1 is [5, 6, 7, 1, 2, 3, 4]\n')

solution.rotate([-1], 2)
print(f'case 2 is [-1]\n')

solution.rotate([1, 2], 3)
print(f'case 3 is [1, 2]')