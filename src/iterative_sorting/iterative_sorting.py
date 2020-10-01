# # TO-DO: Complete the selection_sort() function below
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         # Your code here


#         # TO-DO: swap
#         # Your code here

#     return arr

def selection_sort(a_list):
    # get the range of what we need to compare
    indexing_length = range(0, len(a_list) - 1)
    
    # for every element in the unsorted list
    for i in indexing_length:
        # set the first element in the unsorted list as default min value
        min_value = i

        # for every element to the right 
        for j in range(i + 1, len(a_list)):
            # if element is less than current min value
            if a_list[j] < a_list[min_value]:
                # replace the min value
                min_value = j
        
        # if the min value is lower than the default
        if min_value != i:
            # switch the items
            a_list[min_value], a_list[i] = a_list[i], a_list[min_value]

    return a_list



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
        # get the length that we are indexing (current list - 1)
    indexing_length = len(arr) - 1
    
    # make a variable that will help break out of the while loop
    sorted = False

    # while the list is not sorted
    while not sorted: # when sorted is False
        sorted = True
        # for loop for comparison
        for i in range(0, indexing_length):
            # if the left item is greater than right item
            if arr[i] > arr[i+1]:
                # set the sort to false
                sorted = False
                # flip the two values in the list
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr # list is actually sorted now


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
