import urllib.request
from bs4 import BeautifulSoup

# 타학교에서 이용시 수정
regioncode = 'XXX.go.kr'
schulcode = 'XXXXXXXXXXX'

sccode = 2
# NEIS에서 조식 파싱
url = ('http://stu.' + regioncode + '/sts_sci_md01_001.do?schulCode=' + schulcode + '&schulCrseScCode=3&schulKndScCode=03&schMmealScCode=' + str(sccode))
try:
    source = urllib.request.urlopen(url, timeout=3)
except Exception as e:
    print(e)
    menu = ('급식 정보를 가져오는 중 문제가 발생하였습니다.\n관리자에게 연락바랍니다.')
else:
    # beautifulsoup4를 이용해 utf-8, lxml으로 파싱
    soup = BeautifulSoup(source, "lxml", from_encoding='utf-8')

    # div_id="contents"안의 table을 모두 검색 후 td태그만 추출
    table_div = soup.find(id="contents")
    tables = table_div.find_all("table")
    menu_table = tables[0]
    td = menu_table.find_all('td')

    today = 0
    while today < 7:
        # 월요일 ~ 토요일 = td[8] ~ td[13]
        menu = td[today + 8]
        print(menu)
        # 파싱 후 불필요한 태그 잔해물 제거
        menu = str(menu).replace('*', '').replace('<td', "").replace('<br/></td>', "").replace('</td>', '').replace('class="textC last">', '').replace('class="textC">','').replace('<br/>', '\n').replace('1.', '').replace('2.', '').replace('3.', '').replace('4.', '').replace('5.', '').replace('6.','').replace('7.', '').replace('8.', '').replace('9.', '').replace('10.', '').replace('11.', '').replace('12.', '').replace('13.', '').replace('14.', '').replace('15.', '').replace('1', '').replace(' ', '')

        if menu == '' and today != 5:
            menu = '급식 정보가 존재하지 않습니다.\n급식이 없는 날일 수 있으니 확인 바랍니다.'

        f = open(str(today) + ".txt", 'a')

        if today != 6:
            if sccode == 2:
                f = open(str(today) + ".txt", 'w')
                f.write("\n\n[중식]\n")
            f.write(menu)
        else:
            f = open(str(today) + ".txt", 'w')
            f.write("일요일은 급식이 제공되지 않습니다.")
        f.close()
        today = today + 1

    sccode = sccode + 1
