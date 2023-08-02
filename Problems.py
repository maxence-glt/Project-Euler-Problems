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

#print(sumMultiples(3, 5))


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
        

print(fibonacciSum(4000000))        # It works at lower levels but starts to take a long time above 50, so
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

palindrome2(999, 999)           # SUPER messy answer, but it works! It even works on lower
                                    # values like 2 digit numbers. Ill also be comming back to 
                                    # this one to imrprove it :)





# Problem 5 (5%) - Smallest Multiple - https://projecteuler.net/problem=5
# First try
def smallestMultiple(x, y):
    index1, index2, index3 = 1, list(range(x, y + 1)), 0
    while index3 == 0:
        print(index1)
        if all(index1 % i == 0 for i in index2[::-1]):
            index3 += 1
            return index1
        else:
            index1 += 1
    return index1

smallestMultiple(1, 20)        # This algorithm works but takes way too long, about 6 and a half hours from my calculations





# Second try
def smallestMultiple():
    index2 = [11, 13, 14, 16, 17, 18, 19, 20]       # Winowed down possible factors
    for num in range(2520, 999999999, 2520):        # Tried finding a way to skip over numbers in a range, found out
                                                    # about old python 2's xrange and figured out how to implement it    
        print(num)
        if all(num % i == 0 for i in index2[::-1]):
            return num
    return num