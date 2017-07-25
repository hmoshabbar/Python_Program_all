vowels="aeiouAEIOU"
number="1234567890"
sign="!#@%&*$_-+=?<>"
consonent="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
while True:
    n=raw_input("Enter Your alphabet:")
    if n in vowels:
        print "Thank You!"
        print "You Entered Alphabet its a Vowel"
    elif n in number:
        print "Thank You!"
        print "You Entered Alphabet its a Number"
    elif n in sign:
        print "Thank You!"
        print "You Entered Alphabet its a Special Symbol"
    elif n in consonent:
        print "Thank You!"
        print "You Entered Alphabet its a Consonent"
    else:
        print "OPPS !"
        print "Please Enter again i could not guess it...."

        
    
