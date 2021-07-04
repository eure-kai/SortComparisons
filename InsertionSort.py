def InsertionSort(myList):
  
  for i in range(0, len(myList)):
    current = i #this is your current index 
    
    while current != 0 and myList[current] < myList[current-1]: #current cannot equal 0
      swap = myList[current] #temporary variable for swapping
      
      myList[current] = myList[current-1]
      myList[current-1] = swap
      
      current -= 1 #subtract 1 from current
      
  return myList
