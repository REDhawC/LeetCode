#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#


# @lc code=start
class Solution:
    def fullJustify(self, words, maxWidth: int):
        count = 0
        words_count = -1
        ans_Array = []
        s = []
        temp = []
        for i in range(len(words)):
            len_word = len(words[i])
            count += len_word
            words_count += 1
            if count + words_count > maxWidth:
                count = 0
                words_count = -1
                temp.append(words[i])
                ans_Array.append(s)
                s = []
            else:
                if len(temp) > 0:
                    s.append(temp[0])
                    len_word = len(temp[0])
                    count += len_word
                    words_count += 1
                    temp = []
                    if count + words_count > maxWidth:
                        count = 0
                        words_count = -1
                        temp.append(words[i])
                        ans_Array.append(s)
                        s = []
                        continue
                s.append(words[i])
        if len(s) > 0:
            ans_Array.append(s)
        else:
            ans_Array.append(temp)
        # print(ans_Array)

        def padZero(arr, maxWidth):
            len_arr = len(arr)
            new_item = ""
            for i in range(len_arr):
                if i == len_arr - 1:
                    new_item = " ".join(arr[i]) + " " * (
                        maxWidth - len(" ".join(arr[i]))
                    )
                else:
                    len_row = len(arr[i])

                    total_words_len = len("".join(arr[i]))
                    if len_row == 1:
                        new_item = "".join(arr[i]) + " " * (maxWidth - total_words_len)
                    else:
                        join_Item = " " * (
                            (maxWidth - total_words_len) // (len_row - 1)
                        )
                        new_item = join_Item.join(arr[i])
                        if ((maxWidth - total_words_len) % (len_row - 1)) != 0:
                            new_item = new_item.replace(
                                " ",
                                "  ",
                                # * ((maxWidth - total_words_len) % (len_row - 1) + 1)
                                ((maxWidth - total_words_len) % (len_row - 1)),
                            )
                arr[i] = new_item

        padZero(ans_Array, maxWidth)

        return ans_Array


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
Solution.fullJustify(Solution, words, maxWidth)


# @lc code=end
