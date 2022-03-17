# [Django 공부 부분]

**장고 생활코딩 강의 영상 사이트: https://www.youtube.com/watch?v=pbKhn2ten9I&list=PLuHgQVnccGMDLp4GH-rgQhVKqqZawlNwG**
```
<파이참에서>
venv\Scripts\activate 입력해서 venv 켜고,
python manage.py runserver 입력해서 서버를 켜자. (만약에 8000번 포트가 아닌 다른 포트로 접속하고싶다면, 코드 뒤에 8888과 같은 다른 포트번호를 적어주면 된다. 예를들어 python manage.py runserver 8888)

myproject_settings.py 파일은, 프로젝트를 운영하는데 필요한 여러가지 설정들이 들어가있다.
myproject_urls.py 파일은, 사용자가 접속하는 그 path에 따라서 그 접속, 요청을 어떻게 누가 처리할것인가를 지정(라우팅)하는 파일이다.
manage.py 파일은, 프로젝트를 진행하는데 있어서 필요한 여러가지 기능이 들어가있는 유틸리티(실용적이고 유용한) 파일이다.

```
