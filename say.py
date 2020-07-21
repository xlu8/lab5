one= ['zero','one','two','three','four','five','six','seven','eight','nine']
ones= ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens= ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','one hundred']

num = input('enter number: ')
num = int(num)
if num <10:
       print('number: ', one[num])
elif num <20 and num> 10:
       print('number : ', ones[num%10 -1])
elif num % 10 ==0:
       print('number: ', tens[int(num /10)-1])
else:
       tens = tens[int(num /10) -1]
       one = one[num %10]
       print tens, "-", one
