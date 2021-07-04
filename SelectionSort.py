def SelectionSort(myList): #selection sort with two lists
  newList = [] #this is the list that function will return
  
  while len(myList) > 0:
    smallest = myList[0] #set smallest equal to the first number
    
    for i in range(0, len(myList)): #check every value and replace smallest with the value if it is smaller than the current
      if myList[i] < smallest:
        smallest = myList[i]
        
    newList.append(smallest) #add smallest to the new list
    myList.remove(smallest) #remove it from the original list
    
  return newList
