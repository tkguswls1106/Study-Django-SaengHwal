from django.shortcuts import render, HttpResponse
import random

# Create your views here.

# views에다가 클라이언트로 정보를 전송하기위한 함수를 작성한다. 먼저 index 함수를 작성한다.
def index(request):  # 이 함수는 첫번째 파라미터의 인자로 요청과 관련된 여러가지 정보가 들어오도록 약속되어있는 객체를 전달해주도록 되어있다.
                     # => request 라는 이름의 파라미터를 적어준다. 사실 뭘적든 상관은 없지만 관습적으로 request라고 적어주는것을 추천한다.
    return HttpResponse('<h1>Random</h1>'+str(random.random()))  # HttpResponse()는 http를 이용해서 응답을 하겠다는 의미의 객체이다.
                                                                 # 그리고 그 인자로 전송하고싶은 값을 그 안에 적는다.
                                                                 # ('<h1>Random</h1>'+random.random()) 으로 적으면
                                                                 # +의 앞에는 문자열인데 뒤는 숫자이므로 에러가나서 str(random.random())로 str을 붙여준다.

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)
