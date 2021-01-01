#email送信モジュール
import smtplib
from email.mime.text import MIMEText
 
#メール設定の情報
smtp_host = 'smtp.gmail.com'# そのまま
smtp_port = 587# そのまま
 
#----------------ここ以下の情報を編集する----------------
 
to_email = 'jyuon312k@gmail.com' # 送りたいアドレス
 
gmail_account = 'past.message@gmail.com' # Gmailのアドレス
gmail_password = 'ovsirmofelcvlqml' # Gmailのパスワード
 
#----------------編集スペースここまで----------------
 
def main():
     # メールの本文
     message = 'メールの本文内容'
     # メールの内容を作成
     msg = MIMEText(message, "html")     
     # 件名
     msg['Subject'] = '件名内容'
     # メール送信元 
     msg['From'] = gmail_account 
     #メール送信先
     msg['To'] = to_email 
 
     # メールサーバーへアクセス
     server = smtplib.SMTP(smtp_host, smtp_port)
     server.ehlo()
     server.starttls()
     server.ehlo()
     server.login(gmail_account, gmail_password)
     server.send_message(msg)
     server.quit()
 
 
if __name__=='__main__':
         main()