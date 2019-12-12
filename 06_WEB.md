# 웹(WEB)  :  '요청과 응답' 이 전부다!

>- 요청 : 사용자(client)
>
>- 응답 : 서버 



1. 사용자가 서버에 요청할 수 있는 수단은 `web browser` 이다.
2. `web browser`의 **URL 입력창**을 통해서 요청하게 된다. 



* 서버의 응답은 파일 형태로 준다.
* 네이버 현재 페이지 저장하면 `.HTML` 로 응답해준 파일  확인가능
* 그 응답받은 저장파일에서는 개발자 도구를 통해 조작도 가능하다.





## 파이썬 웹 크롤링

> - 파싱(parsing)을 잘해야 한다.
> - 부모태그에서 자식태그로 확인하기도 하지만,
> - 자식태그에서 부모태그로 **역순** 으로 확인도 해보자.



### 참조

#### 엘리먼트 :  시작태그 ~ 종료태그까지  _ 전체

#### 태그 :   < > 로 묶인 명령어를 말하며, 속성과 (속성)값 으로 이루어진다.



```html
<a href="http://opentutorials.org"> 오픈튜토리얼스 </a>
```

> * 태그 : a
> * 태그 속성 : href
> * 내용 : 오픈튜토리얼스
> * 엘리먼트 <a ...~ > </> _전체 





***





# Flask

>`server`를 개발하는 툴 중에서 
>
>파이썬을 기반으로 하여, 굉장히 빠르고 간편한 개발 툴







***





# JSON

## (JavaScript Object Notation)

- JSON은 경량(Lightweight)의 DATA-교환 형식
- Javascript에서 객체를 만들 때 사용하는 표현식을 의미한다.
- JSON 표현식은 사람과 기계 모두 이해하기 쉬우며 용량이 작아서, 최근에는 JSON이 XML을 대체해서 데이터 전송 등에 많이 사용한다.
- 특정 언어에 종속되지 않으며, 대부분의 프로그래밍 언어에서 JSON 포맷의 데이터를 핸들링 할 수 있는 라이브러리를 제공한다.

### 파이썬_딕셔너리 형태

```json
{
  "firstName": "Kwon",
  "lastName": "YoungJae",
  "email": "kyoje11@gmail.com",
  "hobby": ["puzzles","swimming"]
}
```







### 참고

- 아스키코드로 변환해주는 사이트! : http://artii.herokuapp.com/
- html 공식 공부 사이트 : https://www.w3schools.com/html/default.asp