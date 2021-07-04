def BubbleSort(myList):
  
  for j in range(len(myList)-1, 0, -1): #this starts at length-1, and goes to 0 backwards
    
    for i in range(0, j): #starts at 0, goes to j, but DOES NOT include j
      
      if myList[i] > myList[i+1]: #if the current index is greater than the index above it, then swap. 
        swap = myList[i]
        myList[i] = myList[i+1]
        myList[i+1] = swap
    
  return myList
