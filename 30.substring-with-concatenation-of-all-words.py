#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#


# @lc code=start
class Solution:
    def findSubstring(self, s, words):
        # init all the vars
        stepNum = len(words)
        stepWidth = len(words[0])
        windowSize = stepNum * stepWidth
        window = ""
        hashmap1 = {}
        # get word name and their counts
        for i in words:
            if not i in hashmap1:
                hashmap1[i] = 1
            else:
                hashmap1[i] += 1
        ans = []
        left = 0
        right = 0
        while right < len(s):
            if len(window) < windowSize:
                # we add new space to the window
                # if it is not the size required
                window += s[right]
            if len(window) == windowSize:
                # the size is correct,then we can start checking
                hashmap2 = {}
                flag = 1
                count = 0
                while count < stepNum and flag:
                    curWord = window[count * stepWidth : (count + 1) * stepWidth]
                    if not curWord in hashmap1:
                        # the word is not in the WORDS list
                        flag = 0
                    else:
                        # we add the counts up
                        # to check if it exceeds the counts in the WORDS list.
                        count += 1
                        if not curWord in hashmap2:
                            hashmap2[curWord] = 1
                        else:
                            hashmap2[curWord] += 1
                        if hashmap2[curWord] > hashmap1[curWord]:
                            flag = 0
                if flag == 1:
                    # if we go to this step with flag=1,
                    # that means the string is correct
                    ans.append(left)
                window = window[1:windowSize]
                left += 1
            right += 1
        return ans


# l = "a"
# r = ["a", "a"]
# Solution.findSubstring(Solution, l, r)

# @lc code=end
