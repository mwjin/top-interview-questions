class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        if s.isnumeric():
            return int(s)

        op_add_sub_idx = max(s.rfind("+"), s.rfind("-"))

        if op_add_sub_idx != -1:
            if s[op_add_sub_idx] == "+":
                return self.calculate(s[:op_add_sub_idx]) + self.calculate(
                    s[op_add_sub_idx + 1 :]
                )
            else:
                return self.calculate(s[:op_add_sub_idx]) - self.calculate(
                    s[op_add_sub_idx + 1 :]
                )

        op_mul_div_idx = max(s.rfind("*"), s.rfind("/"))
        if op_mul_div_idx != -1:
            if s[op_mul_div_idx] == "*":
                return self.calculate(s[:op_mul_div_idx]) * self.calculate(
                    s[op_mul_div_idx + 1 :]
                )
            else:
                return self.calculate(s[:op_mul_div_idx]) // self.calculate(
                    s[op_mul_div_idx + 1 :]
                )

        return 0


print(Solution().calculate("1+2*5/3+6/4*2"))
