 

sys_name = ["admin"]
sys_pass = ["333"]


Do_U_have_Account = input(" Do you hava an Account (yes or no) :")
Do_U_have_Account.lower()



while True:
  
  if  Do_U_have_Account == "no":
    userin_name = input(" Enter your name : ")
    userin_pass = input(" Enter your pass : ")

    # requiremets for user name
    if not userin_name[0].islower():
      print(" Username must start with lowercase")
      continue
    if not all(c.isalnum() or "_" in userin_name for c in userin_name):
      print("Username only contains letters, numbers, and underscores.")
      continue

    # requirments for password
    if len(userin_pass) < 8:
      print("The lenght of password must be longer than 8 characters")
      continue
    if not any(char.isupper() for char in userin_pass):
      print(" Password contains at least one uppercase letter")
      continue
    if not any(char.islower() for char in userin_pass):
      print(" Password contains at least one lowercase letter")
      continue
    if not any(char.isdigit() for char in userin_pass):
      print(" Password contains at least one digit")
      continue
    if not any(char in "!, ?, @, #, $, ^, &, *, _, -" for char in userin_pass):
      print("Password Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -")
      continue
    if any(char == " " for char in userin_pass):
      print("Password doesn’t contain any spaces")
      continue

    sys_name.append(userin_name)
    sys_pass.append(userin_pass)
    Do_U_have_Account = "yes"
    # print(sys_name , sys_pass)

  if Do_U_have_Account == "yes":
    userin_name = input(" To log in Enter your name : ")
    userin_pass = input(" To log in Enter your pass : ")

    if (userin_name in sys_name )and (userin_pass in sys_pass):
      print("Logged in successfuly !")
      break
    else:
      print("Wrong username and password")
      continue




  



   





    


