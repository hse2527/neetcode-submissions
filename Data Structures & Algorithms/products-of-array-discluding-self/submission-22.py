class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [0] * len(nums)

        product = 1
        for i, num in enumerate(nums):
            sol[i] = product
            product *= num

        product = 1
        for i in range(len(nums)-1, -1, -1):
            sol[i] *= product
            product *= nums[i]

        return sol