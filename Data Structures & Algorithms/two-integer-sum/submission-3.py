class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        val1 = None
        val2 = None
        for index, value in enumerate(nums):
            map[value] =  index
        for i in range(len(nums)):
            val1 = i
            if(self.findMatch(map, nums[i], target) and map[target-nums[i]] != val1):
                val2 = map[target-nums[i]]
                break;
        return [val1, val2];
        # return []
    

    def findMatch(self, map, searchVal, target) -> bool:
        if(target - searchVal in map):
            return True
        return False
        
        