class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        out = []
        for firstSub in firstList:
            for secondSub in secondList:
                if min(secondSub) > max(firstSub):
                    break
                if min(firstSub) > max(secondSub):
                    continue
                
                # get bigger of the smallest element
                small = max(min(firstSub), min(secondSub))
                # get smallest of the biggest element
                big = min(max(firstSub), max(secondSub))
                
                out.append([small, big])
                # print(out)
                
        return out;