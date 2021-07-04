from random import randint

def Partition(myList, pivot):
  less = []
  equal = []
  greater = []
  
  for i in range(len(myList)): #checks each value in myList
    if myList[i] < pivot: #if value less than pivot, append to less
      less.append(myList[i])
      
    elif myList[i] == pivot: #if value equal to pivot, append to equal
      equal.append(myList[i])
    
    else:
      greater.append(myList[i]) #if value greater than pivot, append to greater
  
  return less, equal, greater
  


def QuickSort(myList):
  if len(myList) <= 1: #base case - if length is <= 1, then just return the list
    return myList
    
  pivot = myList[randint(0, len(myList)-1)] #randomly choose pivot, since it's more likely to be near the median than away
  
  less, equal, greater = Partition(myList, pivot) #use helper function on your list and the pivot, and define the return values as less, equal, greater, respectively
  
  sort_lesses = QuickSort(less) #sort the numbers less than the pivot
  sort_greater = QuickSort(greater) #sort the numbers greater than the pivot
  #no need to sort the equals, since they're just equal to the pivot
  
  return sort_lesses + equal + sort_greater #concatenate everything
