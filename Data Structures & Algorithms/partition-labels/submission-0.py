class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_map = {}
        res = []

        for i, ch in enumerate(s):
            last_index_map[ch] = i
        
        cur_index = 0
        partition_max = 0
        start = 0
        while cur_index < len(s):
            # process cur char
            cur = s[cur_index]
            partition_max = max(partition_max,last_index_map[cur])

            if partition_max == cur_index:
                res.append(partition_max - start+1)
                start = cur_index+1
            
            cur_index +=1
        
        return res






        

# algo: 

# 1. create a map of each char in string and last index of it in 1 pass

# 2. in second pass keep a track of substring lenfth which will be 
#     max index from map of all chars seen till max. once you reach max, append ans 
#     in res list and contirnue with fresh count till you reach end 