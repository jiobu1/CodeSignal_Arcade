"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly
increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
Sequence containing only one element is also considered to be strictly increasing.

Example

    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer sequence

    Guaranteed constraints:
    2 ≤ sequence.length ≤ 105,
    -105 ≤ sequence[i] ≤ 105.

    [output] boolean

    Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

"""

# def almostIncreasingSequence(sequence):
    # if len(sequence) <= 2:
    #     return True

    # removed = []
    # for i in range(len(sequence)):
    #     if i > i + 1:
    #         removed.append(i + 1)
    #         if len(removed) <=1:
    #             return True

    # return False
    # bad code passes 11/19 tests

# def almostIncreasingSequence(sequence):
#     if len(sequence) <= 2:
#         return True

#     def find_and_replace(nums):
#         if nums[0] >= nums[1]:
#             nums.pop(0)
#             return nums
#         if nums[-2] >= nums[-1]:
#             nums.pop(-1)
#             return nums

#         for i in range(1 - len(nums) - 1):
#             if nums[i] <= nums[i - 1] or nums[i] >= nums[i + 1]:
#                 nums.pop(i)
#                 return nums

#         return nums

#     nums = find_and_replace(sequence[:]) # return copy of sequence

#     if len(nums) != len(sequence):
#         return len(find_and_replace(nums[:])) == len(nums)

#     return True
# passes 18/19 tests

# def almostIncreasingSequence(sequence):
#     dropped = False
#     last = prev = min(sequence) - 1
#     for elm in sequence:
#         if elm <= last:
#             if dropped:
#                 return False
#             else:
#                 dropped = True
#             if elm <= prev:
#                 prev = last
#             elif elm >= prev:
#                 prev = last = elm
#         else:
#             prev, last = last, elm
#     return True

# def almostIncreasingSequence(sequence):
#     count = 0
#     for i in range(len(sequence)-1):
#         if sequence[i] >= sequence[i+1]: 
#             count += 1
#         if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: 
#             count += 1
#     return count < 3


# https://stackoverflow.com/questions/43017251/solve-almostincreasingsequence-codefights/43017981
def is_increasing(lst):
        for i in range(len(list1)-1):
            if list1[i] >= list[i + 1]:
                return False
        return True

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            increasing = is_increasing([*sequence[:idx], *sequence[idx+1:]]) or is_increasing([*sequence[:idx+1], *sequence[idx+2:]])
            if not increasing:
                return False

    return True

def almostIncreasingSequence(sequence):
    c = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]: c += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: c += 1
    return c < 3

sequence = [1, 2, 3, 4, 3, 6]
print(almostIncreasingSequence(sequence))