'''
77. Combinations

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def solve(start , k , temp):
            if k == 0:
                result.append(temp[:])
                return
            if start > n:
                return

            temp.append(start)
            solve(start + 1 , k-1 , temp)
            temp.pop()
            solve(start + 1 ,k,temp)
        solve(1,k,[])
        return result