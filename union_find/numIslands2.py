DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        results = []
        island = set()
        self.size = 0
        self.father = {}
        for position in positions: 
            x, y = position[0], position[1]
            if (x, y) in island: 
                results.append(self.size)
                continue
            
            island.add((x, y))
            self.father[(x, y)] = (x, y)
            self.size += 1
            for delta_x, delta_y in DIRECTIONS: 
                x_ = x + delta_x
                y_ = y + delta_y
                if (x_, y_) in island: 
                    self.union((x_, y_), (x, y))
            
            results.append(self.size)
        
        return results
    
    def union(self, point_a, point_b): 
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        if root_a != root_b: 
            self.father[root_a] = root_b
            self.size -= 1
    
    def find(self, point): 
        path = []
        while point != self.father[point]: 
            path.append(point)
            point = self.father[point]
        
        for p in path: 
            self.father[p] = point
        return point
    
            
