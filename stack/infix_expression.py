"""
Infix: the operator is in between the two operands that it is working on.
Each operator has a **precedent** level.
Operators of higher precedence are used before operators of lower precedence.
- Precedence of * and / > precedence of + and -.
- If equal precedence, left-to-right ordering or associativity is used.
- Add parentheses to change the order.

Fully parenthesized:
- To guarantee no confusion with respect to the order of operations.
- Use one pair of parentheses for each operator.
- The parentheses dictate the order of operations.
- No ambiguity, no need to remember any precedence rules.

i.e.
- A + B * C + D = ((A + (B * C)) + D) # multiplication > plus
- A + B + C + D = (((A + B) + C) + D) # left to right

Prefix: All operators precede the two operands that they work on
Postfix: All operators come after the operands that they work on i.e. AB -
i.e.
|Infix                  | Prefix            | Postfix       |
| --------------------- | ----------------- | ------------- |
| A + B                 | + A B             | A B +         |
| A + B * C             | + A * B C         | A B C * +     |
| ( A + B ) * C         | * + A B C         | A B + C *     |
| A + B * C + D         | + + A * B C D     | A B C * + D + |
| ( A + B ) * ( C + D ) | * + A B + C D     | A B + C D + * |
| A * B + C * D         | + * A B * C D     | A B * C D * + |
| A + B + C + D         | + + + + + A B C D | A B + C + D + |

Problem:
Input: A string of tokens delimited by spaces. Operator tokens are *, /, +, -, (, ). Operand tokens are
single-character identifiers A, B, C,...

Algorithm:
- Fully parenthesize the expression using the order of operations.
- Move the enclosed operator to the position of either the left (prefix) or the right parenthesis (postfix).

- Create an empty stack for keeping operators. Create an empty list for output.
- Convert the input infix string to a list by using the string method.
- Scan the token list from left to right.
- If the token is an operand, append it to the end of the output list.
- If the token is a left parenthesis, push it on the stack.
- If the token is a right parenthesis, pop the stack until the corresponding left parenthesis is removed.
  Append each operator to the end of the output list.
- If the token is an operator other than parenthesis, move any operators on the stack with a higher or equal precedence and
  append them to the output list, and push it on the stack.
"""
from stack import Stack


def ge_precedence(a: str, b: str) -> bool:
    precedences = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
    return precedences[a] >= precedences[b]


def infix_to_postfix(expression: str) -> str:
    """
    Use a stack to keep the operators. The top of the stack will always be the most recently saved operator.
    When reading the new operator, compare the precedence of the added one and the recently saved one
    :param expression:
    :return:
    """
    stack = Stack()
    postfix_list = []
    tokens = expression.split()
    for token in tokens:
        if token not in "+-*/()":
            postfix_list.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while True:
                operator = stack.pop()
                if operator == "(":
                    break
                else:
                    postfix_list.append(operator)
        elif token in "+-*/":
            while True:
                if stack.isempty():
                    break
                if ge_precedence(stack.peek(), token):
                    operator = stack.pop()
                    postfix_list.append(operator)
                else:
                    break
            stack.push(token)

    while not stack.isempty():
        operator = stack.pop()
        postfix_list.append(operator)
    return " ".join(postfix_list)
