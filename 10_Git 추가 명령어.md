# git 추가 명령어



## git bash 사용자 전환

```bash
$ git credential reject
protocol=https
host=github.com
```

- 이후 다시 `$ git config --global user.email / user.name`  입력



## github repository delete

```bash
$ git rm -r --cached <파일명>  //원격저장소 파일 삭제, local은 rm -rf로 삭제
```

```bash
$ git commit -m ""
$ git push origin master
```





## caution when git clone

> 1. `git clone`을 통해서 받은 파일을 다른 경로가 설정된(`git remote`) 폴더로 이동시키면
>
>    `git remote -rm .git`을 우선적으로 삭제해야 한다.
>
> 2. 그  이후에 폴더명을 바꾸었다가 다시 설정하면 reset 완료





## rename or delete 리모트저장소

-  `rename`

```bash
$ git remote rename <파일명> <바꿀파일명>
```



- `delete`

```bash
$ git remote rm <리모트저장소>
```

## `git push -f origin master` : 기존 레퍼지토리 초기화 후 psuh 
>failed to push some refs to~,Updates were rejected because the remote contains work that you do not have locally 
- 해결방법 : pull&psuh
