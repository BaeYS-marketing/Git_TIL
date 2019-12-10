# Github 업로드 하기

## 초기 설정

### 1) `git int` 

> bash에서 git과 연동될 파일 설정 
>
> 초기 설정으로 한번 연결되면 계속 연결되어 있다.
>
> *삭제 : 해당 파일에서  `rm -r .git` 명령어로 .git 숨김폴더 삭제하면 된다.



### 2) `git remote`

> **local 폴더**와   **github의 repository** 을 연결



### 3) git bash에서 로그인 하기

```bash
$ git config --global user.email " "
$ git config --global user.name " "
```



___

___



## `PUSH` : bash에서 github로 업로드

 ### 1) `git add` :  Staging Area올려놓기

```bash
$ git add #파일명#
```



### 2) `git commit` : 스냅샷 커밋

```bash
$ git commit -m "커밋 메세지"
```



### 3) `git push` : github 업로드

- staging area에 올려진 파일과 commit 된 파일을 업로드 시킨다. 

```bash
$ git push origin master
```





---

---



# `git PULL` : bash로 github 파일 내려받기

- github의 repository안 파일을 그대로 받아오는 명령어 

```bash
$ git pull origin master
```





---

---

# `git clone` : github의 repository 그대로 복사

- github에서 repository자체를 그대로 복사하는 명령어 
- 자동으로 `git int` 설정 완료 
- 그러나!! repository 접근성에 따라 권한이 다르다.
  - 접근 허용된 repository이면 허용된 주소로 push $ pull 가능
  - 접근 허용되지 않으면 pull만 가능

```bash
$ git clone "URL주소"
```

