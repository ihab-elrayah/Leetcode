""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
    
"""

#Answer with notes
#Took 43 minutes solve
#7-10 dif

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if s and t are of different lengths (not anagrams)
        if len(s) != len(t):
            return False
        
        # Initialize dictionaries to count occurrences of each character
        countS, countT = {}, {}

        # Populate count dictionaries for both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # Increment count for char in s
            countT[t[i]] = 1 + countT.get(t[i], 0)  # Increment count for char in t
        
        # Compare character counts in both strings
        for c in countS:
            if countS[c] != countT.get(c, 0):  # If mismatch found, not anagrams
                return False

        # If no mismatches found, strings are anagrams
        return True

