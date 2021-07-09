def SelectionSort(myList):
  
  for i in range(0, len(myList)):
    min_index = i
      
    for j in range(i + 1, len(myList)):
      if myList[j] < myList[min_index]:
        min_index = j
     
    swap = myList[i]
    
    myList[i] = myList[min_index]
    myList[min_index] = swap
    
  return myList
