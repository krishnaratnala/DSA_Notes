'''
def sum_of_digits(num):
  if num==0:
      return 0
  return sum_of_digits(num//10)+(num%10)
num=2223
print(sum_of_digits(num))
'''
'''
product of digit


def product_value(num):
    if num%10==num:
        return num
    return product_value(nuum//10)+num%10
num=2223
print(product_values(num))
'''