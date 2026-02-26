class Solution:
    dirs = []
    m = 0
    n = 0
    prevColor = 0
    image = []
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.m = len(image)
        self.n = len(image[0])
        self.prevColor = image[sr][sc]
        self.image = image
        if image[sr][sc] == color:
            return image
        
        self.dfs(sr, sc, color)

        return self.image
    
    def dfs(self, sr: int, sc: int, color: int):
        # print(self.image[sr][sc] )
        #base
        if(sr < 0 or sc < 0  or sr >= self.m or sc >= self.n or self.image[sr][sc] != self.prevColor):
            return 
        
        self.image[sr][sc] = color
        print(self.image[sr][sc] )

        for d in self.dirs:
            nr = d[0] + sr
            nc = d[1] + sc

            self.dfs(nr, nc, color)

# // DFS
# // Time Complexity: O(N)
# // Space Complexity: O(N)