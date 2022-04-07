from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
# topics라는 리스트를 만들어 만들어둔 딕셔너리들을 그룹핑해준다.
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag, id=None):  # id가 입력되지 않았을때를 대비하기위해 id=None 으로 지정해둔것이다.
    global topics  # topics라는 변수를 이 함수에서 사용하기위해 전역변수로 지정함.
                   # 더 자세한건 도장깨기 파이썬md파일에 정리해두겠다.
    contextUI = ''  # id가 있을때에만 delete UI버튼을 나오게할것임 => 즉, 홈버튼에서는 delete UI버튼이 안나오도록 만들어볼것임.
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href = "/update/{id}">update</a></li>
        '''
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
            {contextUI}
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
    return HttpResponse(HTMLTemplate(article, id))

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
                                 # topics에 newTopic 추가해서 사이트의 글 목록에 더 create 함.
        url = '/read/'+str(nextId)
        nextId = nextId + 1
        return redirect(url)  # redirect() 안의 매개변수의 url로 이동해라 라는 뜻이다.
                              # redirect 리디렉트와 관련된 것은 django_생활코딩 md 파일에 정리해두겠다.

@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))  # HTMLTemplate 함수의 update 부분을 보면 a href 태그로 링크가 걸려있기때문에
                                                        # 이건 post방식이 아니라 get 방식이다.
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')


@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']  # id는 입력받은 id값이다. (아마도?)
        newTopics = []  # newTopic과 헷갈리지말자!
        for topic in topics:  # for문으로 순회를 하면서 id와 일치하지않는 애들을 newTopics 리스트에 추가하여 넣겠다.
            if topic['id'] != int(id):  # 삭제안할것들을 걸러냄.
                newTopics.append(topic)
        topics = newTopics  # 삭제할 입력된 id가 다른것들(삭제안할것들)을 newTopics 리스트에 넣어두고 topics 와 일치시키면
                            # 그 topics는 결국 '삭제되고 남은것들의 집합체'가 된다. => 홈으로 결국 이동시킬것
                            # 참고로 삭제안할거 제외하고 나머지를 전부 topic을 다시 만든것이므로, 이는 결국 하나를 삭제시킨것과 동일한 효과라는 것이다.
        return redirect('/')  # 이 작업이 끝나면 사용자를 홈으로 보내버린다.
