class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        both players play optimally, this means that Alice will always try to win
        To win this game, Alice needs to send n = 1 to Bob, this means Alice just needs to meet an N divisible by 2 
        """
        return n % 2 == 0