def find_largest_and_smallest(arr): 
 largest = arr[0] 
 smallest = arr[0] 
  
 for num in arr: 
 if num > largest: 
 largest = num 
 if num < smallest: 
 smallest = num 
  
 return largest, smallest
