class Solution:
    def maxProduct(self, words: List[str]) -> int:
        cache = dict()
        max_prod = 0
        for word in words:
            mask, w_len = 0, len(word)
            for c in word:
                mask = mask | (1 << (ord(c) - ord("a")))
            cache[mask] = max(cache.get(mask, 0), w_len)
            for h_mask, h_len in cache.items():
                if (mask & h_mask) == 0:
                    max_prod = max(max_prod, w_len * h_len)
        return max_prod
        