import re
text= " lungi dance, lungi dance muchoko thoda round ghuakee"
match= re.search("dance",text)
print(match)
if match:
    print("Match Found!")
    print("Start Index: ",match.start())
    print("End Index: ",match.end())