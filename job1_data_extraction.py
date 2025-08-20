# job1_data_extraction.py
import time
import random

def run():
    print("ジョブ1: データ抽出を開始します...")
    time.sleep(2) # 処理をシミュレート
    
    # 確率で失敗するようにしてみましょう
    if random.random() < 0.1: # 10%の確率で失敗
        raise Exception("データソースへの接続に失敗しました。")

    print("ジョブ1: データを正常に抽出しました。")
    return True

if __name__ == '__main__':
    run()