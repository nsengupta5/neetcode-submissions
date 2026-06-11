class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_str = s.replace(" ", "").lower()
        clean_str = ''.join(filter(str.isalnum, trimmed_str))

        start_ptr = 0
        end_ptr = len(clean_str) - 1
        
        while (start_ptr < end_ptr):
            if clean_str[start_ptr] != clean_str[end_ptr]:
                return False
            start_ptr += 1
            end_ptr -= 1

        return True