#Hopefully I get this right =)
def palindrome():
    drome=raw_input("Write something. ")
    
    if str(drome)==str(drome)[::-1]:
        print "This is a palindrome. "
    else:
        print "This is not a palindrome. "
palindrome()
