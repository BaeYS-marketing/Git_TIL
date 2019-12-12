
import random


name = "홍길동"
english_name = "hong"

#옛날방식 _ : pyformat
print("안녕하세요, {}입니다. my name is {}".format(name, english_name))


#요즘 방식  : f-string
print(f"안녕하세요, {name}입니다. My name is {english_name}")





#로또 
numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(f"오늘의 행운의 번호는 {sorted(lotto)} 입니다.")