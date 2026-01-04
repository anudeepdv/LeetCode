class Leaderboard:

    def __init__(self):
        self.d = collections.defaultdict(int)


    def addScore(self, playerId: int, score: int) -> None:
        self.d[playerId]+=score
        
    def top(self, K: int) -> int:
        h  = []
        for pid,score in self.d.items():
            h.append((-score,pid))
        heapify(h)
        res = 0
        for i in range(K):
            res+=-heappop(h)[0]     
        return res   

    def reset(self, playerId: int) -> None:
        
        self.d[playerId]=0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)