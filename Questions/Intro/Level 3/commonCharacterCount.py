"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string s1

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ s1.length < 15.

    [input] string s2

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ s2.length < 15.

    [output] integer

"""

from collections import Counter

def commonCharacterCount(s1, s2):
    dict1 = Counter(s1)
    dict2 = Counter(s2)

    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        return 0

    commonChars = list(commonDict.elements())

    return len(commonChars)


s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1, s2))