# job_manager.py
import datetime
import smtplib
from email.mime.text import MIMEText

# --- 設定 ---
JOBS = [
    {"name": "ジョブ1", "module": "job1_data_extraction"},
    {"name": "ジョブ2", "module": "job2_data_processing"},
    {"name": "ジョブ3", "module": "job3_data_loading"},
]

# メール通知の設定
SENDER_EMAIL = "your_email@gmail.com" # 送信元メールアドレス
SENDER_PASSWORD = "your_app_password" # アプリパスワード
RECEIVER_EMAIL = "receiver_email@example.com" # 送信先メールアドレス

def send_notification(subject, body):
    """メールを送信する関数"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        # GmailのSMTPサーバーを使用する場合
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print(f"メールを送信しました: {subject}")
    except Exception as e:
        print(f"メール送信に失敗しました: {e}")

def run_job_flow():
    """ジョブフローを実行するメイン関数"""
    print("--- ジョブフローを開始します ---")
    log_file_name = f"log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(log_file_name, "w") as log_file:
        log_file.write(f"ジョブフロー開始: {datetime.datetime.now()}\n")
        
        for job in JOBS:
            job_name = job["name"]
            module_name = job["module"]
            
            log_file.write(f"\n--- {job_name}の実行を開始 --- ({datetime.datetime.now()})\n")
            
            try:
                # 動的にモジュールをインポート
                module = __import__(module_name)
                module.run()
                
                log_file.write(f"--- {job_name}が正常に完了しました --- ({datetime.datetime.now()})\n")
                
            except Exception as e:
                error_message = f"--- {job_name}が失敗しました --- ({datetime.datetime.now()})\n"
                error_message += f"エラー: {e}\n"
                print(error_message)
                log_file.write(error_message)
                
                # 失敗時の通知
                subject = f"[ジョブ失敗] {job_name}が失敗しました"
                body = f"ジョブ名: {job_name}\nエラー内容: {e}\n\nログファイル: {log_file_name}"
                send_notification(subject, body)
                
                print("--- ジョブフローを中断します ---")
                return # 失敗したらそこで終了
        
        log_file.write(f"\nジョブフロー完了: {datetime.datetime.now()}\n")
    
    print("--- ジョブフローが正常に完了しました ---")

if __name__ == "__main__":
    run_job_flow()