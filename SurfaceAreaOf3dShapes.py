class Solution(object):
	def surfaceArea(self, grid):
		n = len(grid)
		totalFaceVisible = 0

		for i in range(n):
			for j in range(n):
				if j > 0:
					totalFaceVisible += 2
				
				height = grid[i][j]
				
				front = height if i == 0 else max(0, height - grid[i - 1][j])
				totalFaceVisible += front

				back = height if i == (n - 1) else max(0, height - grid[i + 1][j])
				totalFaceVisible += back

				left = height if j == 0 else max(0, height - grid[i][j - 1])
				totalFaceVisible += left

				right = height if j == (n - 1) else max(0, height - grid[i][j + 1])
				totalFaceVisible += right
		return totalFaceVisible


solution = Solution()
grid = [[2,2,2],[2,1,2],[2,2,2]]

print(solution.surfaceArea(grid))