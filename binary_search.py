import random
import time

"""
Binary search and normal naive search juxtaposition
Binary search - O(log(n)), naive search - O(n)
"""

def naive_search(a_list, target):
    for i in range(len(a_list)):
        if target in a_list:
            if a_list[i] == target:
                return i
        print("Not Found")
        
        #print(target)
        

def binary_search(list, target):
    


if __name__ == "__main__":
    a_list = [-3, 4, 8, 12, 17, 21, 29, 37]
    value = 21

    naive_search(a_list, value)