class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # this is so scuffed even i feel sorry for myself
        # Counter to store the frequency of words
        c = Counter(words)
        
        # sorted according to values
        sorted_c = sorted(c.items(), key = lambda item: item[1], reverse = True)
        
        count = sorted_c[0][1]
        temp = []
        out = []
        i = 0
        for item in sorted_c:
            if item[1] == count:
                temp.append(item[0])
                temp.sort()
            else:
                j = 0
                while i < k and j < len(temp):
                    out.append(temp[j])
                    i += 1
                    j += 1
                
                temp = []
                count = item[1]
                temp.append(item[0])
        j = 0
        while i < k and j < len(temp):
            out.append(temp[j])
            i += 1
            j += 1
        return out