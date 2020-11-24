"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.string inputArray

    A non-empty array.

    Guaranteed constraints:
    1 ≤ inputArray.length ≤ 10,
    1 ≤ inputArray[i].length ≤ 10.

    [output] array.string

    Array of the longest strings, stored in the same order as in the inputArray.

"""

# def allLongestStrings(inputArray):
#     d = {} # cannot have duplicate keys in dictionaries
#     for i in (inputArray):
#         d[i] = len(i)


#     return [key  for (key, value) in d.items() if value == max(d.values())]

def allLongestStrings(inputArray):
    inputArray.sort(key = len, reverse = True)

    longest = len(inputArray[0])
    arr = []

    for i in inputArray:
        if len(i) == longest:
            arr.append(i)
    return arr

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))