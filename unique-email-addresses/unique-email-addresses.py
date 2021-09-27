class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = []
        for email in emails:
            l.append(self.helper(email))
        print(l)
        return len(set(l))
    
    # get unique value of (local name, domain name)
    def helper(self, email):
        local = 0
        domain = 0
        i = 0
        
        # traverse local name part
        while email[i] != '@' and email[i] != '+':
            if email[i] != '.':
                local += ord(email[i])
            i+=1
            
        # traverse until @
        while email[i] != '@':
            i+=1
            
        # traverse domain
        while i < len(email)-1:
            domain += ord(email[i])
            i+=1
        
        return local, domain