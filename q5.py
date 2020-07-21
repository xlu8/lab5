def palindrome_number():
    rangeI=xrange(100,1000)
    rangeJ=xrange(10,100)
    palindrome = None
    for i in rangeI:
       for j in rangeJ:
          prod = i * j
          if str(prod) == str(prod)[::-1]:
             if prod > palindrome:
                   palindrome = prod
    return palindrome

print(palindrome_number())
