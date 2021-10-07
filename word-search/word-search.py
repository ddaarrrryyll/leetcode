class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(board, i, j, word):
                    return True
                    
        return False
    
    def dfs(self, board, i, j, word) -> bool:
        if len(word) == 0:
            return True
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or word[0] != board[i][j]:
            return False
        
        # if first char is at this position
        temp = board[i][j] # need to put the char back in case search doesnt give us word back
        board[i][j] = 1
        # for row in board:
        #     print(row)
        out = self.dfs(board, i, j+1, word[1:]) or  self.dfs(board, i, j-1, word[1:]) or self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:])
        board[i][j] = temp
        return out
        