# Problem Name : Remove Duplicates from Sorted Array
# Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Input Operation
# nums=list(map(int, input().split()))
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Input Operation End
        # Solution Start
        mySet=set(nums)
        for i in range(len(mySet)):
            nums[i]=sorted(list(mySet))[i]
        return len(mySet)