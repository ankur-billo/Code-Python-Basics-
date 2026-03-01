# f = open("hello.txt","rt")
# content=f.read()
# print(content)
# f.close()

with open("hello.text","r") as f: #context manager
    content=f.read()
    print(content)
    #no need of content