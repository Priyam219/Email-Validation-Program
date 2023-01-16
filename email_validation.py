email = input("Enter your email : ")
# the length of a email atleast 6 i.e. "g@g.in"
flag1,flag2,flag3 = 0,0,0

if len(email)>=6:     #1
  if email[0].isalpha():      #2
    if ('@' in email) and (email.count('@')==1):      #3
      if (email[-4]==".") ^ (email[-3]=="."):     #4
        for i in email:
          if i==i.isspace(): # --------> 5
            flag1 = 1
          elif i==i.isalpha():  # --------> 5
            if i==i.upper():  # --------> 5
              flag2 = 1
          elif i==i.isdigit():  # ---------> 5
            continue
          elif i == "_" or i == "." or i == "@":  # --------> 5
            continue
          else:
            flag3 = 1
        if flag1 == 1 or flag2 == 1 or flag3 == 1:
          print("Invalid Email")
        else:
          print("Your Email is valid.")
      else:
        print("Wrong Email 4 : The position of '.' is wrong")
    else:
      print("Wrong Email 3 : More then one @ or @ is not present")
  else:
   print("Wrong Email 2 : First letter is not alphabet") 
else:
  print("Wrong Email 1 : Missing Character")