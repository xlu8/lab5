one= ['zero','one','two','three','four','five','six','seven','eight','nine']
ones= ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens= ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','one hundred']

def find(str):
  try:  
    i = one.index(str)
  except: 
    try:
      i = ones.index(str)+11
    except:
      i = tens.index(str) +1 
      i = i * 10
  return i ;

num = raw_input ('enter string number: ')
num = num.split(' ')
n =len(num)
if( n ==1):
  num1 = find(num[0])
  print(num1)
else:
  num1 = find(num[0])
  num2 = find(num[1])
  print ( num1 + num2)
