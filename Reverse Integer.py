class Solution:
    def reverse(self, x: int) -> int:
        array=[]
        # 當x小於0，先將其變成正的，將數字反轉後，再變回負的
        if x<0:
            x=x*(-1)
            # int轉成str
            number=str(x)
            # 將str轉成array儲存
            number_array = [str(digit) for digit in number]
            # 反轉陣列
            number_array_change=number_array[::-1]
            # 將lsit轉成str
            number_change = ','.join(str(num) for num in number_array_change)
            # 去除掉，
            number_change = number_change.replace(",", "")
            # 轉回數字
            number_change=int(number_change)
            # 加上負號
            number_change=number_change*(-1)
            # 如果超出range則返回0，反之回傳翻轉後的數字
            if number_change<(-1)*(2**(31)) or number_change>(2**(31)-1):
                return 0
            return number_change
        else:
            number=str(x)
            # 將int轉成array儲存
            number_array = [str(digit) for digit in number]
            # 反轉陣列
            number_array_change=number_array[::-1]
            number_change = ','.join(str(num) for num in number_array_change)
            number_change = number_change.replace(",", "")
            number_change=int(number_change)
            if number_change<(-1)*(2**(31)) or number_change>(2**(31)-1):
                return 0
            return number_change
