print """Welcome to the world of Light and dark
Enter your answer as 0 or 1 that will head you to some levels and return you to heaven or hell based on the option you enter"""
sun_moon = raw_input("Enter the option 1 or 0 ")
if sun_moon == "0":
    print "Welcome to the world of sun"
    print "Try solving the quiz about sun to go heaven"
    question1 = raw_input("One million Earths could fit inside the Sun? \n \t* if True enter 1 \n \t* if False enter 0")
    if question1 == "1":
        print "Yes Your are right! you are going to heaven :)"
    elif question1 == "0":
        print "Ooopss You are wrong! You are going to hell :("
    else :
        print "Dont be over genius, Input should be 0 or 1."

elif sun_moon == "1":
    print "Welcome to the world of Moon"
    print "Try solving the quiz about moon"
    question2 = raw_input("The Moon is not a light source, it reflects light from the sun. \n \t* if True enter 1 \n \t* if False enter 0")
    if question2 == "1":
        print "Yes Your are right! you are going to heaven :)"
    elif question2 == "0":
        print "Ooopss You are wrong! You are going to hell :("
    else :
        print "Dont be over genius, Input should be 0 or 1."
else :
    print "Dont be over genius, Input should be 0 or 1."
