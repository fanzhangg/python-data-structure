from stack import Stack


def dec_to_bin(num: int) -> str:
    """
    Convert integer values into binary numbers

    Algorithm: Divided By 2
    - Start with an integer greater than 0
    - Continuously divide the number by 2 and keep track of the reminder
    - the reversed string of reminders is the binary string

    i.e. The binary string of 233 is 11101001
    1 | 233
    0 | 116
    0 | 58
    1 | 29
    0 | 14
    1 | 7
    1 | 3
    1 | 1
        0
    """
    stack = Stack()
    while num != 0:
        reminder = num % 2
        stack.push(reminder)
        num = num // 2
    bin_str = ""
    while not stack.isempty():
        bin_digit = stack.pop()
        bin_str = "".join((bin_str, str(bin_digit)))
    return bin_str
