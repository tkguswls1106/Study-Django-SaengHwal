# [Django 공부 부분]

**장고 생활코딩 강의 영상 사이트: https://www.youtube.com/watch?v=pbKhn2ten9I&list=PLuHgQVnccGMDLp4GH-rgQhVKqqZawlNwG**
```
<파이참에서>
venv\Scripts\activate 입력해서 venv 켜고,
python manage.py runserver 입력해서 서버를 켜자. (만약에 8000번 포트가 아닌 다른 포트로 접속하고싶다면, 코드 뒤에 8888과 같은 다른 포트번호를 적어주면 된다. 예를들어 python manage.py runserver 8888)

<파이참에서>
python manage.py startapp myapp 입력해서 myapp이라는 이름의 웹앱을 생성한다.

myproject_settings.py 파일은, 프로젝트를 운영하는데 필요한 여러가지 설정들이 들어가있다.
myproject_urls.py 파일은, 사용자가 접속하는 그 path에 따라서 그 접속, 요청을 어떻게 누가 처리할것인가를 지정(라우팅)하는 파일이다.
manage.py 파일은, 프로젝트를 진행하는데 있어서 필요한 여러가지 기능이 들어가있는 유틸리티(실용적이고 유용한) 파일이다.

프로젝트 안에는 여러 웹앱들이 있고, 그 각 웹앱마다 urls.py 가 있다.
그리고 웹앱안에는 view가 있고, 그 안에는 여러 함수들(def)을 만들어 애플리케이션의 구체적인 구현들을 해나간다.

프로그램이 돌아가는 과정 흐름 설명:
사용자가 접속함.
-> 여러 경로로 들어올것인데, 그 각각의 경로를 누구에게 위임할 것인가를 프로젝트(myproject) 안의 urls.py 파일에 적혀있는대로 적당한 웹앱(myapp)으로 위임이 된다. { 사용자 접속 -> myproject -> myproject_urls.py -> myapp }
-> 그러면 웹앱 안에 있는 urls.py 에서도 작성된 코드에 따라 적당한 view의 적당한 함수로 위임이 된다. { myapp_urls.py -> myapp_views.py -> def }
-> 그 과정에서 구체적인 작업들을 하게될텐데, 그것이 아주 많은 경우에는 데이터베이스를 사용하게 된다.
-> 해당 데이터베이스는 우리가 직접 접속하는것이 아니라, 장고 안의 model이라는 굉장히 편리한 수단을 통해 데이터베이스를 사용하게 된다.
-> 그렇게 데이터베이스에 있는 정보를 받아서 클라이언트에게 응답을 해준다.
-> 그 결과로 최종적으로 html, json, xml 등등의 형태의 데이터를 만들어서 사용자에게 보내주게 된다.

라우트는 경로라는 것으로, 웹앱에서 경로라는 것은, 사용자가 접속한 각각의 사이트 등등의 경로를 누가 처리할 것인가를 지정하는 것이다.
장고에서는 프로젝트 폴더 안에있는 urls.py 가 가장 큰틀에 라우팅을 하고, 저것을 적당한 웹앱에 위임을 해주면, 그 웹앱이 view 안에 있는 특정 함수로 위임해서 그 함수가 이 작업을 처리한다.

기타 주의할 사항 (내가 2022-06-02에 찾아낸 것임):
이미 static 폴더에 들어가있는 js 등등의 파일에, {% load static %} 적지말자. 정상 실행이 안된다.

기타 나중에 확인해볼 사항 (내가 2022-06-02에 생각한 것임):
context 변수의 렌더링은 특정 html파일로 해줬는데, 만약 해당 html파일에서 static 폴더내에 위치한 특정 js 파일을 불러온다면,
해당 js파일에는 {{% for %}} 같은 장고 템플릿 코드를 사용해도 되는지 궁금하다.

------------------------------------- 5강 코드 및 중요 내용 정리 -------------------------------------
{ 사용자 접속 -> myproject -> myproject_urls.py -> path가 /admin/ 아닌것 확인 ->  path가 비어있으므로 path('', include('myapp.urls')) 사용
-> myapp 이동 후 myapp_urls.py -> path가 비어있다면 path('', views.index) 사용 -> myapp_views.py -> def index(request) 사용
-> HttpResponse('Welcome!')으로 사이트 화면에 Welcome!이 출력되도록 클라이언트에게 전달 -> 이로써 라우팅 완료 } 

<myproject_urls.py>
path('admin/', admin.site.urls),
path('', include('myapp.urls'))  # myapp의 urls.py를 사용해라.
                                       # 과정을 설명하자면, 사용자가 접속했을때, 'admin/'이 아닌 다른 경로로 접속을 하면
                                       # 그 접속을 myapp의 urls.py로 위임해라 라는 것이다.

<myapp_urls.py>
path('', views.index)  # 사용자가 경로를 지정하지 않고 접속했을때 myapp의 views.py의 index라는 함수로 위임하기위해서 두번째 파라미터값을 views.index로 준다.

<myapp_views.py>
# views에다가 클라이언트로 정보를 전송하기위한 함수를 작성한다. 먼저 index 함수를 작성한다.
def index(request):  # 이 함수는 첫번째 파라미터의 인자로 요청과 관련된 여러가지 정보가 들어오도록 약속되어있는 객체를 전달해주도록 되어있다.
                          # => request 라는 이름의 파라미터를 적어준다. 사실 뭘적든 상관은 없지만 관습적으로 request라고 적어주는것을 추천한다.
    return HttpResponse()  # http를 이용해서 응답을 하겠다는 의미의 객체이다.
		          # 그리고 그 인자로 전송하고싶은 값을 그 안에 적는다.

<이로써 최종 과정 정리>
예를들어 사용자가 http://127.0.0.1:8000/read/shj/ 로 접속을 했다면,
해당 path는 'admin/'이 아닌 다른 경로인 /read/shj/ 이므로, 접속을 하면 장고는 myproject_urls.py의 path('', include('myapp.urls')) 코드를 바라보게 된다.
그다음에 myapp_urls.py로 위임하게 되고, myapp_urls.py는 path('read/<id>/', views.read) 코드로 인해 myapp_views.py로 위임을 하게된다.
결국 myapp_views.py의 read 함수를 불러오게되어 'Read!'+id 인 Read!shj 를 웹사이트 화면에 출력하여 클라이언트에게 보내주게 된다.
이렇게 모든 과정이 라우팅이었던 것이다.
-------------------------------------------------------------------------------------------------

웹 서버(Web Server): apache, nginx, llS 등등을 사용하며, 1.html 같은 파일을 미리 만들어놔야한다는 단점이 있다. 그래서 정적(static)이다.
웹 어플리케이션 서버(Web Application Server): django, flask, php, jsp, ROL 등등을 사용하며 변경 사항이 있을시 전체가 공장이 돌아가듯이 한번에 바뀌어 동적(dynamic)이라는것이 장점이다.

HttpResponse(값) 는 다른 함수에서 값을 리턴받아 return HttpResponse(다른 함수의 리턴값) 으로 사용하게 될 경우, 그 다른 함수의 리턴값 안의 문자열을 html코드로 해석하여 출력해준다.

form 태그와 method="get" 와 method="post" 에 대한 설명은 html_css_js md 파일에 적어놓았으니 참고하자.

from django.shortcuts import redirect 하고나서
redirect() 란, 리다이렉트(리디렉트)란 말 그대로 re(다시) + 지시하다(direct) 다시 지시하는 것을 말한다.
예를 들어 브라우저가 www.naver.com/blogA URL을 웹 서버에 요청했다고 하자.
그러면 서버는 HTTP 응답 메시지를 통해 "www.naver.com/blogB 로 다시 요청해봐!~" 라고 브라우저에게 다른 URL(길, 방향) 을 지시할 수 있는 것을 리다이렉트라 한다.
이는 인터넷에서 가져온 정보이며, https://webstone.tistory.com/65 사이트에 적혀있다.

예를들어 if topic['id'] == int(id): 이런거 쓸때  if topic['id'] == id: 이런식으로 자료형이 틀린 코드가 있을수 있으니 이부분 주의하자!

우리는 정보를 메모리에 보관하고있기때문에, 웹앱이 재실행될때마다 데이터가 리셋된다.
예를들어 홈페이지 내에서 수정을 하거나 해도 웹앱을 재실행하여 서버를 다시 켜서 들어가보면 작성된 코드였던 그 초기상태의 홈페이지로 다시 돌아간다는 것이다.
그래서 이 정보가 리셋되지않고 영구적으로 보관할수 있게하고싶다면, 데이터베이스를 사용한다.
데이터베이스로 정보를 영구적으로 보관할 수 있을뿐만아니라, 엄청난 속도로 필요한 정보를 검색할수도 있다.
장고에는 모델(model)이라는 기능이 내장되어있는데, 이를 이용하면 데이터베이스를 매우 쉽게 사용할 수 있다.

장고에서 파일 하나 안에 html 코드와 파이썬 코드가 뒤섞여있어 가독성이 떨어진다면, Template engine 이란것을 공부하여 사용해보자.
별도의 html 파일을 만들고, 그 안에 변경되어야하는 부분에만 약속된 문법에 맞게 코드를 추가해주면된다.
이렇게하면 html 코드와 파이썬 코드를 분리하여, 더욱 편리하게 코딩작업이 가능해진다.

```
