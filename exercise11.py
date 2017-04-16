name = raw_input("What is your name ")
age = raw_input("What is your age ")

if int(age) > 18:
    print "Hey %s you are %s" %(name, "major")
else:
    print "Hey %s you are %s" %(name, "minor")
