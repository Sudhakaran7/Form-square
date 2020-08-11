class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        import copy
        def isCoverd(grid):
            count = 0
            for i in grid:
                for j in i:count += int(j)
            return count == (len(grid) * len(grid[0]))
        def getNextOne(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '0':
                        return i,j
            return None

        def encode(grid):
            grid_str = ''
            for i in grid:
                for j in i:
                    grid_str += j
                grid_str += '#'
            return grid_str[:-1]

        def decode(grid_str):
            grid_split = grid_str.split('#')
            grid = []
            for line in grid_split:
                grid.append(list(line))
            return grid

        self.res = 0
        def greed(n,m):
            self.res += 1
            if n == m:
                return
            elif n < m:
                greed(n,m-n)
            else:greed(n-m,m)

        greed(n,m)

        dic = {}

        grid = [['0'] * m for _ in range(n)]
        MAX_SIDE_LENGTH = min(n,m)
        queue = []
        for i in range(1,MAX_SIDE_LENGTH+1):
            new_grid = copy.deepcopy(grid)
            for x in range(i):
                for y in range(i):
                    new_grid[x][y] = '1'
            queue.append((encode(new_grid),1))
            dic[encode(new_grid)] = 1




        while len(queue) > 0:
            mat_str,path = queue.pop(0)
            mat = decode(mat_str)
            if isCoverd(mat):
                self.res = min(self.res,path)
                continue
            elif path >= self.res:
                continue
            i,j = getNextOne(mat)
            for k in range(1,MAX_SIDE_LENGTH+1):
                if i + k > len(mat) or j + k > len(mat[i]):
                    break
                flag = True
                #new_mat = copy.deepcopy(mat)
                new_mat = decode(mat_str)
                for x in range(k):
                    if flag == False:
                        break
                    for y in range(k):
                        if new_mat[i+x][j+y] == '1':
                            flag = False
                            break
                        new_mat[i+x][j+y] = '1'
                new_mat_str = encode(new_mat)
                if flag and (new_mat_str not in dic or dic[new_mat_str] > path + 1):
                    queue.append((encode(new_mat),path+1))
                    dic[new_mat_str] = path + 1
        return self.res
val=Solution()
n,m=map(int,input().split())
print(val.tilingRectangle(n,m))
