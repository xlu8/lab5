
one= ['zero','one','two','three','four','five','six','seven','eight','nine']
ones= ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens= ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','one hundred']

def find(str):
  try:  
    temp = one.index(str)
  except: 
    try:
      temp = ones.index(str)+11
    except:
      temp = tens.index(str) +1 
      temp = temp * 10
  return temp; 

firstNum = raw_input ('enter a string number smaller than 100: ')
secNum = raw_input('enter a string number smaller than 100: ')
firstNum = firstNum.split('-')
n = len(firstNum)
if( n == 1):
  firstNum  = find(firstNum[0])
  
else:
  temp1 = find(firstNum[0])
  temp2 = find(firstNum[1])
  firstNum = temp1 + temp2 

secNum = secNum.split('-')
n2 =len (secNum)
if (n2 ==1):
  secNum = find(secNum[0])
else:
  temp3 =find(secNum[0])
  temp4 =find(secNum[1])
  secNum = temp3 + temp4

total = firstNum * secNum
print firstNum,'*',secNum, '=' , total
