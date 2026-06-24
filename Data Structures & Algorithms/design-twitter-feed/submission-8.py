class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followmap = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        res = []
        heap = []

        users = set(self.followmap[userId])
        users.add(userId)

        for followeeId in users:
            tweets = self.tweets[followeeId]

            index = len(tweets)-1

            if index >= 0:
                time, tweetId = tweets[index]
                heapq.heappush(heap, (-time, tweetId, followeeId, index-1))

        while heap and len(res) <10:
            negTime, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >=0 :
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, (-time, tweetId, followeeId, index-1))
        
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
        
