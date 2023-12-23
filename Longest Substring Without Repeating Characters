# 回傳最長子串列長度
class Solution:
    def lengthOfLongestSubstring(self, s: str, count=0) -> int:
        # 如果是空字串直接回傳0
        if s=="":
            return 0
        else:
            array=[]
            # 如果不是空的至少會有一個長度
            a=1 # array 長度
            b=0 # array2 長度
            # 將str轉成list
            input_array = [str(word) for word in s]
            # 檢查count是否超出限制
            if count<len(input_array):
                # 將第一個字元放入
                array.append(input_array[count])
            # 如果重複則遞迴呼叫，否則就將字元放入
            for i in range(count+1,len(input_array)):
                if s[i] in array:
                    # count用來記錄下一個起始點
                    count+=1
                    b=self.lengthOfLongestSubstring(input_array,count)
                    break
                else:
                    array.append(input_array[i])
                    a=len(array)
            if b>a:
                return b
            else:
                return a

# 回傳最長子串列
class Solution:
    def lengthOfLongestSubstring(self, s: str, count=0) -> int:
        if s=="":
            return ""
        else:
            array=[]
            array2=[]
            input_array = [str(word) for word in s]
            array.append(input_array[count])
            for i in range(count+1,len(input_array)):
                if s[i] in array:
                    count+=1
                    array2=self.lengthOfLongestSubstring(input_array,count)
                    break
                else:
                    array.append(input_array[i])
            if len(array2)>len(array):
                return array2
            else:
                return array

# 輸入
solution = Solution()
final=solution.lengthOfLongestSubstring(s="asbdyfheaddfds")
print(final)
