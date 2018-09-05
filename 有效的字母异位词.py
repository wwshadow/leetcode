if len(s) != len(t):
    return False
c = set(s)
for i in c:
    if t.count(i) != s.count(i):
        return False
return True