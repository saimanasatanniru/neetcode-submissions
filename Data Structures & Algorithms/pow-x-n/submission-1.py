class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Handle negative exponent
        # x^(-n) = (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n

        # Multiplicative identity
        result = 1.0

        while n > 0:

            # If exponent is odd, include current x in result
            if n % 2 == 1:
                result *= x

            # Square the base for the next iteration
            x *= x

            # Halve the exponent
            n //= 2

        return result