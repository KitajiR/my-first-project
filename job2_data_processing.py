# job2_data_processing.py
import time

def run():
    print("ジョブ2: データ処理を開始します...")
    time.sleep(3) # 処理をシミュレート
    print("ジョブ2: データ処理が完了しました。")
    return True

if __name__ == '__main__':
    run()