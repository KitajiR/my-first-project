import pandas as pd
import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  '/Users/kitajimaryuunosuke/Desktop/GCP_Folder/main-sphere-472405-g3-d6388ae7ab26.json' 

def run():
    print("ジョブ3:BigQueryへのロードを開始します。")
    
    PROJECT_ID = "main-sphere-472405-g3"
    DATASET_ID = "my_first_project"
    TABLE_ID = "portfolio"
    CSV_FILE = 'processed_weather_forecast.csv'    
    
    try:
        df = pd.read_csv(CSV_FILE)
        print(f'次のデータをロードします：\n{df}')
    except FileNotFoundError:
        print('ロードするデータが見つかりません。')
        return False
    
    client = bigquery.Client(project=PROJECT_ID)
    table_ref = client.dataset(DATASET_ID).table(TABLE_ID)
    
    try:
        job = client.load_table_from_dataframe(
            df,
            table_ref,
            job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
        )
    
        job.result()
    
        print(f"データロード完了！テーブル：{DATASET_ID}.{TABLE_ID}")
        print(f"ロードされた行数：{job.output_rows}")
    
    except Exception as e:
        print(f"BigQueryへのロード中にエラーが発生しました:{e}")
        return False
     
    print("ジョブ3: データロードが完了しました。")
    return True

if __name__ == '__main__':
    run()