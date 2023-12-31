class Solution:
    def isPalindrome(self, x: int) -> bool:
        number=str(x)
        # 將int轉成array儲存
        number_array = [str(digit) for digit in number]
        # 反轉陣列
        number_array_change=number_array[::-1]
        # 檢查兩陣列是否一致
        if number_array==number_array_change:
            return True
        else:
            return False
