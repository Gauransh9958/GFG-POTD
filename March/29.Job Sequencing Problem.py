class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        
        jobs = [(profit[i], deadline[i]) for i in range(n)]
        
        jobs.sort(reverse=True, key=lambda x: x[0])
        
        max_deadline = max(deadline)
        
        parent = list(range(max_deadline + 1))  # parent[i] points to the next available slot before i
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            parent[x] = y
        
        total_profit = 0
        job_count = 0
        
        for job_profit, job_deadline in jobs:
            available_slot = find(job_deadline)
            
            if available_slot > 0:
                total_profit += job_profit
                job_count += 1
                union(available_slot, find(available_slot - 1))
        
        return job_count, total_profit