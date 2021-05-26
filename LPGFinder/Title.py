from tkinter import *
from tkinter import font
import http.client
from xml.dom.minidom import parse, parseString
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import tkinter.messagebox
import WebBrowser
g_Tk = Tk()
g_Tk.geometry("900x640")
g_Tk["bg"]="navy"
DataList = []

def InitTopText():
    TempFont = font.Font(g_Tk, size=45, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="Welcome to My LPG FINDER")
    MainText.pack()
    MainText.place(x=45)
    MainText["bg"] = "white"

    SFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    l1=Label(g_Tk,font = SFont,text="Choose the option what you want.")
    l1.pack()
    l1.place(x=200,y=120)
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
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    SearchLPG()

    RenderText.configure(state='disabled')


def SearchLPG():


    url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): 'F4ZSQFrTrgSxVr9UoGJ8XvzDDhNg6mZmgfa4iAhVTNbcW2j7rrsJa7TR1De8UcZ1gQtaiyN0hbmcaeBTZGMbNw', quote_plus('pageNo'): '1', quote_plus('numOfRows'): '10',
         quote_plus('addr'): '인천광역시 계양구 작전동 256-2 지상주차장 4층 E10번'})

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    print
    response_body

    for i in range(len(queryParams)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "주소: ")
        RenderText.insert(INSERT, queryParams[i][0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "타입: ")
        RenderText.insert(INSERT, queryParams[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "ID: ")
        RenderText.insert(INSERT, queryParams[i][2])
        RenderText.insert(INSERT, "\n\n")



def InitOneButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button1 = Button(g_Tk, font = TempFont, text="     현위치 LPG FINDER     ",  command=OneButtonAction, width=30, height=7)
    Button1.pack()
    Button1.place(x=150, y=200)
    Button1["bg"]="cyan"



def InitTwoButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button2 = Button(g_Tk, font=TempFont, text="     지역 LPG FINDER     ", command=TwoButtonAction, width=30, height=7)
    Button2.pack()
    Button2.place(x=480, y=200)
    Button2["bg"] = "cyan"

def InitThreeButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button3 = Button(g_Tk, font=TempFont, text="     길찾기 LPG FINDER     ", command=ThreeButtonAction, width=30,
                     height=7)
    Button3.pack()
    Button3.place(x=150, y=400)
    Button3["bg"] = "cyan"

def InitFourButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    Button4 = Button(g_Tk, font=TempFont, text="     지역별 LPG 분포도     ", command=FourButtonAction, width=30, height=7)
    Button4.pack()
    Button4.place(x=480, y=400)
    Button4["bg"] = "cyan"




def OneButtonAction():
    WebBrowser.main()

def TwoButtonAction():
    InitInputLabel()
    InitSearchButton()
    InitRenderText()

def ThreeButtonAction():
    pass

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

InitTopText()





InitOneButton()

InitTwoButton()

InitThreeButton()

InitFourButton()




g_Tk.mainloop()


