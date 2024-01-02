class Solution:
    def findMatrix(self, nums):
      # array:紀錄目前的array；array1:要回傳的array，會是二為陣列；array2:紀錄已經存過的元素位置
        array=[]
        array1=[]
        array2=[]
      # 確保都跑過一遍
        while True:
          # 從頭開始檢查
            for i in range(len(nums)):
              # 如果跑過的位置已經儲存過了就跳過
                if i not in array2:
                  # 檢查當前的array可不可以再新增新的元素
                    if nums[i] not in array:
                      # 新增元素，並將座標作紀錄
                        array.append(nums[i])
                        array2.append(i)
          # 將這次跑完的array做儲存
            array1.append(array)
          # 清空array
            array=[]
          # 如果所有的座標都已儲存就結束
            if len(array2)==len(nums):
                break
      # 回傳結果
        return array1
