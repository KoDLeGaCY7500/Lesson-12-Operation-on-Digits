# number=int(input("Input number"))
# result=0
# temp=number
# while temp !=0:
#     digit=temp%10
#     result=result+digit**3
#     temp=temp//10

# print(result)
# if number==result:
#     print(number,"It is an armstrong number")
# else:print("Sorry, This number dosen't comply as armstrong number. Please choose a different number")

def factors(number):
    print("The factors of the number are ")
    for i in range(1,number+1):
        if number %i==0:
            print(i)

factors(10)
