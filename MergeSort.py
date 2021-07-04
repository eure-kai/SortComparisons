
def Merge(ListA, ListB):
  newList = [] #this will be merging list
  
  while len(ListA) > 0 and len(ListB) > 0:
    
    if ListA[0] < ListB[0]:
      newList.append(ListA[0])
      ListA.remove(ListA[0]) #if the first element in A < the first element in B, then append it to newList, and also remove it from ListA
    
    else:
      newList.append(ListB[0])
      ListB.remove(ListB[0]) #if the first element in A is GREATER, then append the element in B and remove from ListB
   
  return newList + ListA + ListB #concatenate newList with the remaining elements in ListA and ListB (only one of them will actually have elements)



def MergeSort(myList): #implements recursion
  
  if len(myList) <= 1: #base case
    return myList #if length <= 1, then just return
    
  else:
    midpoint = len(myList) // 2 #divide the length by 2, take the floor, then set it to midpoint
    
    leftSide = MergeSort(myList[:midpoint]) #leftSide starts at 0, and goes to midpoint, but not midpoint
    rightSide = MergeSort(myList[midpoint:]) #rightSide starts at midpoint, and goes to end
    
    return Merge(leftSide, rightSide) #call merge on left and right
