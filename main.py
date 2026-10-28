""" A Python program that adds all values in a list using recursion by adding the head to the sum of the tail until the list becomes
empty."""

l = [2,6,8,10,12,5,7]

def listSum(list):
    if list == []:
        return 0
    return list[0] + listSum(list[1:])

print(listSum(l))