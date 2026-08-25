class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ll = 0
        r = len(numbers) - 1
        while ll < r:
            sum = numbers[ll] + numbers[r]
            if sum == target:
                return [ll + 1 ,r + 1]
            elif sum < target:
                ll  += 1
            else:
                r -= 1