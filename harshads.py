harshads=[]
g = 0
gin_iso=[]
harshads=[]      
#-----------------------------------------------------
for i in range ( 1 , 1001 , 1 ):
#-----------------------------------------------------
    if ( i <= 10 ):        
        harshads.append(i)
        g = g + 1
#-----------------------------------------------------
    elif ( i <= 99 & i > 10 ):
        dek = i % 10
        mon = i // 10
        divisor = dek + mon
        gin = dek * mon
        k = i % divisor
        j = i % gin
        if ( j == 0 ):
            gin_iso.append(i)
        if ( k == 0 ):
            harshads.append(i)
            g = g + 1
#-----------------------------------------------------
    elif ( i > 99 & i <= 1000 ):
        if ( i == 100 or i == 1000 ):
            harshads.append(i)
        else:
            ek = ( i % 100 )
            dek = ( i // 100 ) % 10
            mon = ( i // 100 ) // 10
            gin = ek + dek + mon
            divisor = ek + dek + mon
            j = i % gin
            k = i % divisor
            if ( j == 0):
                gin_iso.append(i)
            if ( k == 0 ):
                harshads.append(i)
                g = g + 1
#-----------------------------------------------------
print "Oi arithmoi harshad mexri to 100 einai: "
print "========================="
for i in harshads:
    print i
    print "========================="
print "Oi arithmoi poy to ginomeno twn psifiwn tous diarei ton idio ton arithmo einai: "
print "========================="
for k in gin_iso:
    print k
    print "========================="

            

