'''
Goal : Fill the knapsack such that the value is maximum and the total weight 
is almost W items can be broken down to maximise the knapsack value.
Input:
    wt[]  :10,20,30
    val[] :60,100,120
    W = 50 i.e., knapsack capacity
Output:
    240
    
Greedy Approach:
1) Calculate the ratio (value/weight) for each item.
2) Sort the items based on the ratio.
3) Take the next item with highest ratio and add them until we can't 
   add the next item as whole.
4) At the end the next 
'''
wt = list(map(int,input().split()))
value = list(map(int,input().split()))
w = int(input())
l =[]
for i in range(len(wt)):
    l.append([i+1,wt[i],value[i],value[i]/wt[i]])
l.sort(key = lambda x:x[3],reverse = True)

ansval = 0
for i in range(len(wt)):
    if w>l[i][1]:
        ansval+= l[i][2]
        w-= l[i][1]
    else:
        ansval+= l[i][2] * (w/l[i][1])
        break
print(ansval)
