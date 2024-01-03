# LeetCode_Practice
## [Two Sum](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Two%20Sum.py)
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
## [Palindrome Number](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Palindrome%20Number.py)
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
 ## [Longest Substring Without Repeating Characters](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Longest%20Substring%20Without%20Repeating%20Characters.py)
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
## [Reverse Integer](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Reverse%20Integer.py)
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
## [Largest Substring Between Two Equal Characters](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Largest%20Substring%20Between%20Two%20Equal%20Characters.py)
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
##
## [Roman to Integer](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Roman%20to%20Integer.py)
羅馬數字以七個不同的符號表示：  I、V、X、L、C和D。M

符號       值
I          1 
V          5 
X          10 
L          50 
C          100 
D          500 
M          1000
例如， 2寫成II 羅馬數字，只是兩個數字相加。12寫成 XII，簡單地說就是X + II。該數27寫為XXVII，即XX + V + II。

羅馬數字通常從左到右從最大到最小書寫。然而，四的數字不是IIII。相反，數字四寫為IV。因為一在五之前，所以我們減去它，得到四。同樣的原理也適用於數字九，寫成IX。有六種使用減法的情況：

I可以放在V(5)和X(10)之前，得到4和9。 

X可以放在L(50) 和C(100) 之前，得到 40 和 90。 

C可以放在D(500) 和M(1000) 之前，得到 400 和 900。

給定一個羅馬數字，將其轉換為整數。

範例1：

輸入： s = "III"

輸出： 3

解釋： III = 3。

範例2：

輸入： s = "LVIII"

輸出： 58

解釋： L = 50，V= 5，III = 3。

範例3：

輸入： s = "MCMXCIV"

輸出： 1994

解釋： M = 1000、CM = 900、XC = 90 且 IV = 4。
 
限制條件：

1 <= s.length <= 15

s僅包含字元('I', 'V', 'X', 'L', 'C', 'D', 'M')。

保證 是範圍內的有效羅馬數字。s[1, 3999]
##
## [Convert an Array Into a 2D Array With Conditions](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Convert%20an%20Array%20Into%20a%202D%20Array%20With%20Conditions.py)
給你一個整數數組nums。nums您需要建立滿足以下條件的二維數組：

二維數組應僅包含數組的元素nums。

二維數組中的每一行都包含不同的整數。

二維數組中的行數應該最少。

傳回結果數組。如果有多個答案，則傳回其中任何一個。

請注意，二維數組每行可以有不同數量的元素。

範例1：

輸入： nums = [1,3,4,1,2,3,1]

輸出： [[1,3,4,2],[1,3],[1]]

解釋：我們可以建立一個二維數組包含以下行：

- 1,3,4,2

- 1,3

- 1

使用了 nums 的所有元素，而二維數組的每一行都包含不同的整數，因此這是一個有效的答案。

可以證明，有效數組中的行數不能少於 3 行。

範例2：

輸入： nums = [1,2,3,4]

輸出： [[4,3,2,1]]

解釋：陣列中的所有元素都是不同的，因此我們可以將它們全部保留在2D 的第一行中大批。
 
限制條件：

1 <= nums.length <= 200

1 <= nums[i] <= nums.length
##
## [Number of Laser Beams in a Bank](https://github.com/Dadanielwu/LeetCode_Practice/blob/main/Number%20of%20Laser%20Beams%20in%20a%20Bank.py)
當安全裝置被啟動後，銀行內部有一些防盜設備被啟用。你會拿到一個表示銀行格局的二維矩陣，其格式為 m x n 的 0-indexed 二進制字串陣列 bank。bank[i] 代表第 i 列，包含 '0' 和 '1' 兩種字元。'0' 代表該格子是空的，而 '1' 代表有安全裝置存在。

如果兩個安全裝置符合以下兩個條件，則它們之間會有一束雷射光：

1.兩個裝置位於不同的列，即 r1 和 r2，其中 r1 < r2。

2.對於每一列 i 滿足 r1 < i < r2 的條件下，該列中沒有其他的安全裝置存在。

雷射光是獨立的，也就是說，一束雷射光不會與另一束雷射光干擾或相交。

請返回銀行內總共有多少束雷射光。

Example 1:

輸入: bank = ["011001","000000","010100","001000"]

輸出: 8

解釋: 在每對以下設備之間，都有一束光。總共有 8 條光線：

bank[0][1] -- bank[2][1]

bank[0][1] -- bank[2][3]

bank[0][2] -- bank[2][1]

bank[0][2] -- bank[2][3]

bank[0][5] -- bank[2][1]

bank[0][5] -- bank[2][3]

bank[2][1] -- bank[3][2]

bank[2][3] -- bank[3][2]

請注意，第 0 列的設備與第 3 列的任何設備之間都沒有光線。

這是因為第 2 列包含安全設備，違反了第二個條件。

Example 2:

輸入：bank = ["000", "111", "000"]

輸出：0

解釋：不存在兩個設備位於不同的兩行之上。

限制條件：

m == bank.length

n == bank[i].length

1 <= m, n <= 500

bank[i][j] 要麼是 '0' 要麼是 '1'。
