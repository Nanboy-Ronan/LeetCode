# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    # Bit-wise Operation
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result += n & 1
            n >>= 1
        return result