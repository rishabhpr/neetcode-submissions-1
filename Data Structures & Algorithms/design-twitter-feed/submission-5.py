class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followmap = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = set(self.followmap[userId])
        users.add(userId)

        for followeeId in users:
            for time, tweetId in self.tweets[followeeId]:
                heapq.heappush(heap, (-time, tweetId))
            
        res = []

        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
        
