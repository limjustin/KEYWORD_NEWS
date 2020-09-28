# KEYWORD_NEWS

### 신의 환수 (2019.11 ~ 2019.12)

----------

**주제** : 키워드 추출 및 음성 변환 기술을 이용한 '키워드 뉴스' 프로그램

**기획 배경** : 정보화 소외 계층(시각장애인)의 정보 접근성 보장

**팀원**

- [polyn0(양정안)](https://github.com/polyn0)
- [youngseo0526(김영서)](https://github.com/youngseo0526)
- [Lee-hwansoo(이환수)](https://github.com/Lee-hwansoo)
- [limjustin(임재영)](https://github.com/limjustin)
- [hyejinHong0602(홍혜진)](https://github.com/hyejinHong0602)

----------

**사용 프로그램**

- Pycharm : 파이썬 코드로 프로그램 기능 구현
- Qt Designer : UI Design

----------

**구동 알고리즘**

![image](https://user-images.githubusercontent.com/55044278/94399637-b5b80d80-01a2-11eb-99b0-f95fd9bbb364.png)

----------

**프로그램 실행 화면**

- **시작 화면**
  - 시작 버튼을 누르면 메인 화면으로 넘어감
  - 🔈(TTS) : "반갑습니다. Keyword News 프로그램에 오신 것을 환영합니다."

![image](https://user-images.githubusercontent.com/55044278/94392650-d5940500-0193-11eb-88dd-9bf36094f272.png)

<br>

- **메인 화면**
  - 총 9가지 분야가 화면에 표시
  - 분야에 맞는 번호를 키보드를 통해 누르면 해당 분야 기사를 볼 수 있음
  - 🔈 : "분야를 골라주세요. 1번은 전체, 2번은 정치, 3번은 경제, 4번은 사회, 5번은 국제, 6번은 스포츠, 7번은 문화, 8번은 연예, 9번은 IT 입니다."

![image](https://user-images.githubusercontent.com/55044278/94392659-d9c02280-0193-11eb-88f5-eb2fe8f9e3ea.png)

<br>

- **분야 화면**

  - 첫 번째 기사의 Wordcloud 출력

  - ```돌아가기(1)``` : 메인 화면으로 되돌아 감

  - ```현재기사(2)``` : 현재 기사의 본문을 Crawling 하여 가져옴

  - ```다음 키워드(3)``` : 다음 기사의 Wordcloud 출력 

  - 🔈 : "제목은 ~~~~ 입니다. 키워드는 OO, OO, OO, OO, OO 입니다."

    ​	   "이 기사를 읽으려면 2번, 다음 기사의 키워드는 3번, 분야 선택(홈)은 1번입니다."

    - 키워드는 빈도 수가 높은 순으로 상위 5개의 단어들만 읽어주도록 구현

![image](https://user-images.githubusercontent.com/55044278/94392664-dcbb1300-0193-11eb-8fc9-24a1cee5aef0.png)

- ```다음 키워드(3)``` 버튼의 실행 결과

![image](https://user-images.githubusercontent.com/55044278/94392668-dfb60380-0193-11eb-82ef-034121f23a78.png)

- ```현재기사(2)``` 버튼의 실행 결과
  - 🔈 : "선택하신 기사 내용은 ~~~~ 입니다."
    - 기사의 본문 전체를 읽어주도록 구현

![image](https://user-images.githubusercontent.com/55044278/94392672-e2185d80-0193-11eb-98d4-ecdfef11505b.png)