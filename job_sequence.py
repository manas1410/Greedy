'''
Given an array of jobs where every job has a deadline and associated
profit if the job is finished befor the deadline. It is also given that every
job takes single unit of time, so the minimum possible deadline for any jobs is
1. How to maximize total profit if only one job can be scheduled at a time.

Input: 
    Deadline : 2,1,2,1,3
    Profit : 100,19,27,25,15
      
Output:
   142
'''

deadlines = list(map(int,input().split()))
profits = list(map(int,input().split()))
l = []
answers = []
for i in range(len(deadlines)):
    l.append([i+1,deadlines[i],profits[i]])
    answers.append(0)
l.sort(key = lambda x:x[2],reverse = True)

for i in range(len(deadlines)):
    for j in range(l[i][1]-1,-1,-1):
        if answers[j] ==0:
            answers[j] = l[i][2]
            break
print(answers)
