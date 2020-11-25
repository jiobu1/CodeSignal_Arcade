"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer inputArray

    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 105,
    -105 ≤ inputArray[i] ≤ 105.

    [output] integer

    The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
    It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.
"""

def arrayChange(inputArray):
    sum1 = 0
    q = inputArray[0]
    for i in inputArray[1:]:
        if i <= q:
            sum1 += q - i + 1
            q = q + 1
        else:
            q = i
    return sum1

inputArray = [1, 1, 1]
arrayChange(inputArray)