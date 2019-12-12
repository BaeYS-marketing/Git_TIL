f = open("mulcam.txt",'w')


for i in range(10) :
    f.write(f"This is line {i}. \n")

f.close()



with open("mulcam2.txt",'w') as file:
    file.write(f"This is line {i}. \n")




with open('mulcam.txt', 'r') as f:
    lines = f.readlines()
    #print(lines)  #개행문자 표시되서 보기 불편
    for line in lines:
        print(line.strip())





'''연습문제 
0
1
2
3 
'''

with open('test.txt','w') as t :
    for i in range(4):
        t.write(f"{i} \n")


with open('test.txt','r') as r :
    testLines = r.readlines()
    
    #역순으로 정렬
    testLines.reverse()

    for line in testLines :
        print(line.strip())





