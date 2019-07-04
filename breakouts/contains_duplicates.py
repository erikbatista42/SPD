# Given a list of n numbers, determine if it contains any duplicate numbers.

def contains_duplicates(n):  # O(n) because we loop through each element in n and check if it's in the set
    my_set = set() # O(1)
    for num in n: # O(n)
        if num not in my_set: # O(1)
            my_set.add(num)  # O(1)
        else:
            return True 
    return False # no duplicates found
test = contains_duplicates([1,2,3,4,5,6,7])
print(test)