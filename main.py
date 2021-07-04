from random import randint
from copy import deepcopy
import time


from Selection_Sort import SelectionSort
from Insertion_Sort import InsertionSort
from Bubble_Sort import BubbleSort  
from Merge_Sort import Merge
from Merge_Sort import MergeSort
from Quick_Sort import Partition 
from Quick_Sort import QuickSort 

 
  
def make_a_copy(myList):
  result = deepcopy(myList) #uses deepcopy to make a copy
  return result
  

functions = [SelectionSort, InsertionSort, BubbleSort, MergeSort, QuickSort] #this is a list of functions 


size100 = [randint(1,10000) for i in range(100)] #100 elements, random
size1000 = [randint(1,100000) for i in range(1000)] #1000 elements, random
size10000 = [randint(1,100000) for i in range(10000)] #10000 elements, random
randoms = [size100, size1000, size10000] #makes a list of these 3 lists


size100_sorted = [i for i in range(1, 101)] #100 elements, sorted
size1000_sorted = [i for i in range(1, 1001)] #1000 elements, sorted
size10000_sorted = [i for i in range(1, 10001)] #10000 elements, sorted

sorts = [size100_sorted, size1000_sorted, size10000_sorted] #a list of these 3 lists


size100_backwards = [i for i in range(100, 0, -1)] #100 elements, backwards
size1000_backwards = [i for i in range(1000, 0, -1)] #1000 elements, backwards
size10000_backwards = [i for i in range(10000, 0, -1)] #10000 elements, backwards

backwards = [size100_backwards, size1000_backwards, size10000_backwards] #list_of_lists
  
  

def implement(list_of_lists, list_of_functions): #takes in a list of lists, and a list of functions
  
  for List in list_of_lists: #for each list in the list of lists
    time.sleep(1)
    print(f"\nWith {len(List)} items:") #type out how many elements there are
    
    for function in list_of_functions: #for each function in the list of functions
      time.sleep(0.5)
      copy = make_a_copy(List) #make a copy of the list
      name = function.__name__ #this is a way to get the function's name
      
      start = time.time()
      function(copy) #call the function on the COPY
      end = time.time()
      
      print(f"{name}: {end-start} seconds") #print out how long it took
      
 
      
print("SORTING TIMING TESTS (RANDOM):")      
implement(randoms, functions) #with randoms

time.sleep(1.5)
print("\n\nSORTING TIMING TESTS (SORTED):")
implement(sorts, functions) #with sorted

time.sleep(1.5)
print("\n\nSORTING TIMING TESTS (BACKWARDS):")
implement(backwards, functions) #with backwards  
  
  
  
