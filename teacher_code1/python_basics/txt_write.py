f = open('mulcam.txt', 'w')
for i in range(10):
    f.write(f"This is line {i}. \n")
f.close()

with open('mulcam2.txt', 'w') as text:
    for i in range(10):
        text.write(f"This is line {i}. \n")

with open('mulcam.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())