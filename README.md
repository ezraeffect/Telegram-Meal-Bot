# Telegram-Meal-Bot
대한민국 초, 중, 고등학교의 급식을 텔레그램 채팅 봇으로 알려줍니다.
> 이 소스는 MIT라이선스 하에 자유롭게 이용할 수 있습니다.

### SerenityS님의 효암고등학교 카카오톡 봇을 일부 이용했습니다.
* https://github.com/SerenityS/kakaobot_hyoammeal

### 참고 사이트
* https://blog.qodot.me/post/python%EC%9C%BC%EB%A1%9C-%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8-%EB%B4%87-%EB%A7%8C%EB%93%A4%EA%B8%B0/
* http://yujuwon.tistory.com/entry/Telegrambot-%EB%A7%8C%EB%93%A4%EA%B8%B0
* https://recall2300.github.io/2017-01-01/telegram-bot/
* https://bakyeono.net/post/2015-08-24-using-telegram-bot-api.html

### 사용 언어
* Python + venv

### 필요 모듈
* beautifulsoup4
* urllib
* lxml
* dateutil

# 설치법
## 유의사항
> Amazon AWS EC2 사용시 로케일 오류가 잦습니다.
> http://egloos.zum.com/killins/v/3014274 을 참고해주세요.

### 1. 기초 패키지 설치
<pre> sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv</pre>
### 2. 레포지터리 클론 및 이동
<code>git clone https://github.com/ezraeffect/Telegram-Meal-Bot <working_dir> </code>
<code>cd <working_dir></code>
### 3. python 가상환경 구축 및 실행
<pre><code>python3 -m venv myvenv
source myvenv/bin/activate
</code></pre>
### 4. python 추가 요구 패키지 설치
<code>pip install Django lxml beautifulsoup4 python-dateutil</code>
### 5-1. crawl.py 코드 수정
crawl.py를 열어보면 상단에
<code>regioncode = 'XXX.go.kr'</code>
<code>schulcode = 'XXXXXXXXXXX'</code>
<code>sccode = 2</code>
세개의 수정사항이 있다
여기서 regionCode는 각 시도교육청의 주소이며, schulCode는 [링크](http://weezzle.tistory.com/559) 를 참조하도록 하자.
혹은 크롬에서 [링크](http://stu.sen.go.kr/edusys.jsp?page=sts_m42320)에 들어가 자신이 파싱하고자 하는 학교의 교육청에 들어가
학교 급식표를 불러온후 크롬의 F12(개발자 도구) - Application - Storage - Cookies의 schulcode를 불러오면 된다.
[ex_screenshot](./screenshot.png)
sccode는 학교 구분 코드인데 1은 고등학교 2는 중학교 3은 초등학교이다.

### 5-2. my.keyfile 수정
botFather에게서 봇을 생성하면 API Key를 주는데
my.keyfile을 열어 받은 API Key를 입력해주면 된다

### 6. 실행하기
<code>python3 bot.py</code>을 입력하여
Using a list of filters in MessageHandler is getting deprecated, please use bitwise operators (& and |) instead. More info: https://git.io/vPTbc.
 warnings.warn('Using a list of filters in MessageHandler is getting '
위와같이 뜬다면 정상이다
백그라운드 실행을 원하면 <code>python3 bot.py &</code>입력후 Ctrl+A, Ctrl+D를 누르면 된다.

### 7. crontab을 통한 crawl.py의 주기적 실행
```
crontab -e
# 매주 일요일 0시 0분에 crawl.py 실행
0 0 * * 7 cd ~/meal && /usr/bin/python3 crawl.py
```

## 작동 화면
