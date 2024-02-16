class Solution:
    def longestCommonPrefix(self, l):
        l.sort()
        r=""
        le=len(l)
        a=l[0]
        b=l[le-1]
        for i in range(0,min(len(a),len(b))):
            if(a[i]!=b[i]):
                return r
            r+=a[i]
        return r
