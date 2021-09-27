class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = set()
        for email in emails:
            local, domain  = email.split('@')
            front = local.split('+')[0].replace('.', '')
            l.add(front + '@' + domain)
        print(l)
        return len(l)