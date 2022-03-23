from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index),  # 사용자가 경로를 지정하지 않고 접속했을때 myapp의 views.py의 index라는 함수로 위임하기위해서 두번째 파라미터값을 views.index로 준다.
    path('create/', views.create),
    path('read/<id>/', views.read)  # <id>는 꺽새<>를 이용해서 바뀔수있는 값이 올수도 있다는 의미로 적은것이다.
                                    # myapp_views.py의 read함수에도 id를 추가해주자.
                                    # 이로써 예를들어 path를 /read/shj/ 라고 입력하면 Read!shj 라고 출력된다.
]
# 이렇게 각각의 경로로 접속을 했을때 views로 전달을 한다.
