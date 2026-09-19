class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = False
        for num in nums:
            if num == 0 and not zero:
                zero = True
            elif num == 0 and zero:
                product = 0
            else:
                product *= num
        
        sol = []
        for num in nums:
            if num != 0 and zero:
                sol.append(0)
            elif num != 0:
                sol.append(int(product/num))
            else:
                sol.append(product)

        return sol
