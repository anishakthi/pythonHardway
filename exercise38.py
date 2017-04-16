mylist=[]
myset = set()
mylist.append("a")
mylist.append("b")
mylist.append("c")
mylist.append("d")
mylist.append("e")

print mylist
myset = set(mylist)
print myset

mydict = {"a":123, "b":345}
mydict.update({"c":456666})
for key, val in mydict.items() :
    print "Map contains ", key, val


# print "Pop " , mylist.pop()
# print "Pop " , mylist.pop()

print "-1 index " , mylist[-1]
print  '#'.join(mylist[1:3])
