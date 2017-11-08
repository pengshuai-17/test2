import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['subject'] = 'test'
msg['from'] = 'ps1185649798@163.com'
msg['to'] = '1185649798@qq.com'
content = "你好，这是一封自动发送的邮件。"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp=smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('ps1185649798@163.com','ps.970920')
smtp.sendmail('ps1185649798@163.com', '1185649798@qq.com', str(msg))
smtp.quit()
