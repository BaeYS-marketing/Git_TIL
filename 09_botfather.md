# botfather

1. /newbot
2. 이름 
3. <이름.bot> or <이름_bot>



- 비밀(로그인) 토큰 받는다. : 챗봇 서버사용 접근

---

---

1.API https://api.telegram.org/bot<token> 항상 기억 이후 메서드
    1번 비밀토그 입력

<getme 메서드 예시>
https://api.telegram.org/bot937766371:AAFQGm4j3KeFk_8B2lz_6P3RxA26rH4EFgE/


3. json 형태의 응답이다. 


--

1.내꺼 봇에 들어간다(firstbot)

https://api.telegram.org/bot937766371:AAFQGm4j3KeFk_8B2lz_6P3RxA26rH4EFgE/getUpdates



sendMessage
https://api.telegram.org/bot937766371:AAFQGm4j3KeFk_8B2lz_6P3RxA26rH4EFgE/snedMessage

에러 , 같이 보내줘야하는 값을 안보내줬다.


쿼리로 보재주어야한다. 메서드 뒤에 ?   여러 개 연결 &

chat_id = 901234009
text = 메시지보내기

쿼리 : ?chat_id=901234009&text=메시지보내기


> /sendMessage?chat_id=901234009&text=메시지보내기







env 파일로 숨김

#cmd 창에서 ngrok 열기
./ngrok http 5000

---



내 pythonanywhere 주소

### [baeys93.pythonanywhere.com](http://baeys93.pythonanywhere.com/)



[telegram 공식다큐먼트](https://core.telegram.org/bots/api#available-types)





IP URL 

https://www.slideshare.net/ssuser8fdc37/ip-dns-url

http://blog.daum.net/ash3379/11807124





python _ .stream = True

https://requests.readthedocs.io/en/master/user/advanced/





**Webhook** 이라는 것은 웹 서비스를 제공해주는 서버 측에서 어떠한 이벤트(또는 데이터)를 외부에 전달하는 방법 중 하나이다. 내 공책에는 이렇게 적혀있었고 잘 이해가 안갔다! 다시 차례대로 정리를 해보겠다. 

우선 **Hooking**의 의미를 알아야하는데 어떠한 액션 앞 또는 뒤에 추가로 어떠한 일을 하도록 하는 것을 말한다. Webhook 이라는 건 웹에서 이러한 Hooking 을 할 수 있도록 제공하는 것이다. 어떠한 서비스에 대해서 Hooking을 할 수 있도록 기능을 제공해야하는데, Hooking을 해서 처리하려는 웹서버를 통해 액션을 만들고 이 액션의 URL을 등록하는 방식이 Webhook!

[참조사이트](https://kswims.tistory.com/143)