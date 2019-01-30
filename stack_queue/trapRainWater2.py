import heapq

class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap: return 0
        
        self.initialize(heightMap)
        
        water = 0
        while self.boarders: 
            height, x, y = heapq.heappop(self.boarders)
            for x_, y_ in self.adjcent(x, y): 
                water += max(0, height - heightMap[x_][y_])
                self.add(x_, y_, max(height, heightMap[x_][y_]))
        
        return water 
    
    def initialize(self, heights): 
        self.n = len(heights)
        self.m = len(heights[0])
        self.visited = set()
        self.boarders = []
        
        for index in range(self.n):
            self.add(index, 0, heights[index][0])
            self.add(index, self.m-1, heights[index][self.m - 1])
            
        for index in range(self.m): 
            self.add(0, index, heights[0][index])
            self.add(self.n - 1, index, heights[self.n - 1][index])
            
    def add(self, x, y, height): 
        # add x, y, height to boarders
        heapq.heappush(self.boarders, (height, x, y))
        self.visited.add((x, y))
    
    def adjcent(self, x, y): 
        adj = []
        for delta_x, delta_y in [(0, 1) , (0, -1), (1, 0), (-1, 0)]:
            x_ = x + delta_x
            y_ = y + delta_y
            if 0 <= x_ < self.n and 0 <= y_ < self.m and (x_, y_) not in self.visited: 
                adj.append((x_, y_))
        
        return adj
