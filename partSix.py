age = int (input(" how old are you?"))
std = input(" student or non student")
if age <12 and age >=65 and std == "n/a" :
    print("£5 please")
elif age >= 12 and age <65 and std == "student":
    print("£8 please")
elif age >= 12 and age <65 and std == "non-student":
    print("£10 please")