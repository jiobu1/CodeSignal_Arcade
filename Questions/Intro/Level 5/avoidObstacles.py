"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer inputArray

    Non-empty array of positive integers.

    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 1000,
    1 ≤ inputArray[i] ≤ 1000.

    [output] integer

    The desired length.

"""


def avoidObstacles(inputArray):
    sequence_table = {key1:[key1*key2 for key2 in range(1, 1000)] for key1 in range(1, 10)}

    inputArray = sorted(inputArray)

    options = []
    for k, v in sequence_table.items():
        check =  any(item in v for item in inputArray)
        if check == False:
            options.append(k)

    return options[0]

# inputArray =  [5, 3, 6, 7, 9] # 4
# inputArray =  [2, 3] # 4
# inputArray =  [1, 4, 10, 6, 2] # 7
inputArray =  [1000, 999] # 6
# inputArray =  [19, 32, 11, 23] # 3
# inputArray =  [5, 8, 9, 13, 14] # 6

print(avoidObstacles(inputArray))