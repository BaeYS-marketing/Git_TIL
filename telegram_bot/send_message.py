import requests
from flask import request
from decouple import config



#기본 설정
token = '937766371:AAFQGm4j3KeFk_8B2lz_6P3RxA26rH4EFgE'
#token = config('TELEGRAM_BOT_TOKEN')
app_url = f'https://api.telegram.org/bot{token}'



#서버 응답 내용 저장하기
update_url = f"{app_url}/getUpdates"
response = requests.get(update_url)
response=response.json()   # 파이선 딕셔너리처럼 바꿔주기
print(response)

#chat_id 찾아서 꺼내기
chat_id = response.get('result')[0].get('message').get("chat").get("id")
# chat_id=config('CHAT_ID')

#chat_id를 이용한 메세지 보내기
message_url =f"{app_url}/sendMessage?chat_id={chat_id}&text=첫메세지"
print(requests.get(message_url))  #오.. 해당 URL 입력하면 telegram API의 sendMessage메서드를 거쳐서 출력은 잘 됐다.
print(requests.get(message_url).text) # .text로 내용 뽑고 여기서 다시 파싱 / 요청만 확인하면 되서 안해도 된다.



#webhook이 걸려있어서 안된다. 
# Conflict: can't use getUpdates method while webhook is active; use deleteWebhook to delete the webhook first"


'''
#2 파싱아 아니야.. json이라서 
soup = BeautifulSoup(chat_id , "html.parser")

#1
check_id = request.args.get('chat_id')

print(chat_id)
print(check_id)
'''