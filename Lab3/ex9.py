list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]

print(list1)
print(list2)

def sum_lists (list1, list2):
    if len(list1) == len(list2):
        return [a + b for a, b in zip(list1, list2)]
    
    else:
        print("Listele n-au aceasi lungime!")

result = sum_lists(list1, list2)
print(result)
