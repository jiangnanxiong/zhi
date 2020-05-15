import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
from email.mime.multipart import MIMEMultipart
import os

# 发送邮箱服务器
smtpserver = 'smtp.mxhichina.com'
# 发送邮箱用户/密码
user = 'jun.wu@zeropartner.com'
password = 'Jun123456'  # 发送人邮件的客户端授权码


# 定义文件目录
def file_report():
    result_dir = '../testreport'
    lists = os.listdir(result_dir)
    # 重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    file = os.path.join(result_dir, lists[-1])
    print(file)
    return file


# 发送的附件
def send_mail(file_new):
    # 发送邮箱
    sender = 'jun.wu@zeropartner.com'
    # 接收邮箱
    receiver = '948325350@qq.com'
    # 发送邮件主题
    subject = '智训{}UI测试报告'.format(datetime.now().strftime('%Y-%m-%d-%H:%M'))
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEMultipart()
    # 发送的附件
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="testreport.html"'  # 定义附件名称
    msg.attach(att)
    msg['subject'] = Header(subject, 'utf-8')
    msg['from'] = sender  # 设置发送人
    msg['to'] = receiver  # 设置接收人

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

    # 发送,发送多人要用到split分割成列表
    # smtp.sendmail(sender, receive.split(','), msg.as_string())

