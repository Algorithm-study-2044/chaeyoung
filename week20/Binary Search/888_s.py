class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        avg = (sum(A) - sum(B)) // 2
        A = set(A)
        for b in B:
            if avg + b in A:
                return [avg + b, b]