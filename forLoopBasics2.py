# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggieSize(array):
    for i in range (0,len(array)):
        if (array[i] <0):
            print(2)
            array[i] == array[i]
        else:
            array[i] = "big"
    print (array)
biggieSize([-1,3,5,-5])    

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).


def count_positives(array):
    for i in range (len(array)):
        count += count
        count = arr[i-1]
        
        
count_positives([-1,3,5,-5])




# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it

# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.

def sum_total(array):
    sum = 0 
    for x in array:
        sum = sum + x
    print(sum)

sum_total([1,2,3,4])

# Average - Create a function that takes a list and returns the average of all the values.

def average(array):
    sum = 0
    for x in array:
        sum = sum + x
    
    avg = sum/len(array)
    print avg

average([9,2,4,4])

# Length - Create a function that takes a list and returns the length of the list.

def array_length(array):
    print(len(array))
    
array_length([1,2,3,4,5])
    


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

def minimum_value(array):
    for x in array:
        if x < x+1:
            min = x
    print min
    
minimum_value([1,2,3,4,5,-1])

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.

def maximum_value(array):
    max = array[0]
    for x in array:
        if x > max:
            
            max = x
    print max
maximum_value([1,2,100,4,55])    
            

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimate_analysis(array):
        max = array[0]
    for x in array:
        if x > max:
            
            max = x
    print 'max:', + max
maximum_value([1,2,100,4,55])  

def minimum_value(array):
    for x in array:
        if x < x+1:
            min = x
    print 'min:',+ min
    
minimum_value([1,2,100,4,55])

def array_length(array):
    print 'length:', + (len(array))
    
array_length([1,2,100,4,55])

def average(array):
    sum = 0
    for x in array:
        sum = sum + x
    
    avg = sum/len(array)
    print 'avg:', + avg

average([1,2,100,4,55])

def sum_total(array):
    sum = 0 
    for x in array:
        sum = sum + x
    print 'sum:', + sum

sum_total([1,2,100,4,55])

def dictionary(array):
    print sum_total(array)
    print average(array)
    print array_length(array)
    print minimum_value(array)
    print maximum_value(array)
    
dictionary([1,2,100,4,55])
    

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

def reverse_list(array):
    for x in array:
        
        
        
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
