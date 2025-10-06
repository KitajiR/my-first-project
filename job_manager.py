import subprocess
import sys
import os

def run_job(script_name):
    python_executable = sys.executable
    
    command = [python_executable, script_name]
    
    print(f"\n---ジョブ開始:{script_name}---")

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8')

        print(result.stdout)
        print(f"---ジョブ成功:{script_name}---")
        
    #失敗したらパイプライン停止    
    except subprocess.CalledProcessError as e:
        print(f'---ジョブ失敗:{script_name}---')
        print(f"エラーコード:{e.returncode}")
        print("標準エラー出力:\n", e.stderr)
        sys.exit(1)

def run_job_flow():
    
    jobs = [
        'job1_data_extraction.py',
        'job2_data_processing.py',
        'job3_data_load.py'
    ]
    
    if not os.environ.get('WEATHER_API_KEY') or not os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'):
       print("\n--- 認証エラー ---")   
       print("APIキーまたは、BigQueryの認証情報が設定されていません")
       sys.exit(1)
       
    print("--- ジョブフローを開始します ---")   
    
    for job in jobs:
        run_job(job)
    
    print("--- ジョブフロー実行完了！ ---")

if __name__ == "__main__":
    run_job_flow()