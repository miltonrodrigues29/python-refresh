lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The prime numbers in the range are:")

[1,2,3,4,5,6,7,8,9,10]
for number in range( lower_value, upper_value+1):
    if number>1:
        for i in range(2,int(number/2)+1):
            if number%i == 0:
                break

    
        else:
            print(number)
