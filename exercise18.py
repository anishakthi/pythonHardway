def agrs_together(*args) :
    arg1, args2 = args # unpacking
    print "I am one %s and i m two %s" %(arg1, args2)


def arg_separate(args1, args2):
    print "I am one %s and i m two %s " %(args1, args2)


agrs_together("1","2")
arg_separate("1","2")
