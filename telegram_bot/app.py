from flask import Flask
from flask import request
from flask import render_template
from decouple import config
import requests
import random

app = Flask(__name__)  #SERVER 이름 붙이기


#이제 부터 서버 길 만들고 -> 들어왔을 때 실행할 로직 만들기 순

#token = '937766371:AAFQGm4j3KeFk_8B2lz_6P3RxA26rH4EFgE'
token = config('TELEGRAM_BOT_TOKEN')
app_url = f'https://api.telegram.org/bot{token}'   # 이게 베이스 url ~ 이제 뒤에 메서드만 바뀌면서 작업할 것
#chat_id=config('CHAT_ID')  #네이버 papago 기능 많은 사람 초대 사용하기 위해

#에러 401관련
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    message = request.args.get('message')
    message_url =f"{app_url}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(message_url)
    return '메세지 전송 완료'  #return 이 없으면 에러가 나서 설정.






#webhook

#set_webhook.py 길 만들어준다. 
@app.route(f'/{token}',methods=["post"])
def telegram():
    #1.request print 해보기
    #print(request.get_json())
    
         #1번 기능 추가 : 말 추출
    from_telegram = request.get_json()  #모든 기본이 된다. 다 여기서 작업하게 될 것
    
    chat_id = from_telegram.get('message').get('from').get('id')
    text = from_telegram.get('message').get('text')


    if from_telegram.get('message').get('photo') is not None:
        #사진이 왔을 때 여기 코드 작성
        #1. 우선 파일의 아이디 값을 가져온다. 
        file_id = from_telegram.get('message').get('photo')[-1].get('file_id')
        
        #2. 가져온 파일 아이디로 실제 파일을 가져온다.
        file_res =  requests.get(f'{app_url}/getFile?file_id={file_id}')
        
        
        #3. file path를 뽑아내서 저장
            #print(file_res)
            #file_path = file_res.json() #json으로 변환 그리고 파싱
        file_path = file_res.json().get('result').get('file_path')

        #4.해당 파일의 경로를 찾아서 저장
        #file_url = f'{app_url}/file/bot{token}/{file_path}'
        file_url = f'https://api.telegram.org/file/bot{token}/{file_path}'
        print(file_url) #파일 경로 확인

        #5. 사진(파일)이 있는 주로소 요청을 보내서 가져오자
        '네이버 개잘자 - clova a.i apis - cfr api 사용하기 - 첫 번째 예시'
        real_file_res = requests.get(file_url, stream=True)

        headers = {
            'X-Naver-Client-Id': naver_client_id,
            'X-Naver-Client-Secret':naver_client_secret
        }
            #클로바A.I에 포스트 형식으로 묶어서 보내기 _ 예시 활용
        clova_res = requests.post('https://openapi.naver.com/v1/vision/celebrity',\
            headers=headers, files = {
            'image':real_file_res.raw.read()  # .raw.read 붙여서 보내야한다. 
        })

        #print(clova_res)
        print(clova_res.json())

             #닮은 유명인 수가 있을 경우
        if clova_res.json().get('info').get('faceCount'):
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            '''TypeError: 'NoneType' object is not subscriptable 
            해당 기능이없는 객체의 색인을 생성하려고 시도했음을 의미한다고 한다.'''
            #예시>
            #my_var = None
            #x = my_var[0] 
            
            reply = f"{celebrity.get('value')} - {celebrity.get('confidence')*100}%"

        else:
            reply = "인식된 사람이 없습니다."


        #5 최종적으로 사진(파일)이 있는 주소로 요청을 보내서 가져오자



    
    else:
        #text가 왔을 때 실행

            #2번 기능 추가 : <로또> 텔레그램에 /로또 라고 입력하면, 로또 번호 6자리를 뽑아서 보내주기
        if text =='/로또':
            reply = random.sample(range(1,46),6)
        else:
            reply = text


            #3번 naver_papago
        '사전 과정 : 네이버 개발자 > papago API 신청 > 토큰 정보 .env파일에 저장  // 개발자 가이드 펼치기'
        if text[0:4] == '/번역 ':   #/번역 번역할 문장 
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
            headers = {                                           #에러 401 해결
                'X-Naver-Client-Id':naver_client_id,
                'X-Naver-Client-Secret':naver_client_secret
            }
            data = {
                'source':'en',
                'target':'ko',
                'text':text[4:]
            }
            papago_res=requests.post(papago_url, data=data, headers=headers)
            #번역문 가져오기 위해 
            papago_res =papago_res.json()
            reply = papago_res.get('message').get("result").get("translatedText")

            print(papago_res)
            #[분석] papago_res.json 파일 만들어서 코드 복붙 : shift alt b (정렬)
            ''' 왜 오류인지 알아보자!!
            print(papago_res.text); print(papago_res) #이것은 허용
            fruits = []
            apple = ''

            fruits.append()
            apple.append()
            '''    
        else:
            reply = text
    
    #들여쓰기 조심하자!
    requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={reply}')  #2번 기능 응답
    #requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')  #1번 기능 응답
    
    
    #res = requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')  #쌤 버그 수정 떄 코드
    #print(res)

    #401 권한이 없다

    return '',200




if __name__=='__main__':
    app.run(debug=True)  #debug=true : 코드를 수정하면 서버 껐다가 작동시킬 필요없이 바로 시행 됌 


#<배포!!>
    #1 많은 사람들이 접근하면 터진다. 
    #2 항상 컴퓨터를 켜 놔야한다.


