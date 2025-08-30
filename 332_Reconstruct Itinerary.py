class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []
        cache = dict()
        for ticket in tickets:
            if ticket[0] not in cache:
                cache[ticket[0]] = []
            cache[ticket[0]].append(ticket[1])
        for ticket in cache.keys():
            cache[ticket].sort(reverse=True)
        s = ["JFK"]
        while len(s) > 0:
            t = s[-1]
            if t not in cache or len(cache[t]) == 0:
                itinerary.append(t)
                s.pop()
            else:
                t_next = cache[t].pop()
                s.append(t_next)
        ans = list(reversed(itinerary))
        return ans
