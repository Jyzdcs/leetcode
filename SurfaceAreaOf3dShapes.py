class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        totalVisibleFace = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    totalVisibleFace += 2

                caseValue = grid[i][j]

                front = caseValue if i == 0 else max(0, caseValue - grid[i-1][j])
                totalVisibleFace += front

                back = caseValue if i == (n - 1) else max(0, caseValue - grid[i+1][j])
                totalVisibleFace += back

                left = caseValue if j == 0 else max(0, caseValue - grid[i][j-1])
                totalVisibleFace += left

                right = caseValue if j == (n - 1) else max(0, caseValue - grid[i][j+1])
                totalVisibleFace += right

        return totalVisibleFace



solution = Solution()
grid = [[2,2,2],[2,1,2],[2,2,2]]

print(solution.surfaceArea(grid))