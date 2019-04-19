#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

g_list = [10,15,3,7]
num = 17

def brute():
    for i in range(len(g_list)-1):
        for j in range((i+1),len(g_list)):
            if (g_list[i]+g_list[j]) == num:
                return True
    return False

def bonus():
    hashTable = {}
    for i in range(len(g_list)):
        numMinusElement = num - g_list[i]
        if numMinusElement in hashTable:
            return True
        hashTable[g_list[i]]=g_list[i]
    return False

print(brute())
print(bonus())