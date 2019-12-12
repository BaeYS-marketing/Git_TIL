             #3
def awesome(funcV):
    def wrapper():
        funcV()  # print(I'm ordinary)
        print("No, you are awsome")
    return wrapper

#데코레이터 목적 : 너희가 알 필요없어, 그냥 써 / 기존 ordinary 함수를 건들일 필요가 업다는 것이 장점
@awesome  #1
def ordinary(): #2
    print("I'm ordinary")

ordinary()


#extra_ordinary = awesome(ordinary)
#print(extra_ordinary)  # function
