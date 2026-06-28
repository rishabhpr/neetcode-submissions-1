class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = defaultdict(int)
        max_freq = 0
        res =0

        for right in range(len(s)):
            # add s[right]
            cur = s[right]
            count[cur] +=1
            
            # update max_freq
            max_freq = max(count[cur], max_freq)

            # shrink while invalid
            while (right-left+1) - max_freq > k:
                count[s[left]] -=1
                left+=1

            # update res
            res = max(res, (right-left+1))

        return res

        