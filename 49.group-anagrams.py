#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs):
        hashmap_word = {}
        # loop the strs
        for word in strs:
            # using sorted to sort strings, super efficient!
            curWord = "".join(sorted(word))
            if curWord not in hashmap_word:
                hashmap_word[curWord] = list()
            hashmap_word[curWord].append(word)
        return hashmap_word.values()

        # hashmap_word = {}
        # # loop the strs
        # for word in strs:
        #     # init a list to save chars in one word
        #     hashList = []
        #     for char in word:
        #         hashList.append(char)
        #     hashList.sort()
        #     # sort the list and make it a tuple
        #     # cause tuple is hashable, while list isn't
        #     hashTuple = tuple(hashList)
        #     if hashTuple not in hashmap_word:
        #         # when encounter new tuple combination,
        #         # init a new list in hashmap
        #         hashmap_word[hashTuple] = list()
        #     hashmap_word[hashTuple].append(word)
        # # we can directly return submission by using dict.values()
        # return hashmap_word.values()


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Solution.groupAnagrams(Solution, strs)


# @lc code=end
