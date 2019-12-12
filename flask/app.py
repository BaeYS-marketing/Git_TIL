
import random
from flask import Flask  #모듈 불러옴
from flask import render_template
from flask import request
import requests


app = Flask(__name__)  # app은 서버 이름 



@app.route('/')    # @는 데코레이터; 다른 사람들이 서버로 올 수 있게 길을 만들어줄 꺼야 , 길의 주소가 '/' (/ = local host)
def hello_world():               # 서버로 접근하면 함수를 실행할꺼야
    return 'Hello, World!'       # 서버 접속에 대한 서버 응답


@app.route('/mulcam')
def mulcam():
    return 'This is mulcam'


#@app.route('/greeting/bae')
#def greeting():
#    return 'Hello, bae!'


@app.route('/greeting/<string:name>')
def greeting(name):
    return f"Hello,{name}!"


@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)   #무조건 string만 출력해줘야한다.


@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면','짬뽕','볶음밥','고추잡채밥']
    order = random.sample(menu,people)
    return str(order)


@app.route('/html')
def html():
    return '<h1>안녕하세요!!!</h1>'


@app.route('/html_file')
def html_file():
    return render_template("html_file.html")


@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html',your_name=name)    #flask jinja 라는 것을 수행하게 해준다.


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('pong.html',pong_name = name , pong_message = message)




#실습1_ 신이 나를 만들 때  : 파일이름이 app.py 이여야 하고,  app = Flask(__name__) 
@app.route('/pr_input')
def commit():
    return render_template("pr_input.html") 


@app.route('/pr_instance')
def pr_instance():
    name=request.args.get('user')
    atr=["미모","기럭지",'성격','돈','광채','신앙']
    attribute = random.sample(atr,2)
    #attribute=' '.join(map(str,attribute))
    one=attribute[0]
    two=attribute[1]       
    return render_template('/pr_instance.html',you=name, thing1=one, thing2=two)
                                               #you=name, chosen=attribute
                                               





#실습2 아스키코드로 입력 받기
@app.route('/ascii')
def ascii():
    return render_template('ascii.html')

@app.route('/ascii_result')
def ascii_result():
    #1. form 태그로 날린 데이터(word)를 받는다.
    #request != requests : 패키지가 서로 다른 것!!! 
    word=request.args.get('input_word')
    word2=request.args.get('input_word2')

    #2. word를 가지고 ascii_art API 요청 주소로 요청을 보낸다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}')
    result2 = requests.get(f'http://artii.herokuapp.com/make?text={word2}')
   
    print(result.text)
    ascii_text = result2.text

    #3. API 응답 결과를 html 파일에 담아서 보여준다( ★템플릿을 랜더링한다). 
    return render_template('ascii_result.html',show_text=ascii_text)





#실습3 : 로또!!
@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    #선언하기 전 사용에러 = UnboundLocalError: local variable 'lotto_round' referenced before assignment
    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    
    #딕셔너리라고 했지만 그냥 갸져오면 string 그래서 .jason()
    lotto = response.json()  
    
    #딕셔너리 형식 추출_ 방법1
    drwtNo6 = lotto["drwtNo6"]

    #딕셔너리 형식 추출_방법2 [권장] ~ 차이점 lotto.get() 이면 NONE 값이 나오지만 위의 인덱싱 방법은 에러 발생
    drwtNo6 = lotto.get("drwtNo6")

    #추출 방법 1) for
    winner = []
    for i in range(1,7):
        winner.append(lotto[f"drwtNo{i}"])

    numbers = request.args.get('numbers')   #1 string
    numbers = numbers.split()      # list인데 string으로 된 list
    
    numbers_int = []
    for number in numbers:
        numbers_int.append(int(number))

    matched = (set(winner) & set(numbers_int))  #집합 자료형 / 특수 경우(bit 연산 : & 사용)
    if matched == 6:
        result = '1등입니다.'
    elif matched == 5:
        if lotto["bnusNo"] in numbers_int:
            result = "2등 입니다."
        else:
            result = "3등 입니다."
    elif matched == 4:
        result = "4등 입니다."
    elif matched == 3:
        result = "5등 입니다."
    else:
        result = "꽝"


    
    #추출 방법 2) List Comprhension
    #winner = [lotto[f'drwtNo{i}'] for i in range(1,7)]

    return render_template('lotto_result.html',
        lotto_round = lotto_round , winner= winner, result=result,
        numbers=numbers_int)








#파이썬 파일 시행으로 "콘솔창에서 :  flask run  " 입력안해도 되는 코드!

if __name__== '__main__' :   #직접 실행시킬 때만 파일 시행시킨다. / 어디서 불러오면 실행안됌.
    app.run(debug=True)