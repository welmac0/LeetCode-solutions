# v1 done in like 20 minutes, ~1000ms, 88 mb
class TimeMap:
    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm.keys():
            self.tm[key] = [None]  # key: [None]

        while len(self.tm[key]) - 1 < timestamp:
            self.tm[key].append(None)

        self.tm[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        searched = self.tm.get(key)

        if searched is None:
            return ""

        t = timestamp
        while t >= 1 and (len(searched) <= t or searched[t] is None):
            t -= 1

        if searched[t] is None:
            return ""

        return searched[t]
        
# v2 done
class TimeMap:

    def __init__(self):
        self.tm = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        # v2
        if self.tm.get(key):
            self.tm[key][timestamp] = value
        else:
            self.tm[key] = {}
            self.tm[key][timestamp] = value
        """
        self.tm = {
            key1 =
            {
                timestamp1 = value
                timestamp2 = value
            },
            key2 = 
            {
                timestamp1 = value
                timestamp2 = value
            }
        }
        """        

    def get(self, key: str, timestamp: int) -> str:
        if self.tm.get(key) is None: # if key not in self.tm
            return ""

        sv = None
        for ts in sorted(self.tm[key]):
            if ts <= timestamp:
                sv = self.tm[key][ts]
            else:
                break

        if sv is None:
            return ""

        return sv

# v2.5 ~1300 ms, 16mb memory
class TimeMap:

    def __init__(self):
        self.tm = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        # v2
        if self.tm.get(key):
            self.tm[key][timestamp] = value
        else:
            self.tm[key] = {}
            self.tm[key][timestamp] = value
        """
        self.tm = {
            key1 =
            {
                timestamp1 = value
                timestamp2 = value
            },
            key2 = 
            {
                timestamp1 = value
                timestamp2 = value
            }
        }
        """        

    def get(self, key: str, timestamp: int) -> str:
        if self.tm.get(key) is None: # if key not in self.tm
            return ""
        from bisect import bisect_right

        # coded with neetcode solution
        tses = list(self.tm[key].keys())
        idx = bisect_right(tses, timestamp) - 1 # pod kroty index wstawic timestamp, zeby lista pozostala posortowana
        if idx >= 0:
            return self.tm[key][tses[idx]]
        return ""

# v3, just neetcode solution with written myself function get after figuring out how to do this
# 356ms, 16mb
class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

