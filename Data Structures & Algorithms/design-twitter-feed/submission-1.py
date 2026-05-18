import heapq

class Twitter:

    def __init__(self):
        self.user_tweets = {}
        self.user_network = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.time += 1
        heapq.heappush(self.user_tweets[userId], (-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        fetch_users_followees = set(self.user_network.get(userId, set()))
        fetch_users_followees.add(userId)

        tweets_stream = []
        for followee_id in fetch_users_followees:
            if followee_id in self.user_tweets:
                tweets_stream.extend(self.user_tweets.get(followee_id, []))
        heapq.heapify(tweets_stream)

        result = []
        while tweets_stream and len(result) < 10:
            neg_time, tweet_id = heapq.heappop(tweets_stream)
            result.append(tweet_id)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_network:
            self.user_network[followerId] = set()
        self.user_network[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_network:
            self.user_network[followerId].discard(followeeId)
