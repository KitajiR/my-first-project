import time
import pandas as pd

def run():
    print("ジョブ2: データ処理を開始します...")
    time.sleep(3) 
    
    try:
        df = pd.read_csv('temp_data.csv')
    except FileNotFoundError:
        raise Exception('一時ファイルが見つかりません。抽出ジョブが失敗した可能性があります。')
    
    filtered_df = df[(df['sales'] >= 100) & (df['status'] == 'OK')]
    
    filtered_df.to_csv('processed_data.csv', index=False)
    
    print("ジョブ2: データ処理が完了しました。")
    return True

if __name__ == '__main__':
    run()