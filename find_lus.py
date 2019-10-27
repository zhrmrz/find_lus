class Sol:
    def find_lus(self,s,t):
        if s in t:
            return -1
        ln=len(s)
        common=[]
        l=0
        for i in range(len(s)):
            if s[i]==t[i]:
                l+=1
            else:
                common.append(l)
                l=0
        if l!=0:
            common.append(l)
        m=ln-max(common)
        return m
