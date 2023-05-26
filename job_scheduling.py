# Jobs, Profit, Slot
profit = [15,27,10,100, 70]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [4,3,5,1,2] 
profitNJobs = list(zip(profit,jobs,deadline))
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
slot = []
for _ in range(len(jobs)+1):
    slot.append(0)

profit = 0
ans = []

for i in range(len(jobs)+1):
    ans.append('null')

for i in range(len(jobs)):
        job = profitNJobs[i]
        #check if slot is occupied
        for j in range(job[2], 0, -1):
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
        
print("Jobs scheduled buddy:",ans[1:])
print(profit)