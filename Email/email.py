import smtplib
st = smtplib.SMTP_SSL ('smtp.gmail.com', 465)
st.login ('xyz@gmail.com', '123456789')
msg = '''From : XYZ <xyz@gmail.com>
To : ABC <abc@gmail.com>
Subject : TEST MAIL
content- type : text/html
<h1> HELLO DEAR </h1>
<h3> STAY HAPPY </h3>
'''
st.sendmail ('xyz@gmail.com', 'abc@gmail.com', msg)
st.quit ()