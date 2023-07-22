class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        memo = [[]]*n
        memo[0] = [1]
        for i in range(1,n):
            memo[i] = [1]*(i+1)
            for j in range(len(memo[i-1])-1):
                memo[i][j+1] = memo[i-1][j] + memo[i-1][j+1]
        return memo
 