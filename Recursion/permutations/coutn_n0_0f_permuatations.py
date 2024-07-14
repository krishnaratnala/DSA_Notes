from typing import List


def findMissingOperationindex(ops: List[str], missingOp: str, currentTop: int) -> int:
    def apply_operations(operations):
        stack = []
        for op in operations:
            if "PUSH" in op:
                _, x = op.split()
                stack.append(int(x))
            elif op == "POP":
                if stack:
                    stack.pop()
                else:
                    return None  # Invalid operation: trying to POP from an empty stack
        return stack

    n = len(ops)

    for i in range(n + 1):
        modified_ops = ops[:i] + [missingOp] + ops[i:]
        result_stack = apply_operations(modified_ops)
        if result_stack is not None and result_stack and result_stack[-1] == currentTop:
            return i

    return -1  # This line should never be reached given the problem's guarantee


# Test cases

# Example 1
ops = ["PUSH 1", "PUSH 2", "PUSH 3", "POP", ]
missingOp = "Pop"
currentTop = 1
print(findMissingOperationindex(ops, missingOp, currentTop))  # Expected output: 2