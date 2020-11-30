"""
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral!
You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way:
Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square
that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]

the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. 
The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

the output should be

boxBlur(image) = [[5, 4],
                  [4, 4]]

There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output.
To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5.
The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.integer image

    An image, stored as a rectangular matrix of non-negative integers.

    Guaranteed constraints:
    3 ≤ image.length ≤ 100,
    3 ≤ image[0].length ≤ 100,
    0 ≤ image[i][j] ≤ 255.

    [output] array.array.integer

    A blurred image represented as integers, obtained through the process in the description.

https://www.geeksforgeeks.org/box-blur-algorithm-with-python-implementation/

"""
def square_matrix(square):
    """
    This function will calculate the value x
    (i.e blurred pixel value) for each 3*3 blur image.
    """
    tot_sum = 0

    # Calculate sum of all teh pixels in a 3*3 matrix
    for i in range(3):
        for j in range(3):
            tot_sum += square[i][j]

    return tot_sum//9

def boxBlur(image):
    square = []
    square_row = []
    blur_row = []
    blur_img = []

    n_rows = len(image)
    n_col = len(image[0])

    rp, cp = 0, 0

    while rp <= n_rows - 3:
        while cp <= n_col - 3:
            for i in range(rp, rp + 3):
                for j in range(cp, cp + 3):
                    square_row.append(image[i][j])

                square.append(square_row)
                square_row = []

            blur_row.append(square_matrix(square))
            square = []

            cp = cp + 1

        blur_img.append(blur_row)
        blur_row = []
        rp = rp + 1
        cp = 0

    return blur_img

def boxBlur(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans

image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

print(boxBlur(image))
