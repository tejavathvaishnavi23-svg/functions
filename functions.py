# maximum of three numbers
def max_of_two(x,y):
    if x>y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))
print(max_of_three(1,2,3))

# sum all numbers in a list
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum((8,2,3,0,7)))

#Multiply all numbers in a list
def multiply_list(numbers):
    total = 0
    for num in numbers:
        total *= num
    return total
print(multiply_list((8,2,3,0,7)))

#reverse a string
def string_reverse(vaishu):
    return vaishu[::-1]  # [::-1] is used in slicing
print(string_reverse('vaishu'))

#Factorial of a number
def factorial(n):
    if n==0:
        # if 'n' is 0, return 1 (factorial of 0 is 1)
        return 1
    else:
        return n * factorial(n-1)
n = int(input(" Input a number to compute the factorial: "))
print(factorial(n))

#check if a number falls within a given range
def test_range(n):
    if n in range(3,9):
        print(n)
    else:
        print("the number is out of range")
test_range(5) # call the test_range function with the argument 5

#Count Uppercase and Lowercase letters in string
def count_letters(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_letters("Tejavath vaishnavi")

#Return a new list with distinct elements from a list
def distinct_list(lst):
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    return new_list
print(distinct_list([1,2,3,4,5,6,7,8,9]))

