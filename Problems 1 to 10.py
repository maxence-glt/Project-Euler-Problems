# Problem 1 (5% difficulty) - Multiples of 3 and 5 - https://projecteuler.net/problem=1

# Iteratively:
def sumMultiples(x, y):        #x and y are the multiples
    total, index = 0, 0
    while index != 1000:
        if index % x == 0 or index % y == 0:
            total += index
            index += 1
        else:
            index += 1
    return total

# print(sumMultiples(3, 5))


# Recursively:
def sumMultiplesRecursive(x, y, z):        #z is the amount of sum limit - 1
    if z == 0:
        return 0
    elif z > 0:
        if (z % x == 0) or (z % y == 0):
            return z + sumMultiplesRecursive(x, y, z - 1)
        else:
            return sumMultiplesRecursive(x, y, z - 1)

#print(sumMultiplesRecursive(3, 5, 999))        #Reaches recursion limit, but does work with lower z values  


#Using a list comprehension
multiples = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)

#print(multiples)





#Problem 2 (5%) - Even Fibonacci Numbers - https://projecteuler.net/problem=2
#Fibonacci: (start with 1 and 2) 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Recursively... ish:
def fibonacciSeq(x):
    if x <= 2:
        return x
    else:
        return fibonacciSeq(x - 1) + fibonacciSeq(x - 2)


def fibonacciSum(x):
    index = 1
    sum = 0
    number = fibonacciSeq(index)
    while number < x:
        if (number % 2 == 0):
            sum += number
            index += 1
            number = fibonacciSeq(index)
        elif (number % 2 != 0):
            index += 1
            number = fibonacciSeq(index)
        elif number >= x:
            return sum
        

# print(fibonacciSum(4000000))        # It works at lower levels but starts to take a long time above 50, so
                                    # technically its a solution just not an optimal one.

# I will come back to this one!





# Problem 3 (5%) - Largest Prime Factor - https://projecteuler.net/problem=3

# Iteratively + list
def primeFactors(x):
    index = 2
    primes = []
    while index <= x:
        if x % index == 0:
            primes.append(index)
            x = x / index
        else:
            index += 1
    return primes       # This returns ALL factors, the maximum should be fairly easy to decipher
                        # however I could always just add max(primes) at the end there!
# primeFactors(600851475143)





# Problem 4 (5%) - Largest Palindrome Product - https://projecteuler.net/problem=4

def palindrome2(n1, n2):
    index = n2
    num = []
    palind = palindrome(n1, n2)
    if palind != []:
        num = palindrome(n1, n2)
    else:
        while palind == []:
            index = index - 1
            palind = palindrome(n1, index)
            num = palind
    return num

def palindrome(n1, n2):
    pals = []
    while n1 > 899:
        n = n1 * n2
        x = [int(d) for d in str(n)]
        y = x[::-1]
        if y == x:
            pals.append(x)
            n1 =  n1 - 100
        else:
            n1 -= 1
    return pals

# palindrome2(999, 999)           # SUPER messy answer, but it works! It even works on lower
                                    # values like 2 digit numbers. Ill also be comming back to 
                                    # this one to imrprove it :)





# Problem 5 (5%) - Smallest Multiple - https://projecteuler.net/problem=5
# First try
def smallestMultiple(x, y):
    index1, index2, index3 = 1, list(range(x, y + 1)), 0
    while index3 == 0:
        if all(index1 % i == 0 for i in index2[::-1]):
            index3 += 1
            return index1
        else:
            index1 += 1
    return index1

# smallestMultiple(1, 20)        # This algorithm works but takes way too long, about 6 and a half hours from my calculations





# Second try
def smallestMultiple():
    index2 = [11, 13, 14, 16, 17, 18, 19, 20]       # Winowed down possible factors
    for num in range(2520, 999999999, 2520):        # Tried finding a way to skip over numbers in a range, found out
                                                    # about old python 2's xrange and figured out how to implement it    
        if all(num % i == 0 for i in index2[::-1]):
            return num
    return num





# Problem 6 (5%) - Sum Square Difference - https://projecteuler.net/problem=6
# Solved using 2 nested generators so as improve coroutines and not run into the Space complexity from previous quesitons
def smallest_multiple(x=100):
    def sum_squares(x):
        total = 0
        for _ in range(0, x + 1):
            yield total ** 2
            total += 1
    def square_sum(x):
        total = 0
        for _ in range(0, x + 1):
            yield total
            total += 1
    return sum(square_sum(x)) ** 2 - sum(sum_squares(x))





# Problem 7 (5%) - 10001st Prime - https://projecteuler.net/problem=7
list_primes = [2, 3, 5, 7, 11, 13]
def tenthousandth_andfirst(range):
    x = 14
    while len(list_primes) != range:
        prime(x)
        x+=1
    return list_primes[-1]

def prime(x):
    for y in list_primes:
        if x % y == 0: return False
    list_primes.append(x)
    print(len(list_primes))
    return True

# print(tenthousandth_andfirst(10001))




 # Problem 8 (5%) - Largest Product in a Series - https://projecteuler.net/problem=8
def greatest_product(series):
    series_list = [int(x) for x in str(series)]
    total_list = []
    i = 0
    for x in range(0, len(series_list) - 13):
        total = 1
        for y in range(x, x + 13):
            total = total * series_list[y]
        total_list.append(total)
        i += 1
    return max(total_list)





# Problem 9 (5%) - Special Pythagorean Triplet - https://projecteuler.net/problem=9
def pythag(a, b, c):
    a, b, c = a**(1/2), b**(1/2), c**(1/2)
    return a % 1 == 0 and b % 1 == 0 and c % 1 == 0
        

def special_pythag_triple():
    pythags_list = []
    total = 1
    for a in range(3, 500):
        for b in range (4, 500):
            c = a*a + b*b
            if pythag(a*a, b*b, c) and ((a + b + c**(1/2)) == 1000):
                pythags_list.append([a, b, c**(1/2)])
    for x in pythags_list:
        for y in x:
            total = total * y
        return total





# Problem 10 (5%) - Summation of Primes - https://projecteuler.net/problem=10
list_primes2 = [2, 3, 5, 7]
def sum_primes2(total):
    sum = 17
    for x in range(10, total + 1):
        if is_prime(x):
            sum += x
    return sum

def is_prime(x):
    for y in list_primes2:
        if x % y == 0: return False
    print(x)
    list_primes2.append(x)
    return True

# print(sum_primes(2000000))
