class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            j = i + 1
            if target == (nums[i] + nums[j]):
                    output = [i, j]
                    return print(output)
            elif target != (nums[i] + nums[j]):
                for x in range(j, len(nums)):
                    if target == (nums[i] + nums[x]):
                        output = [i, x]
                        return print(output)

Solution.twoSum(nums=[2,7,11,15], target=9)
# Solution.twoSum(nums=[3,3], target=6)
# Solution.twoSum(nums=[3,2,3], target=6)