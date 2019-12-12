import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com').text
soup = BeautifulSoup(response , "html.parser")


#soup.select_one  한개

box = []


tags = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li > a > span.ah_k")
for tag in tags:
    print(tag.text)

with open('naver.txt','w', encoding ='utf-8') as f:
    f.write("네이버 검색순위 \n")
    for i, tag in enumerate(tags):
        f.write(f'{i+1}.{tag.text} \n')




#1~10위 파싱했던 과정
#4위 든지 아무 순위로 태그 확인한 다음에 그 텍스트 파일 보면서 하나씩 올라가는 방법 
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a > span.ah_k
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li > a > span.ah_k

#11~20위
#ul:nth-child(5)
# >> !!, 그렇다면 여기부터 적어도 되겠다.!



'''for문 돌려서 하려고 헀었는데 아직 미해결

for i in range(1,11) :
    index = soup.select(f"#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child({i}) > a > span.ah_k")
    box.append(index)


print(box)

for context in box :
    print(context.text)
'''



