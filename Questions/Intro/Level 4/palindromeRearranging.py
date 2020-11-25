"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 50.

    [output] boolean

    true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.

"""


def palindromeRearranging(inputString):
    inputString = list(inputString)

    dic = {}

    for i in inputString:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    keys = []
    for (key, value) in dic.items():
        if value % 2 == 1:
            keys.append(key)

            if len(keys) > 1:
                return False

    return True




inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
print(palindromeRearranging(inputString))