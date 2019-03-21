from unittest import TestCase

from infix_expression import *


class TestInfixToPostfix(TestCase):
    def test_plus_minus(self):
        self.assertEqual("A B +", infix_to_postfix("A + B"))
        self.assertEqual("A B + C +", infix_to_postfix("A + B + C"))
        self.assertEqual("A B + C + D +", infix_to_postfix("A + B + C + D"))
        self.assertEqual("A B -", infix_to_postfix("A - B"))
        self.assertEqual("A B - C +", infix_to_postfix("A - B + C"))
        self.assertEqual("A B - C + D -", infix_to_postfix("A - B + C - D"))

    def test_times_divide(self):
        self.assertEqual("A B * C *", infix_to_postfix("A * B * C"))

    def test_operators_with_diff_precedence(self):
        self.assertEqual("A B C * +", infix_to_postfix("A + B * C"))
        self.assertEqual("A B C * + D +", infix_to_postfix("A + B * C + D"))
        self.assertEqual("A B * C D * +", infix_to_postfix("A * B + C * D"))

    def test_expression_with_parenthesis(self):
        self.assertEqual("A B + C *", infix_to_postfix("( A + B ) * C"))
        self.assertEqual("A B + C D + *", infix_to_postfix("( A + B ) * ( C + D )"))

    def test_has_higher_precedence(self):
        self.assertTrue(ge_precedence("*", "+"))
        self.assertFalse(ge_precedence("+", "*"))
        self.assertTrue(ge_precedence("+", "-"))
