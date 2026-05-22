import logging
from typing import Optional

class MyBigNumber:
    """Simple big-number helper that adds two non-negative integer strings
    Implements the elementary-school addition algorithm by scanning both
    strings from right to left, adding digits and carrying as needed.

    Method:
    - `sum(stn1, stn2)` returns the sum as a string.
    - Logs each step of the digit-by-digit addition at INFO level.

    Assumptions: inputs contain only characters '0'..'9' and are non-empty.
    """

    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)

    def sum(self, stn1: str, stn2: str) -> str:
        """Return string representation of stn1 + stn2 using manual digit add.

        Example log output for sum("1234","897") will show each step:
        Step 1: 4 + 7 + carry(0) = 11 -> write 1, carry=1
        Step 2: 3 + 9 + carry(1) = 13 -> write 3, carry=1
        ...
        """
        # last character pointers
        i = len(stn1) - 1
        j = len(stn2) - 1
        carry = 0
        result_parts = [] 
        step = 1

        while i >= 0 or j >= 0 or carry:
            d1 = int(stn1[i]) if i >= 0 else 0
            d2 = int(stn2[j]) if j >= 0 else 0
            prev_carry = carry
            total = d1 + d2 + carry
            digit = total % 10
            carry = total // 10

            # log the operation for this step
            self.logger.info(
                "Step %d: %d + %d + carry(%d) = %d -> write %d, carry=%d",
                step,
                d1,
                d2,
                prev_carry,
                total,
                digit,
                carry,
            )

            result_parts.append(str(digit))
            step += 1
            i -= 1
            j -= 1
        # reverse the result parts and join
        result = ''.join(reversed(result_parts))
        result = result.lstrip('0') or '0'
        self.logger.info("Final result: %s", result)
        return result
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    nb = MyBigNumber()
    print(nb.sum('1234', '897'))