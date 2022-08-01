# Today I Learned

## vscode에서 git연동
---

### ⭐ add는 일단 버전관리 할 폴더로 저장만하는 것이고 그 다음에 commit을 해줘야함.




### 💡vscode
git init : 원하는 폴더 위치로 들어가서 저장소로 설정

git status : 현재 git으로 관리되고 있는 파일들의 상태를 알 수 있음

git add. : 추적 되지 않은 모든 파일과 추적 하고 있는 파일 중 수정 된 파일을 모두 Staging Area에 올림

git폴더에 버전관리하고싶은 폴더를 추가하려면 git add해야함
그 후에 다시 status해보면 newfile로 등록된 걸 확인할 수 있음(원래는 no connits yet에 표시됨)

git config --global user.name "~~~" : 깃허브에 가입한 유저네임 입력

git config --global user.email "~~~@gmail.com" : 깃허브에 가입한 이메일 입력

git commit -m “넣고싶은 메시지” : 이름과 메일설정이 완료해야 커밋을 진행할 수 있음

git log : commit의 history를 볼 수 있음
git diff : 수정된 내용을 보여줌

git  remote add origin “repo url”
git push origin master 토큰입력까지하면 연동 완료


### 💡git bash

git clone “repo url” : 새로운 폴더 만들고 git bash이용하여 이 명령문 사용하면 git이랑 연동!


### 💡git 6단계
git init  
git add .  
git commit -m ""  
github에서 repo만들기  
git remote add origin "github_repo_url"  
git push origin master  


#### 만약 잘 안되면 폴더 안에있는 .git 폴더 삭제 한후에 다시해보기(제일 간단한 방법) 


### 내용 수정 후 push 
git pull origin master : 내용 먼저 불러오기  
내용수정 후 저장  
git status : 상태확인(빨간 글)  
git add . : 수정사항 저장    
git status : 상태확인(녹색 글)  
git commit -m "" :커밋  
git log : commit기록 확인, q눌러서 탈출  
git push origin master : 수정사항 업로드 


### github username 변경 후 repo 재연결  
bash 창에서  
git remote -v : 현재 주소 확인  
git remote set-url origin 바뀐주소 
git remote -v : 바뀐 주소로 잘 변경되었는지 확인

