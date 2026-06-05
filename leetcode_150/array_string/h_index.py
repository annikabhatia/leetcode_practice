# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150\

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #if len(citations) == 1:
        citations.sort()
        max = 0
        last = len(citations)
        

        for i in range(0, last):
            if last - i >= citations[i]: # 1 > 100 ? NO
                max = citations[i]
            elif last - i > max: # 1 > 0 ? YES
                max = last - i
        return max

# Example usage:
solution = Solution()
citations = [3, 0, 6, 1, 5]
result = solution.hIndex(citations)
print(result)  # Output: 3 (because there are 3 papers with at least 3 citations each)
