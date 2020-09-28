# -*- coding: utf-8 -*-

import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import uic
import feedparser
import newspaper
from konlpy.tag import Mecab
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from gtts import gTTS
import time
import os
from PIL import Image

MainUI = 'main.ui'
MenuUI = 'menu.ui'

def rss_link(num):
    rss = ['http://www.khan.co.kr/rss/rssdata/total_news.xml',
           'http://www.khan.co.kr/rss/rssdata/politic_news.xml',
           'http://www.khan.co.kr/rss/rssdata/economy_news.xml',
           'http://www.khan.co.kr/rss/rssdata/society_news.xml',
           'http://www.khan.co.kr/rss/rssdata/kh_world.xml',
           'http://www.khan.co.kr/rss/rssdata/kh_sports.xml',
           'http://www.khan.co.kr/rss/rssdata/culture_news.xml',
           'http://www.khan.co.kr/rss/rssdata/kh_entertainment.xml',
           'http://www.khan.co.kr/rss/rssdata/it_news.xml']
    return rss[num-1]

def links_crawling(rss):
    feeds = feedparser.parse(rss)
    links = [entry['link'] for entry in feeds['entries']]
    return links

def news_makefile():
    global links
    global num
    global news_text
    article = newspaper.Article(links[num], language='ko')
    article.download()
    article.parse()
    news_text = article.text
    headline = article.title
    engine = Mecab()
    nouns = engine.nouns(news_text)
    nouns = [n for n in nouns if len(n) > 1]
    count = Counter(nouns)
    tags = count.most_common(15)
    print(headline, tags)
    text = " 제목은  " + headline + " 입니다.  " + "키워드는 "  "  " + str(tags[0][0]) + str(tags[1][0]) + str(tags[2][0]) + str(tags[3][0]) + str(tags[4][0])
    tts = gTTS(text + "입니다.  이 기사를 읽으려면 5번, 다음 기사의 키워드는 6번, 분야선택(홈)은 0번 입니다", lang='ko')
    tts.save('keyword.mp3')
    font_path = 'c:\\windows\\fonts\\NanumGothic.ttf'
    wc = WordCloud(font_path=font_path, background_color='white', width=500, height=400)
    cloud = wc.generate_from_frequencies(dict(tags))
    fig = plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    fig.savefig('keyword.jpg')
    image = Image.open('keyword.jpg').resize((500,400)).save('keyword.jpg')
    tts2 = gTTS("선택하신 기사 내용은   " + news_text, lang='ko')
    tts2.save("news_all.mp3")


class PopUp(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        global news_text
        uic.loadUi(MenuUI, self)
        self.textBrowser.close()
        self.show()
        self.keywordplay()
        self.show_img()
        self.num_pushButton_1.clicked.connect(lambda : self.keywordoff())
        self.num_pushButton_1.clicked.connect(lambda : self.close())
        self.num_pushButton_2.clicked.connect(lambda : self.keywordoff())
        self.num_pushButton_2.clicked.connect(lambda : self.newsread())
        self.num_pushButton_2.clicked.connect(lambda : self.textBrowser.setText(news_text))
        self.num_pushButton_2.clicked.connect(lambda : self.textBrowser.show())
        self.num_pushButton_3.clicked.connect(lambda: self.textBrowser.close())
        self.num_pushButton_3.clicked.connect(lambda : self.keywordoff())
        self.num_pushButton_3.clicked.connect(lambda : os.remove("keyword.mp3"))
        self.num_pushButton_3.clicked.connect(lambda : os.remove("news_all.mp3"))
        self.num_pushButton_3.clicked.connect(lambda : self.nextkeyword())
        self.num_pushButton_3.clicked.connect(lambda : self.show_img())
        self.num_pushButton_3.clicked.connect(lambda : self.keywordplay())

    def nextkeyword(self):
        global num
        num = num + 1
        news_makefile()

    def newsread(self):
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("news_all.mp3")))
        self.player.play()

    def keywordplay(self):
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("keyword.mp3")))
        self.player.play()

    def keywordoff(self):
        self.player.stop()

    def show_img(self):
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("keyword.jpg")
        self.label_view.setPixmap(self.qPixmapVar)

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(MainUI, self)
        self.menuplay()
        self.num_pushButton_1.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_1.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_2.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_3.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_4.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_5.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_6.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_7.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_8.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_9.clicked.connect(lambda: self.menuoff())
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda : PopUp(self))
        self.num_pushButton_0.clicked.connect(self.close)

    def NumClicked(self, state, button):
        global links
        global num
        num = 0
        exist_line_text = self.q_lineEdit.text()
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)
        links = links_crawling(rss_link(int(now_num_text)))
        news_makefile()

    def menuplay(self):
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("menu.mp3")))
        self.player.play()

    def menuoff(self):
        self.player.stop()

# 메뉴.mp3 만드는 코드
def menu_make():
    tts = gTTS(text=" 분야를 골라주세요. 1번은 전체 2번은 정치 3번은 경제 4번은 사회 5번은 국제 6번은 스포츠 7번은 문화 8번은 연예 9번은 IT입니다.", lang='ko')
    tts.save("menu.mp3")
# menu_make()

# 키 메뉴.mp3 만드는 코드
def key_menu_make():
    tts = gTTS(text="  이 기사를 읽으려면 5번, 다음 기사의 키워드는 6번, 분야선택은 0번 입니다.", lang='ko')
    tts.save("key_menu.mp3")
#key_menu_make()

links = []
num = 0
news_text = ''
text =''

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()

