class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def diffWaysToCompute1(expression):
            ways = []
            op_funcs = {
                "+": (lambda x, y: x + y),
                "-": (lambda x, y: x - y),
                "*": (lambda x, y: x * y),
            }
            for i, c in enumerate(expression):
                if c not in op_funcs:
                    continue
                left = diffWaysToCompute1(expression[:i])
                right = diffWaysToCompute1(expression[i + 1 :])
                ways += [op_funcs[c](l, r) for l in left for r in right]
            return [int(expression)] if len(ways) == 0 else ways
        return diffWaysToCompute1(expression)