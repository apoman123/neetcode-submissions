class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n != 0:
            is_negative = n < 0

            if is_negative:
                n = n * -1

            def calc_pow(n):
                if n == 1:
                    return x
                elif n > 1 and n % 2 == 0:
                    return calc_pow(n // 2) * calc_pow(n // 2)
                elif n > 1 and n % 2 != 0:
                    return calc_pow(n // 2) * calc_pow(n // 2) * calc_pow(1)

            return calc_pow(n) if not is_negative else 1 / calc_pow(n)
        else:
            return 1