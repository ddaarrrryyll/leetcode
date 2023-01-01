class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        out = []
        blockOpen = False
        buf = ''
        
        for line in source:
            i = 0
            while i < len(line):
                if line[i] == '/' and i+1 < len(line) and line[i+1] == '/' and not blockOpen:
                    i = len(line)
                elif line[i] == '/' and i+1 < len(line) and line[i+1] == '*' and not blockOpen:
                    blockOpen = True
                    i += 1
                elif line[i] == '*' and i+1 < len(line) and line[i+1] == '/' and blockOpen:
                    i += 1
                    blockOpen = False
                
                elif not blockOpen:
                    buf += line[i]
                i += 1
            
            if buf and not blockOpen:
                out.append(buf)
                buf = ''
        return out