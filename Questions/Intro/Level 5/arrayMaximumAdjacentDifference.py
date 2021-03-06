"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer inputArray

    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 10,
    -15 ≤ inputArray[i] ≤ 15.

    [output] integer

    The maximal absolute difference.

"""
def arrayMaximalAdjacentDifference(inputArray):
    largest = []
    for i in range(len(inputArray)-1):
        difference = abs(inputArray[i] - inputArray[i+1])
        largest.append(difference)

    largest.sort()
    return largest[-1]

# inputArray = [2, 4, 1, 0]
inputArray =  [10, 11, 13]
print(arrayMaximalAdjacentDifference(inputArray))