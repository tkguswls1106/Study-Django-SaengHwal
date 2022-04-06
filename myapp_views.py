from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
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
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
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
    return HttpResponse(HTMLTemplate(article))  # HttpResponse(값) 는 다른 함수에서 값을 리턴받아 return HttpResponse(다른 함수의 리턴값) 으로 사용하게 될 경우,
                                                # 그 다른 함수의 리턴값 안의 문자열을 html코드로 해석하여 출력해준다.

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):  # 현재 상태는 그냥 홈페이지 접속해서 create 링크만 누르면 요청 메서드가 'GET'이고,
                      # 홈페이지 들어가서 create 링크 눌러서 들어가서 빈칸에 정보 입력하고 제출버튼 누르면, 요청 메서드가 'POST'로 설정시켜놓았다.
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))  # HttpResponse()는 http를 이용해서 응답을 하겠다는 의미의 객체이다.
                                                    # 그리고 그 인자로 전송하고싶은 값을 그 안에 적는다.
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)  # 딕셔너리는 append 사용이 안되지만, topics는 딕셔너리를 그룹핑한 리스트이므로 사용이 가능하다.
        url = '/read/'+str(nextId)
        nextId = nextId + 1
        return redirect(url)  # redirect() 안의 매개변수의 url로 이동해라 라는 뜻이다.
                              # redirect 리디렉트와 관련된 것은 django_생활코딩 md 파일에 정리해두겠다.
