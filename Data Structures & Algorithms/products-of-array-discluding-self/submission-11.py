class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [0] * len(nums)
        rightProduct = [0] * len(nums)

        product = 1
        for i, num in enumerate(nums):
            leftProduct[i] = product
            product *= num

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            rightProduct[i] = product
            product *= nums[i]
        
        sol = []
        for i in range(len(nums)):
            sol.append(leftProduct[i]*rightProduct[i])

        return sol