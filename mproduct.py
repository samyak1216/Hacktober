# Python3 code to demonstrate Matrix Product using list comprehension + loop 
  
# getting the Product 
def prod(val) : 
    res = 1 
    for ele in val: 
        res *= ele 
    return res  
  
# initializing the list 
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]] 
  
# printing the original list 
print("The original list : " + str(test_list)) 
  
# using list comprehension + loop 
# Matrix Product 
res = prod([ele for sub in test_list for ele in sub]) 
  
# print the result 
print("The total element product in lists is : " + str(res)) 
