# Problem 1 - Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000.

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

print(sumMultiples(3, 5))


# Recursively:
def sumMultiplesRecursive(x, y, z):        #z is the amount of sum limit - 1
    if z == 0:
        return 0
    elif z > 0:
        if (z % x == 0) or (z % y == 0):
            return z + sumMultiplesRecursive(x, y, z - 1)
        else:
            return sumMultiplesRecursive(x, y, z - 1)

print(sumMultiplesRecursive(3, 5, 999))        #Reaches recursion limit, but does work with lower z values  


#Using a list comprehension
multiples = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(multiples)
