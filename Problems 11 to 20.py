import math
# Problem 11 (5%) - Largest Product in a Grid - https://projecteuler.net/problem=11

array = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
]

# def largest_prod(array):
#     products = []
#     for y in array:
#         for x in y:
#             products += [array[0][0] + array[0][1] + array[0][2] + array[0][3]]
#             products += [array[0][0] + array[1][0] + array[2][0] + array[3][0]]
#             products += [array[0][0] + array[1][1] + array[2][2] + array[3][3]]
#             if x
#     return max(products)





# Problem 12 (5%) - Highly divisible triangular number - https://projecteuler.net/problem=12
def euler_12():
    total = 1
    index = 1
    while True:
        print(total)
        if divisors(total) > 500:
            return total
        index = index + 1
        total += index

# figured out how to use a log(O) time complexity!! (abuot 272% faster than my original solution)
def divisors(x):
    num, total, call_count = 2, 2, 1
    index = x - 1
    while index > num + 1:
        call_count += 1
        if math.sqrt(x) == num:
            total += 1
            index = math.sqrt(x)
        if x % num == 0 and num != math.sqrt(x):
            total += 2
            index = x // num
        num += 1
    return total
# 76576500





# Problem 13


# Problem 14 (5%) - Longest Collatz sequence - https://projecteuler.net/problem=14
def longest_collatz_seq():
    index = 4
    longest = [3, 8]
    while index < 1000000:
        print(index)
        collatz = collatz_seq(index)
        if collatz > longest[1]:
            longest[0] = index
            longest[1] = collatz
            index += 1
        else: index += 1
    return longest

def collatz_seq(x):
    total = 1
    while x != 1:
        total += 1
        if x % 2 == 0:
            x = x/2
        else: x = (3 * x) + 1
    return total
# 837799, with 525





# Problem 15 (5%) - Lattice paths - https://projecteuler.net/problem=15
# classic recursion problem I did twice in Berkeley's CS61a
# implemented memoization to make the function extremely fast
paths = {}
def lattice_paths(x, y):
    if x == 0 or y == 0:
        return 1
    if (x, y) in paths:
        return paths[(x, y)]
    else:
        paths[(x, y)] = lattice_paths(x-1, y) + lattice_paths(x, y-1)
        return lattice_paths(x-1, y) + lattice_paths(x, y-1)
# 137846528820







# Problem 16 (5%) - Power Digit Sum - https://projecteuler.net/problem=16
total = 0
for x in str(2 ** 1000):
    total += int(x)
