import time 
try_to_invite = 0
last_try = 0
while True :  
    login = int(input("Login:"))
    password = int (input("Password:"))
    if login == 240121028 and password == 123456789:
        print ("You invite in your account")
        break
    else:
        try_to_invite +=1
        print("Try again please(you can try invite 3 try)" , try_to_invite)
        if try_to_invite ==3:
            try_to_invite = 0
            last_try +=1
            print ("you can try after 5 sec"  , "Your last try" )
            time.sleep(10)
        if last_try == 2:
            print ("Sorry it is your last invite program close")
            break    
        # I have already done this projcet so it is only for commit
        # it is so boring 