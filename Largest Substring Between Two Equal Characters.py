class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # leng:記錄新的子字串的長度；leng1:紀錄原子字串的最長長度
        leng=0
        leng1=0
        #先抓取第一個字元
        for i in range(len(s)):
            # 檢查其後面有沒有重複地字元，如果有就紀錄其長度(長度為最長距離)
            for j in range(i+1,len(s)):
                # 找到重複的紀錄其長度
                if s[j]==s[i]:
                    leng=j-i
                    # 如果比原比得更長就更新
                    if leng>=leng1:
                        leng1=leng
        # 長度為1:他是連續的
        if leng1==1:
            return 0
        # 長度為0:沒有找到 
        elif leng1==0:
            return -1
        # 有找到的話需要將長度-1(扣掉自己)
        else:
            return leng1-1
