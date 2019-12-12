

# 가상환경

<가상환경>

> - default : 패키지  등 윈도우 환경 전역에서 접근이 가능하다.
>
> - venv _ virtual environment :  전역접근을 `환경변수 / path` 의 변경을 통해 분리 
>
> - VM 프로그램과는 다르다. 완전한 분리는 아니여서 파일설치 등은 같이 영향을 받는다.
>
> ex) request 패키지 버전에 따라 조절



- 가상환경 만들기

  ```bash
  $ python -m venv 가상환경명
  ```

1. (venv : virtual environment)

2. `ls`로 가상환경 만들어 졌는지 확인



- 가상환경 실행시키기(들어가기)

```bash
$ source 가상환경명/Scripts/activate
```



- 가상환경 실행명령어 `alias`로 만들기

```bash
$ vi ~/.bashrc
```

> - bash창이 바뀐다. 
> - `i`    (쓰기모드)로 변경 
> - `alias activate="source venv/Scripts/acitvate"`   
>   - 빈칸있으면 안된다.
>   - `source 가상환경명/Scripts/activate` 명령어의 `alias`_별명 붙이는 명령어 
> - `wq` : 저장 후 나간다.





- 배시 재가동 

```bash
$ source ~./bashrc
```





- 단축 가상환경 실행 명령어 키인

```bash
$ activate
```

> `alias`(단축시킨 별명 코드로) 가상환경 시행
>
> *단 bash창에서 가상환경 파일이 있는 곳에서 시행해야 한다. 



- 가상환경 나가기

  ```bash
  $ deactivate
  ```

  

#에러사항 

```bash
student@M1601 MINGW64 ~/TIL (master)
$ activate
bash: venv/Scripts/acitvate: No such file or directory

student@M1601 MINGW64 ~/TIL (master)
$ ls
 00_markdown_basic.md   homework.txt     quiz.txt    venv/
 01_TIL.md              new.md           README.md  '마크다운 문법.md'
 02_push_pull.md        python_basics/   TIL/

student@M1601 MINGW64 ~/TIL (master)
$ vim ~/.bash_profile

student@M1601 MINGW64 ~/TIL (master)
$ source ~/.bash_profile

student@M1601 MINGW64 ~/TIL (master)
$ activate
(venv)
student@M1601 MINGW64 ~/TIL (master)
$ vi .gitignore
(venv)
student@M1601 MINGW64 ~/TIL (master)
$ ls -a
 ./           00_markdown_basic.md   new.md           TIL/
 ../          01_TIL.md              python_basics/   venv/
 .git/        02_push_pull.md        quiz.txt        '마크다운 문법.md'
 .gitignore   homework.txt           README.md
(venv)
student@M1601 MINGW64 ~/TIL (master)
$ activate
(venv)
student@M1601 MINGW64 ~/TIL (master)
$ which python
/c/Users/student/TIL/\Users\student\TIL\venv/Scripts/python
(venv)
student@M1601 MINGW64 ~/TIL (master)
$ deactivate

```





----

가상환경에서 버전이 다른 여러 패키지를 깔았다

이 상태로 깃허브로 올리면 안돼.
패키지 여기서 다운받았는데 여기서 올리면 용량이 너무 크다!



패키지 설치한 거 빼주는 것 !! 뭐 뺴야할지 알려주는 웹서비스 이용

## http://gitignore.io/

`Python` `Flask` `venv` 엔터 후 모든 목록 복사  _ 이 3가지와 관련된 것은 알아서 제거할 목록 알려준다. 

bash창에서

```bash
$ vi .gitignore
```



여기서 목록 복사한거 붙여넣기 후 
`wq`

`ls`에서 `.gitignore` 파일이 있으면 된다.



> gitignore이 있는 파일부터 하부폴더 까지 다 적용 _  : 최상단에 만들어주면 된다.



여러질문
가상환경은 환경변수/패스가 따로 지정이 되는 것
파이썬에는 영향을 미치지 파일에는 영향을 미치지 않는다.





가상환경에서 버전 뭐뭐 있는지 알려주기

```bash
$ pip freeze > requirements.txt
```



그 requirements 목록 한번에 설치해주기 

```bash
$ pip install -r requirements.txt
```



