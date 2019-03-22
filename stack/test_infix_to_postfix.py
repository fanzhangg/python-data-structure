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


class TestCalc(TestCase):
    def test_valid_case(self):
        self.assertEqual(calc(1, "+", 2), 3)
        self.assertEqual(calc(1, "*", 2), 2)
        self.assertEqual(calc(1, "-", 2), -1)
        self.assertEqual(calc(1, "/", 2), 0.5)

    def test_invalid_operator(self):
        with self.assertRaises(SyntaxError):
            calc(1, "$", 2)


class TestEvalPostfix(TestCase):
    def test_valid_case(self):
        self.assertEqual(1 + 2, eval_postfix("1 2 +"))
        self.assertEqual(1 + 2 * 3, eval_postfix("1 2 3 * +"))
        self.assertEqual((1 + 2) * 3, eval_postfix("1 2 + 3 *"))

    def test_invalid_operand(self):
        with self.assertRaises(SyntaxError):
            eval_postfix("a b +")


class TestFormatInfix(TestCase):
    def test_valid_case(self):
        self.assertEqual("1 + 2 * 3", format_infix("1+2*3"))
        self.assertEqual("( 1 + 2 ) * 3", format_infix("( 1+2)*3  "))

    def test_invalid_char(self):
        with self.assertRaises(SyntaxError):
            format_infix("1a * b + c")
