# a = len(s)
# count = 1
# i = 0
# while i <= (a / 2):
#     if s[i] == s[a - i - 1]:
#         count = 1
#         i += 1
#     else:
#         count = 0
#         break
# if count == 1:
#     return True
# else:
#     return False
import re
s = re.sub('[^a-z0-9]',' ',s.lower())
return s ==s[::-1]

