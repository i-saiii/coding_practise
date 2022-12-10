# my leet code problems and answers

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

###my answer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if target-nums[i] in nums and ((nums.count(target-nums[i])==1) and(nums.index(target-nums[i])!=i)):
                l.append(i)
            elif target-nums[i] in nums and (nums.count(target-nums[i])>1):
                l.append(i)
        
        return l

###most accepted solution 2

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for idx, val in enumerate(nums):
                if target - val in nums[idx + 1:]:
                    return [idx, nums[idx + 1:].index(target - val) + (idx + 1)]


###most accepted solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i



