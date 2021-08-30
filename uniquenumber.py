# Prints all triplets in  
# arr[] with 0 sum 
def findTriplets(arr, n): 
  
    found = True
    for i in range(0, n-2): 
      
        for j in range(i+1, n-1): 
          
            for k in range(j+1, n): 
              
                if (arr[i] + arr[j] + arr[k] == 0): 
                    print(arr[i], arr[j], arr[k]) 
                    found = True
      
              
    # If no triplet with 0 sum  
    # found in array 
    if (found == False): 
        print(" not exist ") 
  
# Driver code 
arr = [1,2,4,-3,5,6,7,8,0,0,0]

n = len(arr) 
findTriplets(arr, n)
