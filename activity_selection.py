'''
Given n activities with their start and finish times . 
Select the maximum number of activities that can be performed 
by a single person ,assuming that a person can work on a single 
activity at a time.

input: 
  start[] : 0,3,1,5,5,8 
  end[]   : 6,4,2,9,7,9

output: 3 2 5 6
       i.e., index of events done

Greedy Approach:
1) Sort the activities according to their finishing time.
2) Select the first activity from the sorted array and print it.
3) Do following for remaining activities in the sorted array.
   - If the start time of this activity is greater than or equal to the
   finish time of previously selected activity then select this 
   activity and print it.
'''
start = list(map(int,input().split()))
end = list(map(int,input().split()))
l=[]
for i in range(len(start)):
    l.append([i+1,start[i],end[i]])
l.sort(key = lambda x:x[2])
prev = l[0][2]
print(l[0][0],end= " ")
for i in range(1,len(start)):
    if prev<l[i][1]:
        print(l[i][0],end=" ")
        prev = l[i][2]

