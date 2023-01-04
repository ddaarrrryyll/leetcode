class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        rounds = 0
        for k, v in count.items():
            if v < 2:
                return -1
            if v % 3 == 0:
                rounds += v//3
            elif v % 3 == 1:
                # remove one from rounds to give 4, then add 2, overall add 1
                rounds += v//3 + 1
                # divide by 3 then we minus 2, add 1
            elif v % 3 == 2:
                rounds += v//3 + 1
        return rounds
                    
            