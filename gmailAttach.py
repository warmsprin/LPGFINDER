import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def sendAddrList(addrlist, InitGmailInputLabel):
    # 세션생성, 로그인
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("userid@gmail.com", "password")
    #userid@gmail.com은 자신이 사용하는 지메일 주소로 바꾸고
    #password는 지메일 주소의 비밀번호로 바꿔야 실행됨

    # 제목, 본문 작성
    msg = MIMEMultipart()
    msg['Subject'] = '전기차 충전소 어플 - 지역 전기차 충전소 정보'
    #msg.attach(MIMEText('본문', 'plain'))
    for i in range(len(addrlist)):
        msg.attach(MIMEText(addrlist[i], 'plain'))

    # 파일첨부
    attachment = open('map.html', 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + "map.html")
    msg.attach(part)

    # 메일 전송
    # userid@gmail.com은 s.login에 입력한 지메일 주소와 같은 것으로 바꿔야 실행됨
    s.sendmail("userid@gmail.com", InitGmailInputLabel, msg.as_string())
    s.quit()
    print("gmailAttach 전송 성공!")