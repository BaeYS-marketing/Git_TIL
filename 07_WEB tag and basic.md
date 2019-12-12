# visual code _WEB : 편의 프로그램 설치

>- css peeper : 폰트 및 컬러, 사이즈 확인 
>- json viewer
>- open in browser : 코딩 제대로 되고 있는지 바로 확인
>- html snippets : html을 자동 완성하는 플러그인

[참조 사이트]([https://kamang-it.tistory.com/entry/VisualStudioCode%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8Open-In-Browser-vscode%EC%97%90%EC%84%9C-html%EC%9D%84-%EB%B0%94%EB%A1%9C-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90%EC%84%9C-%ED%99%95%EC%9D%B8%ED%95%98%EC%9E%90?category=771113](https://kamang-it.tistory.com/entry/VisualStudioCode플러그인Open-In-Browser-vscode에서-html을-바로-브라우저에서-확인하자?category=771113)) 



편의 프로그램 설치 후 단축키

>- `! + tab` : html 기본 포맷 자동완성
>
>- `shift + alt b` : 코드창에서 웹 구현





# HTML 태그 

### form : 입력 /전송 태그 

>- 웹 페이지의 정보를 다른 페이지로 전송하는 태그
>
>- 단순 텍스트의 내용만 보여 주는 페이지에는 필요없다.  서로 데이터를 주고 받는 웹 페이지일 경우 사용  
>
>- l **action :** 폼 내부에 데이터를 보내는 목적지 URL 을 지정한다.
>
>  l **actocomplete :** HTML5 에 추가되었으며 양식의 자동완성을 지정한다.
>
>  l **enctype :** 넘기는 Content 타입을 지정하는데 주로 파일을 넘길 때 많이 사용한다. 
>
>  ​                            type 은 “multipart/form-data” 로 지정해서 사용한다.
>
>  l **method :** 폼을 서버로 전송하는 http 방식을 지정한다. POST 와 GET 이 있다.
>
>  l **name :** 폼을 식별하기 위한 이름을 지정한다.
>
>  l **target :** action 에서 지정한 스크립트 파일이 현재나 다른 위치에서 열리도록 지정한다.
>
>  l **accept-charset :** 폼 전송에 사용될 문자 인코딩을 지정한다.
>
>[참조사이트](https://mainia.tistory.com/4246)



### 목록과 관련된 태그

>- `ul` 태그 : Unoerdered List 의 약자로 순서가 없는 목록이다.
>
>  ​				글머리 기호를 붙혀서 목록을 만드는 형식이다.
>
> 
>
>- `ol` 태그 : Ordered List 의 약자로 순서가 있는 목록이다.
>
>  ​				번호 형식으로 순서를 매겨 목록을 만드는 형식이다.
>
> 
>
>- `dl` 태그 : Difinition List 의 약자로 정의 목록을 만드는 형식이다.
>
>  ​				어떤 용어의 정의를 나열하는 형식이다.
>
> 
>
>- `li` 태그 : List Item 의 약자로 ul 태그와 ol 태그의 내부에서 사용되는 태그이다.
>
>  ​			목록의 내용이 되는 실질적인 태그이다.
>
>  ​			들여쓰기 및 줄바꿈 기능이 있고 type 속성으로 다양한 기호를 사용할 수 있다.
>
>[참조사이트](https://cofs.tistory.com/124)



### link 

>- 외부의 문서를 연결시키는 태그입니다.  
>- 주로 css파일 같은 스타일시트 파일을 연결하거나, 
>- 웹 폰트를 사용할 때 폰트가 있는 주소로 연결시킬 수도 있습니다.



link 태그와 함께 사용할 수 있는 속성

1. **href**  : 연결할 곳의 주소 (절대주소, 상대주소 모두 가능)
2.  **rel** : 현재문서와 연결문서의 관계 표시

```html
<head>

<link rel='stylesheet' type='text/css' href='http://fonts.googleapis.com/css?family=Open+Sans:400,300'  />

</head>
```

> rel의 속성값
>  
>
> stylesheet : 스타일시트로 연결할 때
>
> alternate : 문서의 대안 버전(프린트나 번역 사이트)으로 연결할 때
> <link rel="alternate" type="application/atom+xml" href="/print/atom">
>
>  
>
> author: 저작자로 연결할 때
> help: 도움말로 연결할 때
> license: 문서의 저작권 정보로 연결할 때
> search: 검색 도구로 연결할 때 

​	3. **type** :  연결 문서의 MIME 유형 (href 속성이 설정될 때만 사용 함)

​			cf) MIME(Multipurpose Internet Mail Extensions)은 원래 전자 메일 전송을 위한 인터넷 표준이었으나                   				현재는 웹에서 내용 유형(content type)을 말할 때 자주 쓰임

[참조사이트](https://aboooks.tistory.com/147)



### **id** 

>스타일을 지정할 때 한 가지만 지정해서 쓰는 이름이고      **표기방식 : `#id_name`**
>
>하나의 문서에 고유한 id 하나밖에 쓸 수 없습니다.



#### **class** 

> 그룹으로 묶어서 스타일을 지정할 때 쓰는 이름이에요.     **표기방식은 :    `.class`**



#### span

>  문자열에서  원하는 부분만 선택해서 시각적 효과를 줄 수 있습니다.

```html
<span class="welcome">지구별</span> 홈페이지에 오신 것을 환영합니다.
```



#### div

>  하나 이상의 태그를 묶어서 스타일을 지정할 때 사용합니다.



#`.css`확장자 저장파일

```css
.am {
background:green;
}
.pm {
background:yellow;
}
```

#`html`저장 파일

```html

 <html>
 <head>
 <title>지구별 안내서</title>
 <link rel="stylesheet" type="text/css" href="test.css" />

 </head>
 </head>
<body>


<div class="am">
<p>9시 </p>
<p>10시 </p>
<p>11시 </p>
<p>12시 </p>
</div>


<div class="pm">
<p>13시 </p>
<p>14시 </p>
<p>15시 </p>
<p>16시 </p>
</div>


</body>
</html>
```





## style

> 스타일 태그를 사용하여 **웹문서의 디자인을 변경**할 수 있습니다.

[참조사이트](https://androidtest.tistory.com/73)

**스타일의 형식**

**선택자{ 속성:값;}**

> - **`p{color:black;}`** 형태로 사용합니다. 
>
> -  **`p,h1{color:black;}`**    :선택자는 한번에 여러개도 적용 가능합니다.



모든 선택자에 적용하고 싶을경우 ***{속성:값;}** 을 사용하시면 됩니다.

특정 태그가 아닌 특정 클래스이름에 스타일을 적용하고 싶을 경우 **`.class_name`{속성:값};**

특정 id 이름에 스타일을 적용하고 싶을 경우 **`#id_name`{속성:값};**



스타일은 **헤드태그** 사이에 넣어도되고 **css파일**을 따로 만들어 적용하거나 **태그에 직접** 하는 방법들이있습니다.



---



#### a

> - **문서를 연결**
> - 속성 : **href,   title,    target **



[참조사이트](https://aboooks.tistory.com/87)



#**`href`속성**

- 절대URL 

```html
<a href="http://aboooks.tistory.com">지구별 안내서</a>
```

- 상대URL

```html
<a href="home/right.htm">오른쪽 페이지로 이동</a>   <!--home폴더 안 riht.html-->
```

- id를 이용한 URL (특히 같은 문서 내에서 가리키는 id)

```html
<div id="top">ID를 이용한 URL</div>   <!--같은 문서 내 어딘가 ID를 지정함-->>
<a herf="#top">해당 아이디(#top)으로 이동</a>       
```



#**`title` 속성**

- 해당 링크에 마우스를 갖다 대면 link에 대한 설명이 나옵니다.

```html
 <a href="http://aboooks.tistory.com/"  title="my homepage">지구별 안내서</a>
```



#**`target` 속성**

- 링크를 클릭 할 때 창을 어떻게 열지 결정합니다

> **_self** 연결 문서를 클릭한 창에서 엶(기본값)
>
> **_blank** 연결 문서를 새 창에서 엶
> **_parent** 부모(상위 레벨) 창에서 엶(부모가 없으면 _self처럼 표시함)
> **\_top** 가장 상위 창에서 엶(즉 프레임을 무시하며, 전체 브라우저 창에서)(부모가 없으면 _self처럼 표시됨)
> **frame name** 지정된 프레임 안에 염.

```html
<a href=http://aboooks.tistory.com" target="_blank">지구별 안내서 바로가기</a>
```



`<a>`태그는 문자뿐 아니라,  1) `img,`  2) `<div>` 등도 링크를 걸 수 있습니다.

```html
<a href="http://aboooks.tistory.com"><img src="main.png" /></a>
<a href="http://aboooks.tistory.com"><div id="a">애국가</div></a> 
```







---







# HTML과 CSS의 차이 

[참조사이트](https://aboooks.tistory.com/49)

## css

> - CSS는 Cascading Style Sheets 약자      cf *스타일시트 이다. `stylesheet`
>
> - HTML, XHTML, XML 같은 문서의 스타일를 꾸밀 때 사용하는 **"스타일 시트 언어"** 입니다.



HTML로 문서의 뼈대를 만들면

 CSS는 이 문서의 화장을 맡고 있는 셈인데요.  

 

글꼴이나, 배경색, 너비와 높이, 위치 등을 지정하거나,

 웹 브라우저, 스크린 크기, 장치에 따라서 화면을 다르게 표시될 수 있도록 지정할 수도 있습니다.

 

CSS는 1996는 12월 W3C(웹 문서 표준을 만드는 기관)가 도입 했는데

그 전엔 HTML언어 하나로 문서의 뼈대도 만들고, 꾸밈도 같이 했습니다.

그러다 보니 HTML 문서를 수정할 때 모든 문서를 하나씩 수정해야 하는 번거로움이 있었습니다..

 

CSS는 문서의 내용(content)과 표현(presentation)을 분리하여

 CSS 파일 하나만 수정하면 스타일에 해당하는 HTML 문서가 한번에 수정되는 엄청난 장점이 있습니다.



### 스타일을 꾸미는 법

> 1. 속성처럼 style 적용  [ inline ]                               ~ 비선호 
> 2. style tag를 사용        [ embeded]                           ~ ..
> 3. css 파일을 별도로 만들어 html 문서에 연결.  [ external link ]      ~선호 



- 1번 방식

```html

 <html>
 <head>
 <title>지구별 안내서</title>
 </head>
 <body>

<h1 style="color:blue; text-align:center;">   

CSS 첫번째 강좌</h1>  

 </body>
 </html>
```



- 2번 방식

```html
<html>
 <head>
 <title>지구별 안내서</title>
 <style type="text/css">
    h1 {

color: blue;

text-align:center;

}
  </style>

 </head>
 <body>

 <h1>CSS 첫번째 강좌 </h1> 

 </body>
 </html>
```



- 3번 방식

```html
<html>
 <head>
 <title>지구별 안내서</title>
 <link rel="stylesheet" type="text/css" href="test.css" />

 </head>
 <body>

  css 첫번째 강좌
 </body>
 </html>


css파일 따로 있다.
보통 css.css로 저장 

  h1 {
color: blue;
text-align:center;
}

```



### css 작성법이 다르다는 점을 보고 가자!

- css 작성법

```css
selector  {property: value;}

   h1 {
color: blue;
text-align:center;
}
```

>- html 작성 방법과 다르다는 점 유의해주세요!
>
>  열고 닫기는 { } 를 사용하며, 하나의 속성값이 끝날 때마다 세미콜론 ; 을 씁니다.
>
> 
>
>- 중괄호를 연 후 태그를 밑에 쓰는 것은, 코드 작성 시 오류를 줄이기 위해서입니다.
>
>  아래 처럼 작성해도 틀린 것은 아닙니다
>
>  
>
>- HTML   : <태그 속성="속성값">내용 </태그>
>
>  ```html
>  <p align="center">내용 </p>
>  ```
>
>  css  : 선택자 {속성:속성값; 속성: 속성값;}
>
>  ```css
>  p {
>  text-aglign:center; color: red;
>  }
>  ```
>
>     