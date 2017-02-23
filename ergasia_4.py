
#please insert your list 
num_lis = [-45,-3,-5,-6,-7,-8]
if ( len( num_lis ) <=4 ):
   print "Wrong Insert"
else:
#checkin if they are not all the same !!
   num_lis.sort()
   first = min(num_lis)
   last = max(num_lis)
   if ( first == last ):
      print "Wrong Insert because they are all the same numbers"
   else:
#checking if there are 4 diferent values
      count = 0
      checkvar = num_lis[0]
      for i in range ( 1 , len(num_lis) , 1 ):
         if ( checkvar != num_lis[i] ):
            count = count + 1
      print count    
      if ( count > 4 ):
#for the high values(pop)
         for i in range ( 0 , 2 ,1 ):
            a  = max(num_lis)
            b = max(num_lis)
            while ( a == b ):
               num_lis.pop()
               a = max(num_lis)

#for the low values(del)
         for j in range ( 0 , 2 , 1 ):
            a = min(num_lis)
            b = min(num_lis)
            while ( a == b ):
               del num_lis[0]
               a = min(num_lis)
      else:
          print "Wrong Insert"
#now we have our list ready :)
   sum_lis = sum(num_lis)
   mesos_oros = float(sum_lis)/(len(num_lis))
   times=[]
   for i in num_lis:
      a = ( i - mesos_oros)**2
      times.append(a)

   sum_times = sum(times)
   mesos_orosTimes = sum_times / len(times)
   typ_apoklisi = mesos_orosTimes**(1/2.0)
   print "H typikh apoklisi twn timwn tis listas einai: ",typ_apoklisi

