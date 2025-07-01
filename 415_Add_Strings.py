class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        added_str = ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        len1, len2 = len(num1), len(num2)
        if len1 <= len2:
            num1, num2 = num2, num1
            len1, len2 = len2, len1
        add_bit = 0
        for i in range(len1):
            cur_sum = int(num1[i]) + (int(num2[i]) if i < len2 else 0) + add_bit
            added_str += str(cur_sum % 10)
            add_bit = int(cur_sum >= 10)
        if add_bit:
            added_str += "1"
        return added_str[::-1]