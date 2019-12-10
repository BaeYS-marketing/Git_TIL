# FORK

> 다른 사람의 repository를 그대로
>
> 내 계정 repositroy로 복사하기 



## 2 `pull request` 

- contributor로 권한을 부여받지 않으면
- Fork로 받더라도, push할 수 있는 권한이 없다.
- `pull request`는 오픈소스를 받아서(pull)  push를 요청

> 포크 계정에서 `pull request`는 과정이 복잡하니,
>
> 내 계정에서 `new pull request`로 쉽게 요청할 수 있다.





#  Github와 bash의 충돌

## case1) Github와 Local에서 서로 다른 파일이 존재

> Github에서는 trash.txt 파일이 존재하고,  local에서는 junk.txt 파일이 존재한다.
>
> local에서 junk.txt가 trash.txt 파일로 착각하여 `git pull` 명령어를 수행시키면,
>
> local은 junk.txt 와 trash.txt 파일 2개가 생성된다.

#### 이런 경우의 모두 남기는 방식으로 충돌은 자동해결된다.



## case2) Github와 Local에서 같은 파일, 다른 내용

>GIthub와 Local에 모두 dump.txt 파일이 존재하지만 
>
>Github에서는 ABC로 내용이 저장되어 있고, Local에서는 DEF로 내용이 저장되어 있다.



#### 이런 경우의 PULL은 Local의 한 파일에 ABC, DEF 두 가지가 충돌되며 에러발생.

- 두 가지 내용을 어떻게 저장할 것인지 선택해야 한다.

  - visual studio code에서 선택

    ```bash
    $ code .
    ```

  - 메모장에서 선택해서 저장

    - `<<HEAD>> `와 `hash 태그` 지우고 남기고 싶은 `content`만 표시한 후 저장 



- 이후에 `git add`와 `git commit -m " "` `git push` 단계를 거쳐서 github에 업로드



## stash

## checkout

git checkout  <16진수ID> 

git checkout master 





그 외 기억하고 싶은 명령어 

* `git log #--online`  :commit들의 역사 

- q : 나가기   ,  qw : 저장하고 나가기
- git diff : 수정사항 보기
- cat 파일명 : 내용출력