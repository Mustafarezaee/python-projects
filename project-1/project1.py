msgs = (  '''
  Requriments for username
   start with lowercase letter     #  userin.islower()
   contains letter , numbers ,and underscores 

  Requirment for password
   contains At least 8 characters long
   Contains at least one uppercase letter
   Contains at least one lowercase letter
   Contains at least one digit
   Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -
   Does not contain any spaces

 '''   )
print(msgs)




password = ''
username = ''


sys_user = ['admin', 'admin123', 'user1', 'superuser']
sys_pass = []






# check = input (" if you have an account press (any key)  if you don't press (n) ").lower()
while True:

  
    ''' sign up           3 step       1/3 :username  2/3: password  3/3:stor    '''
    if  sys_pass == []:
        # print(msgs[0])    #Inform the requirements to the user
        username = input(' Sign up - Enter username : ')
        password = input(' Sign up - Enter password : ')
        # print(username , password)  #test 
        
        
        
        
        '''  user name  '''
        # user name   step: 1/3   1 : check the first char   (username[0] must be only letter and lowercase)
        if  ( not username[0].isalpha()) or (not username[0].islower()) or (len(username) < 5):
            print(" \n Username should start with lower letter and must be more than 5 character \n ")

            # print(" I hit the step 1/3 ==  repat taking user name and password")    #test
            continue

  
        # user name step 2/3   2: check each character in username_input (only letter, digit, under_score is valid)
        if not all( char.isalpha() or  char.isnumeric() or char == '_'  for char in username):
        
            print('\n invalid character, only letters, numbers and underscore is valid \n')
            # print("I hit step 2/3 == repeat taking username")
            continue
        # user name step 3/3   3: if i pass step 1 and 2 it means my username is ready to store in system but you have  to care of dublicate before storing


        
        
        
        '''  password  '''
        if (len(password) < 8) :
            print(" \n Password must be more thane 8 character \n")
            # print("password: <8 step 1/6 ")
            continue
  

        if not any(char.islower() for  char in password):
            print("\n Error : password should b least on lower case character \n")
            # print("password: lowercase step 2/6 ")
            continue

        if not any(char.isupper() for char in password):
            print(" Error : password should have at least a lower case, adigit and a upper case letter")
            print("password: upercase step 3/6 ")
            continue
  
        if not any(char.isdigit() for char in password):
            print("password: Digit step 4/6 ")
            print("\n Error : password should contain at least a lower case, adigit and a upper case letter \n")
            continue
     
     
        if not any(char in "  '%','!','?','@','#','$','^','&','*','-','_'"  for char in password ):
            print(" \n the password should contain at least one this charters \n  '!','?','@','#','$','^','&','*','-','_' \n" )
            # print("password: #$%^ step 5/6 ") test
            #  print(char)
            continue
  
        if any(char == " " for char in password):
            print(" \n Password doesn't contain any space \n")
            # print(" step 6/6 ") test
            continue
  
        '''' you nedd to check the username is not already taken then add to the system'''

  

        if any(item in username for item in sys_user):
            print("\n This username is already taken try again \n")
            continue
  
    
        sys_user.append(username)
        sys_pass.append(password)
        print(sys_user.append(username))
        print("\n\n You seccussfully signed up  \n \n")

        # print(sys_user, sys_pass, "\n")  # Test
        
       
    else:
    # Log-in process
        username = input("Log in - Enter your username: ")
        password = input("Log in - Enter your password: ")

        if username in sys_user and password in sys_pass:
            print("\n \n    Login successful!   \n \n")
            break
        else:
            print(" \n Error: Incorrect username or password. Please try again. \n")
     


