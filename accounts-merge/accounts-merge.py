class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d_accounts = defaultdict(lambda: [])
        out = []

        for account in accounts:
            name = account[0]
            # get email bounded to name
            emails = account[1:len(account)]
            # check dictionary
            idx_arr = self.check(emails, d_accounts[name])
               
            # merging list
            if idx_arr:
                first_idx = idx_arr[0]
                for j in range(1, len(idx_arr)):
                    d_accounts[name][first_idx].extend(d_accounts[name][idx_arr[j]]) 
                    d_accounts[name][idx_arr[j]] = None
                
                d_accounts[name][first_idx].extend(emails)
            
                
            # bind emails to account name if no records
            else:
                d_accounts[name].append(emails)
        
        # convert dict back to list
        for name, emailArr in d_accounts.items():
            # print(name, emailArr)
            for group in emailArr:
                if group:
                    subArr = [name]
                    subArr.extend(sorted(set(group)))
                    out.append(subArr)
        
        return out
            
    # should return index of arrarys with duplicates
    def check(self, emails: list, emailArr: list):
        # print(emailArr)
        # array to keep track of indices where duplicate happened
        idx_arr = []
        for email in emails:
            # emailArr is an array of another email array belonging to an owner
            for idx, subArr in enumerate(emailArr):
                if subArr and email in subArr:
                    # print("duplicate")
                    idx_arr.append(idx)
                    
        return list(set(idx_arr))
            