"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]

the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.string picture

    A non-empty array of non-empty equal-length strings.

    Guaranteed constraints:
    1 ≤ picture.length ≤ 100,
    1 ≤ picture[i].length ≤ 100.

    [output] array.string

    The same matrix of characters, framed with a border of asterisks of width 1.

"""

from numpy import *

def addBorder(picture):
    rows = len(picture) #height
    columns = len(picture[0]) # width

    output = []
    border = ""

    for i in range(0, columns+2):
        border += "*"
    output.append(border)

    for i in range(0, rows):
        output.append("*"+picture[i]+"*")

    output.append(border)

    return output

picture = ["abc",
           "ded"]

print(addBorder(picture))