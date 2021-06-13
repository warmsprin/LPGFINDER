from tkinter import *
from tkinter import font
import http.client
from xml.dom.minidom import parse, parseString
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import tkinter.messagebox
import WebBrowser

import http.client
import xml.etree.ElementTree as ET

#지메일 연동 때문에 추가
#import gmail
#from xmlbook import * #???
#from http.client import HTTPSConnection
#from http.server import BaseHTTPRequestHandler, HTTPServer
import folium

g_Tk = Tk()
g_Tk.geometry("900x640")
g_Tk["bg"]="navy"
DataList = []
addrlist = []

def InitTopText():
    TempFont = font.Font(g_Tk, size=45, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="전기차 충전소 어플")
    MainText.pack()
    MainText.place(x=170)
    MainText["bg"] = "white"

    SFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    l1=Label(g_Tk,font = SFont,text="Choose the option what you want.")
    l1.pack()
    l1.place(x=10,y=120)
    l1["bg"] = "white"

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=500, y=105)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=820, y=110)

def SearchButtonAction():
    global SearchListBox, InputLabel

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    SearchLPG(InputLabel.get())

    RenderText.configure(state='disabled')

def SearchLPG(region):
    global addrlist, InputLabel
    url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): 'OsStwAQk2Orc+hEyRvDjXQXKRX3Z5M7VtxAZfSkdhf6ba+7xboEt9vYj6/2ZFalb1BoIWYgNkO7jxk5r7E1Rag==', quote_plus('pageNo'): '1', quote_plus('numOfRows'): '10',
         quote_plus('addr'): region})

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode("utf-8")

    tree = ET.ElementTree(ET.fromstring(response_body))
    charge = tree.iter("item")

    addrlist.clear()
    for charging in charge:
        addr = charging.find("addr").text
        addrlist.append(addr)

    for i in addrlist:
        print(i)  #요기가 콘솔에 xml 표시하는 부분??

    for i in range(len(addrlist)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "] ")
        #RenderText.insert(INSERT, "시설명: ")
        RenderText.insert(INSERT, addrlist[i])
        RenderText.insert(INSERT, "\n\n")

def Initteller():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    #Button5 = Button(g_Tk, font=TempFont, text="Telegram", command=TelButtonAction)
    Button5 = Button(g_Tk, font=TempFont, text="Telegram")
    Button5.pack()
    Button5.place(x=800, y=600)
    Button5["bg"] = "white"

def InitOneButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button1 = Button(g_Tk, font = TempFont, text="  현위치 전기차 충전소  ",  command=OneButtonAction, width=20, height=7)
    Button1.pack()
    Button1.place(x=15, y=200)
    Button1["bg"]="cyan"

def InitTwoButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button2 = Button(g_Tk, font=TempFont, text="  지역 전기차 충전소  ", command=TwoButtonAction, width=20, height=7)
    Button2.pack()
    Button2.place(x=250, y=200)
    Button2["bg"] = "cyan"

def InitThreeButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button3 = Button(g_Tk, font=TempFont, text="  길찾기 전기차 충전소  ", command=ThreeButtonAction, width=20, height=7)
    Button3.pack()
    Button3.place(x=15, y=400)
    Button3["bg"] = "cyan"

def InitFourButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button4 = Button(g_Tk, font=TempFont, text="  지역별 충전소 분포도  ", command=FourButtonAction, width=20, height=7)
    Button4.pack()
    Button4.place(x=250, y=400)
    Button4["bg"] = "cyan"




def OneButtonAction():
    WebBrowser.main()

def TwoButtonAction():
    InitInputLabel()
    InitSearchButton()
    InitRenderText()

def ThreeButtonAction():
    WebBrowser.main()

def FourButtonAction():
    pass

def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=500, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

def GmailButtonAction():
    InitGmailInputLabel()
    InitGmailSendingButton()

    #옮기는게 좋을 것 같은데...
    # eclass 강의자료 참고했음, HTML 파일 생성은 되지만 웹 브라우저와 연동이 안됨
    # 지도 저장
    # 위도 경도 지정
    m = folium.Map(location=[37.3402849, 126.7313189], zoom_start=13)
    # 마커 지정
    folium.Marker([37.3402849, 126.7313189], popup='한국산업기술대').add_to(m)
    # html 파일로 저장
    m.save('map.html')

    #import gmailAttach
    #gmailAttach.sendAddrList(addrlist)

def InitGmailInputLabel():
    global InitGmailInputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InitGmailInputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InitGmailInputLabel.pack()
    InitGmailInputLabel.place(x=80, y=590)

def InitGmailSendingButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SendingButton = Button(g_Tk, font = TempFont, text="전송",  command=SendingButtonAction)
    SendingButton.pack()
    SendingButton.place(x=400, y=600)

def SendingButtonAction():
    global InitGmailInputLabel

    import gmailAttach
    gmailAttach.sendAddrList(addrlist, InitGmailInputLabel.get())

def InitGmailButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button6 = Button(g_Tk, font = TempFont, text="Gmail", command=GmailButtonAction)
    Button6.pack()
    Button6.place(x=10, y=600)
    Button6["bg"]="white"

InitTopText()

InitOneButton()

InitTwoButton()

InitThreeButton()

InitFourButton()

Initteller()

InitGmailButton()

g_Tk.mainloop()