
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.folow = dict()
        self.ref = dict()
        self.posts = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        try:
            self.posts[userId].append( (-self.time, (userId, tweetId) )   )
        except:
            self.posts[userId] =  [ (-self.time, (userId, tweetId) ) ]
            
        if self.ref.get(userId) == None:
            self.ref[userId] = [userId]
            self.folow[(userId, userId)] = True
   
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if self.ref.get(userId) == None:
            self.ref[userId] = [userId]
            self.folow[(userId, userId)] = True

        sol = []
        temp = self.ref.get(userId).copy()
        feed = []
        for people in temp:
            for post in self.posts.get(people, []):
                heapq.heappush(feed, post)

        while feed!=[] and len(sol) < 10:
            post = heapq.heappop(feed)
            
            if  self.folow[ (userId,  post[1][0]) ] or post[1][0] == userId:
                sol.append(post[1][1])
          
        return sol
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or self.folow.get ( (followerId, followeeId), False):
            return

        try:
            self.ref[followerId] .append(followeeId)
        except:
            self.ref[followerId]  = [followerId, followeeId] 
            self.folow[(followerId, followerId)] = True

        self.folow[(followerId, followeeId)] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
            
        if self.ref.get(followerId) == None:
            return

        try:
            self.ref[followerId] .remove(followeeId)
        except:
            pass

        
        self.folow[(followerId, followeeId)] = False
