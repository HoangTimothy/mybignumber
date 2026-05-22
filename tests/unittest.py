import io
import logging
import unittest

from src.add2num import MyBigNumber


class TestMyBigNumber(unittest.TestCase):
    def setUp(self):
        self.log_stream = io.StringIO()
        handler = logging.StreamHandler(self.log_stream)
        handler.setLevel(logging.INFO)

        self.logger = logging.getLogger(f"test.add2num.{id(self)}")
        self.logger.handlers.clear()
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.logger.addHandler(handler)

        self.add2num = MyBigNumber(logger=self.logger)

    def tearDown(self):
        self.logger.handlers.clear()

    def test_sum_simple(self):
        self.assertEqual(self.add2num.sum("1234", "897"), "2131")

    def test_sum_long_first_short_second(self):
        self.assertEqual(self.add2num.sum("4567", "123"), "4690")


    def test_sum_carry_at_most_significant_digit(self):
        self.assertEqual(self.add2num.sum("500", "500"), "1000")

    def test_sum_with_one_zero(self):
        self.assertEqual(self.add2num.sum("0", "987654321"), "987654321")
        self.assertEqual(self.add2num.sum("987654321", "0"), "987654321")

    def test_sum_extremely_large_numbers(self):
        num1 = "9" * 50  # 50 số 9
        num2 = "1"
        expected = "1" + "0" * 50
        self.assertEqual(self.add2num.sum(num1, num2), expected)

    def test_sum_with_carry_chain(self):
        self.assertEqual(self.add2num.sum("999", "1"), "1000")
    
    def test_sum_different_lengths(self):
        self.assertEqual(self.add2num.sum("123", "4567"), "4690")

    def test_sum_with_zero(self):
        self.assertEqual(self.add2num.sum("0", "0"), "0")

    def test_sum_with_leading_zeros(self):
        self.assertEqual(self.add2num.sum("00123", "00077"), "200")

    def test_logs_each_step(self):
        result = self.add2num.sum("1234", "897")
        self.assertEqual(result, "2131")

        logs = self.log_stream.getvalue()
        self.assertIn("Step 1: 4 + 7 + carry(0) = 11 -> write 1, carry=1", logs)
        self.assertIn("Step 2: 3 + 9 + carry(1) = 13 -> write 3, carry=1", logs)
        self.assertIn("Final result: 2131", logs)

if __name__ == "__main__":
    unittest.main()