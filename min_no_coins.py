'''
Given a value V, we want to make change for V Rs. We have infinite supply of
each of the denomination in Indian currency.
i.e., we have infinite supply of {1,2,5,10,20,50,100,500,1000} valued coins/notes
what is the minimum number of coins and/or notes needed to make the change 
V Rs?

Input : Value = 70
Output:  2 
    Explanation: One rs 50 and rs 20.
    
Solution:
    Start from largest possible denomination and keep adding denominations 
    while remaining value is greater than 0.

Greedy Approach:
    1) Initialize result as empty.
    2) Find the lasrgest denomination that is smaller than V.
    3) Add denomination to the result.Subtract value of found denomination 
       from V.
    4) If V becomes 0, then print result.
       Else repeat steps 2 and 3 for new value of V.
'''

list_ruppees = [2000,500,100,50,20,10,5,2,1]
value = int(input())
min_coins = 0
for i in range(len(list_ruppees)):
    if value ==0:
        break
    elif value>=list_ruppees[i]:
        no_each_coins = (value//list_ruppees[i])
        min_coins+= no_each_coins
        value-= no_each_coins*list_ruppees[i]
        
print(min_coins)
    
