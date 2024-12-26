'''
question link: 
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

question :
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

'''
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:

        k = len(nums1) - 1
        ptr1 = m-1
        ptr2 = n-1
        
        while ptr1>=0 and ptr2 >= 0:
            if nums1[ptr1] >= nums2[ptr2]:
                nums1[k] = nums1[ptr1]
                k=k-1
                ptr1 = ptr1 - 1
            else:
                nums1[k] = nums2[ptr2]
                ptr2 = ptr2 - 1
                k=k-1
        while ptr1 >= 0:
                nums1[k] = nums1[ptr1]
                k=k-1
                ptr1 = ptr1 - 1
        while ptr2 >= 0:
                nums1[k] = nums2[ptr2]
                ptr2 = ptr2 - 1
                k=k-1


# Test the solution
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)