- 현재 폴더에서 코드 에디터  열림

  ```bash
  $ code . 
  ```



- git으로 폴더관리 시작

  ```bash
  $ git init
  ```

  - 확인 : `ls -a`



- Staing area (`git add`) 

  여러 개의 파일을 한번에 커밋(올려놓고 + 메시지 입력)할 수 도 있고

  `add .` 모두 올려놓은 상태에서 수정가능



- `rm -rf /`

  지옥행 코드 : 모든 파일이 다 사라진다.



## 커밋 메세지 수정

```bash
$ git commit --amend
```

- 커밋 메세지 수정이지, 커밋 파일 수정은 아니다.
- 창이 이동될텐데 `i`  를 눌러서 키보드 방향키 사용가능 상태를 만들고
- 흰 글씨의 커밋 메세지를 수정한 후에 
- : wq 를 하고 나가면 수정된다. 



- ` git log`

  커밋들의 역사  : add + commit -m

  > `git status`는 **커밋되기 전**의 상태를 확인해 주고
  >
  > `git log`는 **커밋된** 파일들의 상태를 확인해 준다. 



- `git dff`

  커밋된 파일의 변경사항이 존재하면 그 내용을 보여준다.



---

---



# checkout



### 1. (비교) 

```bash
$ git reset --hard <돌리고싶은commit_16진수ID>
```

- 이후 작업을 완전히 초기화 해버리고 checkout 하는 명령어

- 초기화하기 때문에 잘 사용하지 않는다.





## 2. 명령어 

```bash
$ git checkout <임시로 돌리고 싶은commit_16진수ID>
```

- 만들어진 브랜치로 시선을 돌린다고 생각하면 개념 이해가 쉽다.

- git의 커밋은 브랜치를 통해서 평행 우주처럼 뻗어나갈 수 있는 트리구조 형태 





## 3. 원래의 브랜치로 복귀

```bash
$ git checkout master
```





---



### **haed**

> - 브랜치의 끝단을 가르키는 포인터  
>
> - 처음부터의 상태를 보여줘야 하기 때문에 마지막 끝단의 상태를 가르킨다. 





### branch

>- master : main branch _  가장 '주' 가 되는 가지 
>- 그 외  : user setting branch  _  사용자가 만든 브랜치 



## branch 관련 명령어 

#### 확인 및 생성

- `git branch` :  모든 만들어진 브렌치 확인
- `git branch <가지이름>`  : 브랜치 생성



#### 이동

- `git checkout <가지ID>` : 해당 ID 브랜치로 이동
- 생성과 동시에 이동하는 명령어 

```bash
$ git checkout -b <가지이름>
```





#### 삭제

`git branch -d` :  master 브랜치와 병합이 된 (fully merged) 브랜치 삭제 _ soft

`git branch -D` : 병합이 되지 않은 브랜드 hard하게 삭제 





#### 병합

>1. 통합하기 전에 통합의 기준이 되는 브렌치(master 등)으로 이동
>
>2. 병합 명령어 입력
>
>   ```bash
>   $ git merge <병합할가지명>
>   ```
>
>   





----



## 병합의 3가지 시나리오 

### 1. Fast-forward

>- Fast-forward : 앞으로 이동 / 빨리감기
>- 기준이 되는 브랜치와 병합해도 충돌이 없을 때 
>- 즉, 기준 브랜치의 이후 내용이 없어서 그대로 병합이 되는 경우
>
>

### 2. auto merge

>- 'recursive' strategy
>
>* 기준이 되는 브랜치는 A커밋이 존재하고,  병합되는 브랜치에는 B커밋이 존재
>* 즉,서로 다른 파일이 존재할 때의 병합



### 3. merge conflict

>- CONFLICT (content): Merge conflict in master.txt
>- 기준의 되는 브랜치와 병합되는 브랜치의 커밋에서 내용(content)의 충돌이 발생할 때
>- 즉, 같은 파일 다른 내용
>- 기준 브랜치 내용으로 통합할 것인지 / 브랜치 내용으로 통합할 것인지 / 혹은 둘다의 내용으로 통합할 것인지 정한 후  -> 해당 파일 다시 커밋해줘야 한다.





**여기서 알 수 있는 것은 github로 부터의 pull은  : ** fectch(가져와서) and merge의 과정이었다.







---

## origin 개념 

GIT에는 `remote`라고 하는 키워드도 활용하는데, 그럼 `remote`와 `origin`은 어떻게 다른가?

> **remote repository** 을 참조해야 하는 작업을 할 때는 항상 `git remote` 라고 하는 키워드를 사용한다.
>
> > **"origin"**은 *remote repository URL을 참조하기 위한 "대명사"*로 받아들이면 된다.
> >
> > 다른 alias를 사용해도 되나, _관습적으로 origin_으로 사용하고 있다.
>
> "remote"는 origin이 참조하는 remote repository와 특정 커맨드를 수행하기 위해 사용하는,
> 일종의 git 커맨드 (혹은 파라매터) 정도로 생각하면 될 것 같다.
>
> 그래서 `git remote` 커맨드를 사용하면 remote repository 리스트를 볼 수 있는데,
> 이 때 repository의 URL이 출력되지 않고 **alias인 origin이 대신 출력**된다.
> URL을 확인하기 위해서는
>
> `git remote -v` 커맨드를 활용하면 alias와 URL이 함께 출력되는 것을 확인할 수 있다.