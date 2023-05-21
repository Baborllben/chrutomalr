import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
import json
import email
import os

# 定义函数
a = (random.randint(0, 9) * 1)
b = (random.randint(0, 9) * 10)
c = (random.randint(0, 9) * 100)
d = (random.randint(0, 9) * 1000)
e = (random.randint(0, 9) * 10000)
f = (random.randint(0, 9) * 100000)
g = (random.randint(0, 9) * 1000000)
h = (random.randint(0, 9) * 10000000)
# 发出邮件的字符串
theEmail = str(a + b + c + d + e + f + g + h)

# json读取
current_path = os.path.abspath(os.path.dirname(__file__))
f = open(current_path+'\\temp-0.json', 'r')
content = f.read()
a = json.loads(content)
b = json.dumps(a)
userEmail = a['email']
print(userEmail)
# print(type(a))
f.close()

# SMTP邮件发送：
username = 'baboeliver@foxmail.com'
mandate_code = 'tdfqnluqemzwiigg'
to_addr = userEmail
smtp_server = 'smtp.qq.com'
# 邮件正文
smtp_txt = '<Chrutomalr>'+userEmail+'您的验证码为：'+theEmail+'\n很高兴您能使用Chrutomalr，这封邮件虽是验证码。但此邮件标注着您的注册流程已经过去一半，填写验证码后，您即可进入注册的最后一部分。\n如果您未在此平台注册过账户，请您不要理睬此邮件。可能您遭受了邮件轰炸，也可能是别人填错邮件了。\n From iceFoxr to <orgName>'+theEmail
form = 'iceFoxr <baboeliver@foxmail.com>'
to = 'orgName'
# 邮件标题
subject = '<Chrutomalr> 验证码接收'
# 邮箱正文内容，第一个参数为内容，第二个参数为格式()，第三个参数为编码
msg = MIMEText(smtp_txt, 'plain', 'utf-8')
# 邮件头部信息
msg['From'] = Header(form)
msg['To'] = Header(to)
# 邮件标题
msg['Subject'] = Header(subject, 'utf-8')

# 尝试连接
try:
    smtpobj = smtplib.SMTP_SSL(smtp_server)
    # 建立连接，参数：qq邮箱服务和端口号
    smtpobj.connect(smtp_server, 587)
    # 登录，发送方账号和授权码
    smtpobj.login(username, mandate_code)  #登录
    # 发送邮件，参数：发送方，接收方，内容
    smtpobj.sendmail(username, to_addr, msg.as_string())
    print("<Regedit> Email sent successfully")
except smtplib.SMTPException as smtpSendEmailError:
    print("<Regedit> Can't send email!! orgName: "+userEmail)
#窗口不消失
os.system("pause")
