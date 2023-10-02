class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # as long as we travel from corner to corner it is ok if we handle direction properly
        """
        bottom left to top right -> up and right
        at top row all is [1,1,1,...]
        second row we can go up or right -> [n, n-1, n-2, ..., 1]
        at every iteration we take the sum of going up + the sum of going right
        at every cell it is the number of ways to get to the end point from there
        """
        row=[1]*n
        for i in range(m-1):
            new_row=[1]*n
            for j in range(n-2,-1,-1):
                new_row[j]=new_row[j+1]+row[j]
            # print(new_row)
            row=new_row
        return row[0]