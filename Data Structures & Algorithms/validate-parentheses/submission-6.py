class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mappings = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        bracket_stack = []

        for c in s:
            if c in bracket_mappings.keys():
                bracket_stack.append(c)
            elif c in bracket_mappings.values():
                if len(bracket_stack) < 1:
                    return False
                if bracket_mappings[bracket_stack.pop()] != c:
                    return False
            else:
                return False
        
        if len(bracket_stack) > 0:
            return False
        return True