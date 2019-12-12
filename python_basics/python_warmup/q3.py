'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('input number please : '))
# 아래에 코드를 작성해 주세요.

if number %2 ==0 :
    print("input number {} is Even.".format(number))

else :
    print("input number {} is odd".format(number))