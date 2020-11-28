"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

    For inputString = "172.16.254.1", the output should be
    isIPv4Address(inputString) = true;

    For inputString = "172.316.254.1", the output should be
    isIPv4Address(inputString) = false.

    316 is not in range [0, 255].

    For inputString = ".254.255.0", the output should be
    isIPv4Address(inputString) = false.

    There is no first number.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A string consisting of digits, full stops and lowercase English letters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 30.

    [output] boolean

    true if inputString satisfies the IPv4 address naming rules, false otherwise.

"""

def isIPv4Address(inputString):
    inputString = inputString.lower()

    if inputString.islower():
        return False

    l = inputString.split(".")

    if len(l) != 4:
        return False

    li = []
    for i in l:
        if (i != "") and (i != "01") and (i != "00"):
            li.append(int(i))

    new = []
    for i in li:
        if (0 <= i <= 255):
            new.append(i)

    if len(new)!= 4:
        return False

    return True

def isIPv4Address(s):
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

# inputString = "172.316.254.1"
# inputString = "172.16.254.1"
# inputString = ".254.255.0"
inputString = "1.1.1.1a"
print(isIPv4Address(inputString))