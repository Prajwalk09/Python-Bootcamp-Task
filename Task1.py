"""
This piece of code is used to determine the integer when a list of digits is given.
First, we define the list which is to be considered in this task.

Next, we create a variable (container to hold values) called result (name of variable) to store the final result.

For each number in the list, multiply the result variable by 10, add the number and store the result back in result variable.

In the below example: the list is [1,7,9,2,5]
For the first number i.e., 1, the initial value of result is 0.
So when result = result*10 + number is executed, we get result = 0*10 + 1 = 1

For the second number i.e., 2, the current value of result is 1 (from previous number)
So when result = result * 10 + number is executed, we get result = 1*10 + 2 = 12

The same logic continues till the last number in the list, and we will have our final answer stored in the result variable.

The important operation to be noted here is for each number in the list, multiply the current value of result with 10
and add that number to result.
"""
numbers = [1, 7, 9, 2, 5]

result = 0

# Going through (iterating) each number in the numbers list.
for number in numbers:
    result = result * 10 + number

# Displaying the final result
print(result)
