# LeetCode_Practice
## [Two Sum](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Two%20Sum)
給定一個整數數組nums 和一個整數target，傳回兩個數字的索引，使它們相加為target。您可以假設每個輸入都有一個解決方案，並且您不能兩次使用相同的元素。您可以按任意順序返回答案。

範例1：

輸入： nums = [2,7,11,15], target = 9

輸出： [0,1]

解釋：因為 nums[0] + nums[1] == 9，所以我們回傳 [0, 1]。

範例2：

輸入： nums = [3,2,4]，目標 = 6

輸出： [1,2]

範例3：

輸入： nums = [3,3]，目標 = 6

輸出： [0,1]

限制條件：

2 <= nums.length <= 104

-109 <= nums[i] <= 109

-109 <= target <= 109

只有一個有效答案。


追問： 你能想出一個小於時間複雜度的演算法嗎？O(n2)

##
## [Palindrome Number](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Palindrome%20Number)
給定一個整數x，如果x是一個回文則傳回true，否則回傳false。

範例1：

輸入： x = 121

輸出： true

解釋： 121 從左到右讀為 121，從右到左讀為 121。

範例2：

輸入： x = -121

輸出： false

解釋：從左到右，讀取的是 -121。從右到左，變成121-。因此它不是回文。

範例3：

輸入： x = 10

輸出： false

解釋：從右向左讀取 01。因此它不是回文。

 ## 
 ## [Longest Substring Without Repeating Characters](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Longest%20Substring%20Without%20Repeating%20Characters)
給定一個字串，找出最長s的長度子字串，沒有重複字元。

範例1：

輸入： s = "abcabcbb"

輸出： 3

解釋：答案是“abc”，長度為 3。

範例2：

輸入： s = "bbbbb"

輸出： 1

解釋：答案是 "b"，長度為 1。

範例3：

輸入： s = "pwwkew"

輸出： 3

解釋：答案是“wke”，長度為 3。

請注意，答案必須是子字串，“pwke”是子序列而不是子字串。
 

限制條件：

0 <= s.length <= 5 * 104

s由英文字母、數字、符號和空格組成。

限制條件：

-231 <= x <= 231 - 1
 

追問：你能在不將整數轉換為字串的情況下解決這個問題嗎？
##
## [Reverse Integer](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Reverse%20Integer)
給定一個帶符號的 32 位元整數x，傳回x其數字反轉的值。如果反轉x導致值超出有符號 32 位元整數範圍[-231, 231 - 1]，則傳回0。

假設環境不允許您儲存 64 位元整數（有符號或無符號）。

範例1：

輸入： x = 123

輸出： 321

範例2：

輸入： x = -123

輸出： -321

範例3：

輸入： x = 120

輸出： 21
 
限制條件：

-231 <= x <= 231 - 1

##
## [Reverse Integer](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Reverse%20Integer)
給定一個 string s，傳回兩個相等字元之間最長子字串的長度，不包括這兩個字元。如果沒有這樣的子字串則回傳-1。子字串是字串中連續的字元序列。

範例1：

輸入： s = "aa"

輸出： 0

解釋：這裡的最佳子字串是兩個 之間的空子字串'a's。

範例2：

輸入： s = "abca"

輸出： 2

解釋：這裡的最佳子字串是 "bc"。

範例3：

輸入： s = "cbzxy"

輸出： -1

解釋： s 中沒有出現兩次的字元。
 

限制條件：

1 <= s.length <= 300

s僅包含小寫英文字母。
