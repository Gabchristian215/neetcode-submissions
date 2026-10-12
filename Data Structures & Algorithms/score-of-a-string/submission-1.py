class Solution:
    def scoreOfString(self, s: str) -> int:

        total = 0

        for i in range(len(s) - 1):
            current_val = ord(s[i])
            next_val = ord(s[i + 1])
            new_val = abs(next_val - current_val)
            total += new_val
        return total
        