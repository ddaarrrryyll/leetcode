class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        [2,2,3,2], [3,1,2,1]
        [(1,2), (2,1), (2,1), (3,2)]
        0 1 2 3 4 5 6 7 8 9
        1 1 x x x 1
                  2 2 x 2
                      3 3 x 3
            4 4 4 x x 4
        [(3, 4), (2, 1), (1, 3)]
        0 1 2 3 4 5 6 7 8 9
        1 1 1 1 x x x 1
                2 x x 2
                  3 3 3 x 1
        [(8, 3), (8, 1), (1, 2), (1, 2)]
        0 1 2 3 4 5 6 7 8 9
        1 1 1 x x x x x x x x 1
              2 x x x x x x x x 2
                3 3 x 1
                    4 4 x 1

        """
        # sort according to grow time?
        tups = [(growTime[i], plantTime[i]) for i in range(len(plantTime))]
        tups.sort(reverse=True)
        # print(tups)
        curr_min = 0
        days = 0
        for tup in tups:
            days += tup[1]
            curr_min = max(curr_min, days + tup[0])
        return curr_min