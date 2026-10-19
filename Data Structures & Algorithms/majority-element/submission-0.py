class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        self.candidate = None
        self.count = 0
        
        for i in range(len(nums)):
            print(f'{self.count}, {self.candidate}')
            if(nums[i] != self.candidate and self.count == 0):
                self.candidate = nums[i]
                continue
            elif(nums[i] == self.candidate):
                self.count += 1
            else:
                self.count -= 1
        return self.candidate
        
        