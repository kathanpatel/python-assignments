print("********MENU********")
print("*   press 1. add   *")
print("*   press 2. sub   *")
print("*   press 3. mul   *")
print("*   press 4. div   *")
print("*   press 5. per   *")
print("********************")
flag=True
while flag ==True:
	var1=int(input("Enter 1st number: "))
	var2=int(input("Enter 2ed number: "))
	choice=int(input("Enter your choise: "))
	if choice == 1:
		print(var1+var2)
		flag = False
	elif choice == 2:
		print(var1-var2)
		flag = False
	elif choice == 3:
		print(var1*var2)
		flag = False
	elif choice == 4:
		print(var1/var2)
		flag = False
	elif choice == 5:
		print(var1%var2)
		flag = False
	else:
		flag = False
		print("choose correct choice")
	var3 = input("do u want to continue ?? (y/n) :")
	if var3 =='y':
		flag = True
	else:
		flag = False