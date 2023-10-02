class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        a can only remove AAA, we call extensions to both sides =AAA=
        there is no way that neighbours can merge
        for a to win, number of AAA should be more than BBB
        AAAAAABBBB -> AAAAABBBB -> AAAAABBB -> AAAABBB -> AAAABB -> AAABB -> b loses
        count number of times A can remove and number of times B can remove, true if countA > countB
        """
        i = 0
        j = 3
        countA = 0
        countB = 0
        while j <= len(colors):
            window = colors[i:j]
            if window == "AAA":
                countA += 1
            if window == "BBB":
                countB += 1
            i += 1
            j += 1
        return countA > countB