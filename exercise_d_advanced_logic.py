# For the following list of numbers:

from cmath import nan


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
max_number = max(numbers)
min_number = min(numbers)
print(max_number - min_number)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
# I used help from this link: https://stackoverflow.com/questions/25215494/how-to-check-if-previous-element-is-similar-to-next-elemnt-in-python

for index, number in enumerate(numbers):
    # print(index, number, numbers[index - 1])
    if number == 2:
        if number == numbers[index - 1] or number == numbers[index + 1]:        
            print(True)
            break

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







