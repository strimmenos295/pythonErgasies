num = int(input("Enter a Number: "))
if (num < 10 and num > -10):
    print(num)
elif (num >= 10):
    while num >= 10:
        num=num*3
        num=num+1
        result = 0
        while num >0:
            dig = num % 10
            result = result + dig
            num = num//10
        num = result
        print(num)
else:
    while (num <= -10 or num >= 10):
        num=num*3
        num=num+1
        result = 0
        absoluteValue = abs(num)
        while absoluteValue > 0:
            dig = absoluteValue % 10
            result = result + dig
            absoluteValue = absoluteValue // 10
        num = result
        print(num)
wait=input("press enter")