"""
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first
half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    isLucky(n) = true;
    For n = 239017, the output should be
    isLucky(n) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    A ticket number represented as a positive integer with an even number of digits.

    Guaranteed constraints:
    10 ≤ n < 106.

    [output] boolean

    true if n is a lucky ticket number, false otherwise.

"""
def isLucky(n):
    res = [int(x) for x in str(n)]

    if len(res) % 2 > 0:
            return False

    sum1 = 0
    sum2 = 0
    for i in range(len(res)):
        if (i < (len(res)//2)):
            sum1 += res[i]
            print(sum1)
        else:
            sum2 += res[i]
            print(sum2)

    if sum1 == sum2:
        return True

    return False

def isLucky(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))


n = 1230
print(isLucky(n))