#SOLUTION:
class Solution:
    def longestCommonPrefix(self, l):
        l.sort()
        r=""
        le=len(l)
        a=l[0]
        b=l[le-1]
        for i in range(0,min(len(a),len(b))):
            if(a[i]!=b[i]):
                return r
            r+=a[i]
        return r
        
"""14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""
