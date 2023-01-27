'''
Assignment 4
'''

#Ques1

x=int(input("Enter your marks: "))

if x<25:
    print("Your Grade is F.")
elif 25<=x<=45:
    print("Your Grade is E.")
elif 45<x<=50:
    print("Your Grade is D.")
elif 50<x<=60:
    print("Your Grade is C.")
elif 60<x<=80:
    print("Your Grade is B.")
elif 80<x:
    print("Your Grade is A.")