class Solution:
    def numberOfBeams(self, bank):
      # 紀錄每個row有幾個1
        array=[]
      # 檢查此row是否有1
        for i in range(len(bank)):
            count=0
            if "1" in list(bank[i]):
              # 檢查有幾個1，紀錄於count中
                for j in range(len(bank[i])):
                    print(list(bank[i][j]))
                    if bank[i][j]=="1":
                        count+=1
              # 將結果紀錄於array中
                array.append(count)
       # 如果只有一個row有，救回傳0
        if len(array)==1:
            return 0
        else:
          # 否則就計算總共會有多少個路徑
            feeback=0
            for i in range(len(array)-1):
                feeback+=array[i]*array[i+1]
            return feeback
