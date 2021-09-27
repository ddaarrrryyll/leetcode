class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = set()
        for email in emails:
            local, domain  = email.split('@')
            front = local.split('+')[0].replace('.', '')
            
            # for different cases e.g. Abc and aBC should be the same local name
            l.add(front.lower() + '@' + domain.lower())
        print(l)
        return len(l)
