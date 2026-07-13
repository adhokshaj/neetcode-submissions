from functools import cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_length = 0

        @cache
        def is_palindrome(i, j):
            if i >= j:
                return True

            return (
                s[i] == s[j]
                and is_palindrome(i + 1, j - 1)
            )

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    length = j - i + 1

                    if length > max_length:
                        max_length = length
                        start = i

        return s[start:start + max_length]