import urllib2
import json

user = []

result = 0

#input list user bellow

user = [5,8,1,4,3,9,6]

if ( max(user) > 9 or min(user) < 0 ):

    print "Wrong Insert"

else:

    for i in range ( 01 , 32, 1 ):

        flag = False
        
        dt = i
        
        count = 0        

        response = urllib2.urlopen('http://applications.opap.gr/DrawsRestServices/proto/drawDate/0%d-02-2017.json'%dt)

        html = response.read()

        draws = json.loads(html)["draws"]["draw"]

        nums = []

        for d in draws:

            print "-----------------------------------"

            nums += d["results"]


        if ( len(nums) > 0 ):

            print "draws: ",nums

            print "user : ",user

            if ( nums[0] == user[0] and nums[1] == user[1] ):

                print "-----------------------------------"

                print "YES"

                result += 1

                flag = True

            elif ( nums[5] == user[5] and nums[6] == user[6] ):

                print "-----------------------------------"

                print "YES"

                if ( flag == False ):
                    result += 1

             
                    

               


print "The possible wins are: ",result


















                


           
                
