"""
Basic Implementation of Binary Search 
Author: Forrest Cai
"""


def BS(list, val):
  """
  Impementation of Binary Search.

  Parameter list: a sorted list 
  
  Parameter val: value to look for 

  Returns the index of value and None if not found 
  """
  i = 0
  j = len(list) - 1 

  while i <= j:
    mid = i + (j-i) // 2
    if list[mid] == val: #The value is in the middle 
      return mid 
    elif val < list[mid]: #The value is in the left hand side:
      j = mid - 1
    else:
      i = mid + 1

  return -1 
  


list = [1]
val = 1

print(BS(list,val))

  