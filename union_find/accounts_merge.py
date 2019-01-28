# Note 1: 
"""
            for email in emails[1:]: 
                # ids = email_to_ids.get(email, [])
                # email_to_ids[email] = ids.append(id)
                
                email_to_ids[email] = email_to_ids.get(email, [])
                email_to_ids[email].append(id)
"""
# Note 2: 
"""
need to use self.find(id)
not only self.father[id]
in case there are node not yet merged to same father 

    def get_id_to_email_set(self, accounts): 
        id_to_email_set = {}
        for id, account in enumerate(accounts): 
            #root_id = self.father[id]
            root_user_id = self.find(id)
            # email_set = id_to_email_set.get(root_user_id, set())
            for email in account[1:]: 
                id_to_email_set[root_user_id] = id_to_email_set.get(root_user_id, set())
                id_to_email_set[root_user_id].add(email)
                #email_set.add(email)
            #id_to_email_set[root_user_id] = email_set
        return id_to_email_set
"""
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.initialize(len(accounts))
        email_to_ids = self.get_email_to_ids(accounts)
        
        # union 
        for email, ids in email_to_ids.items(): 
            root_id = ids[0]
            for id in ids[1:]:
                self.union(id, root_id)
        
        id_to_email_set = self.get_id_to_email_set(accounts)
        
        merged_accounts = []
        for user_id, email_set in id_to_email_set.items():
            merged_accounts.append([accounts[user_id][0], 
                                    *sorted(email_set)])
        return merged_accounts
            
    def initialize(self, n):
        self.father = {}
        for i in range(n): 
            self.father[i] = i
    
    def get_email_to_ids(self, accounts): 
        email_to_ids = {}
        for i, account in enumerate(accounts): 
            for email in account[1:]: 
                email_to_ids[email] = email_to_ids.get(email, [])
                #print(email_to_ids[email])
                email_to_ids[email].append(i)
        return email_to_ids
    
    def union(self, id1, id2): 
        self.father[self.find(id1)] = self.find(id2)
    
    def find(self, user_id): 
        path = []
        while user_id != self.father[user_id]: 
            path.append(user_id)
            user_id = self.father[user_id]
        
        for node in path: 
            self.father[node] = user_id
        return user_id
    
    def get_id_to_email_set(self, accounts): 
        id_to_email_set = {}
        for user_id, account in enumerate(accounts): 
            root_user_id = self.find(user_id)
            email_set = id_to_email_set.get(root_user_id, set())
            for email in account[1:]: 
                email_set.add(email)
            id_to_email_set[root_user_id] = email_set
            
        return id_to_email_set
