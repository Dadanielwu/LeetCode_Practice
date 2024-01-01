class Solution:
    def romanToInt(self, s: str) -> int:
      # count:計算最終數字 i:計算到第幾個單字
        count=0
        i=0
      # 檢查某些單字後面是否連接需要經特殊處理的單字
        while i<len(s):
          # 如果以檢查到最後一個則無需檢查下一個
            if s[i]=="I":
                if i==len(s)-1:
                    count+=1
                else:
                    if s[i+1]=="V":
                        count+=5-1
                      # 下次檢查時可以不用再看一次
                        i+=1
                    elif s[i+1]=="X":
                        count+=10-1
                        i+=1
                    else:
                        count+=1
            elif s[i]=="X":
                if i==len(s)-1:
                    count+=10
                else:
                    if s[i+1]=="L":
                        count+=50-10
                        i+=1
                    elif s[i+1]=="C":
                        count+=100-10
                        i+=1
                    else:
                        count+=10
            elif s[i]=="C":
                if i==len(s)-1:
                    count+=100
                else:
                    if s[i+1]=="D":
                        count+=500-100
                        i+=1
                    elif s[i+1]=="M":
                        count+=1000-100
                        i+=1
                        print("I",i)
                    else:
                        count+=100
            elif s[i]=="V":
                count+=5
            elif s[i]=="L":
                count+=50
            elif s[i]=="D":
                count+=500
            elif s[i]=="M":
                count+=1000
          # 每次檢查完都往後跳一個
            i+=1
        return count
