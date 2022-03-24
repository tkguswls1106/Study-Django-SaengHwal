from django.shortcuts import render, HttpResponse
import random

# topics라는 리스트를 만들어 만들어둔 딕셔너리들을 그룹핑해준다.
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag):
    global topics  # topics라는 변수를 이 함수에서 사용하기위해 전역변수로 지정함.
                   # 더 자세한건 도장깨기 파이썬md파일에 정리해두겠다.
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'  # f는 파이썬의 f-string 이라는 문자열 포매팅 방법인데, 도장깨기 파이썬md파일에 정리해두겠다.
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>
    </html>
    '''

# views에다가 클라이언트로 정보를 전송하기위한 함수를 작성한다. 먼저 index 함수를 작성한다.
def index(request):  # 이 함수는 첫번째 파라미터의 인자로 요청과 관련된 여러가지 정보가 들어오도록 약속되어있는 객체를 전달해주도록 되어있다.
                     # => request 라는 이름의 파라미터를 적어준다. 사실 뭘적든 상관은 없지만 관습적으로 request라고 적어주는것을 추천한다.
    article = '''
    <h2>Welcome</h2>
        Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('Create')  # HttpResponse()는 http를 이용해서 응답을 하겠다는 의미의 객체이다.
                                   # 그리고 그 인자로 전송하고싶은 값을 그 안에 적는다.
