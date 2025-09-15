import time
import pandas as pd

def run():
    print("ジョブ3: データロードを開始します...")
    time.sleep(1)
    
    try:
        df = pd.read_csv('processed_data.csv')
        print(f'次のデータをロードします：\n{df}')
    except FileNotFoundError:
        print('ロードスリデータがありません。処理ジョブでフィルタリングされた可能性があります。')
    
    print("ジョブ3: データロードが完了しました。")
    return True

if __name__ == '__main__':
    run()