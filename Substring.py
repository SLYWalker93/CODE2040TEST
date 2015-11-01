def substring():
    S=raw_input("Input text. ")
    if S.isalpha():
        print len(S)
        print S[0:100000]
    
    else:
        print "False. "

substring()
