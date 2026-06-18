# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150 

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
       
        #defaultdict() automatically creates an empty list [] for any new key
        #you can .append() without checking if the key exists first
        anagram_map = defaultdict(list)
        
        for str in strs:
            #anagrams all have the same letters, so when sorted they produce the SAME string **key concept!
            sorted_key = "".join(sorted(str))
            
            #so now all the anagrams are appended together under the same key
            anagram_map[sorted_key].append(str)
            
        #returns all grouped lists, and then you can cast it to a list!
        return list(anagram_map.values())
    
#Test cases
solution = Solution()
print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(strs = ["rat","evil","tar","silent","listen","vile", "annika2"]))