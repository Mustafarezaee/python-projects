
''' Print statement outlining rules for your application'''


print("Welcome to the website sign-up!")


''' Initialize your variables 

We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''

system_username = set()
system_password = set('admin','admin123','admin_123')

userin_username , userin_password = '', ''


''' A List to handle error messages '''

msgs = ['msg1' , "msg2", 'msg3' ]

''' Start your while loop '''

while True:


  ''' Get your username and password'''
  userin_username = input(" User name :  ")
  userin_password = input(" password  :  ")
  # print( userin_username, userin_password)


  ''' Test your username and enforce logic'''



''' Test your password and enforce logic'''



''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



