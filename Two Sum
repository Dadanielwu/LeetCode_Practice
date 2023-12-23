class Solution:
    def twoSum(self, nums: List[int], target: int, count=0) -> List[int]:
        # 檢查第一個位置的數字跟後面的有沒有辦法組成target
        for i in range(count+1,len(nums)):
            # 如果可以就回傳
            if nums[count]+nums[i]==target:
                ans=[count,i]
                return ans
        # 否則將位置調至下一個，並使用遞迴重複上述動作
        count+=1
        return self.twoSum(nums,target,count)
