class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1

        while a < b:
            numa, numb = numbers[a], numbers[b]
            total = numa + numb
            
            if total == target:
                return [a+1, b+1]
            elif total > target:
                b -= 1
            elif total < target: 
                a += 1