class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        si = 0
        gi = 0
        sl = len(s)
        gl = len(g)
        count = 0
        while (si < sl and gi < gl):
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi