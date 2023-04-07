str = input("문자열 입력 : ")

if str.isdigit() == True:
  print("숫자입니다.")
elif str.isalpha() == True: 
  print("문자입니다.")
elif str.isalnum() == True: 
  print("문자+숫자입니다.")
else :
  print("모릅니다.")
