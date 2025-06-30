class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        base7 = ""
        is_negative = num < 0
        num = abs(num)
        while num:
            quotient, remainder = num // 7, num % 7
            base7 = str(remainder) + base7
            num = quotient
        return "-" + base7 if is_negative else base7
