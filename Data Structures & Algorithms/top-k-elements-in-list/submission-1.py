class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq = {}
        result = []
        def getItem(item):
            return item[1]

        for num in nums:
            numsFreq[num] = numsFreq.get(num, 0) + 1;
        
        numFreq = dict(sorted(numsFreq.items(), key=getItem, reverse=True))
        result = list(numFreq.keys())
        return result[:k]
        
        

        
            