class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        frog = 0
        for croak in croakOfFrogs:
            if croak == 'c':
                c+=1
            elif croak == 'r':
                r+=1
                if r > c:
                    return -1
            elif croak == 'o':
                o+=1
                if o > r:
                    return -1
            elif croak == 'a':
                a+=1
                if a > o:
                    return -1
            elif croak == 'k':
                frog = max(frog, c-k)
                k+=1
                if k > a:
                    return -1
        if k == c:
            return frog
        else:
            return -1

print(Solution().minNumberOfFrogs("croakcroa"))