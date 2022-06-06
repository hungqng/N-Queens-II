# 52. N-Queens II

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()
        res = 0
        
        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        backtrack(0)
        return res

        # Solution 2
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return len([ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result])