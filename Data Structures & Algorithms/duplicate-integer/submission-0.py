class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.dupmap = dict()
        for i in range(len(nums)):
            if(self.dupmap.get(nums[i]) != None):
                val: int = self.dupmap[nums[i]]
                self.dupmap.update({nums[i]: self.dupmap[nums[i]]+1})
            else:
                self.dupmap.update({nums[i]: 0})
        for i in range(len(nums)):
            if self.dupmap[nums[i]] > 0:
                return True
        return False
