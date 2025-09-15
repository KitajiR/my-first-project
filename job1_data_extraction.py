import time
import pandas as pd



def run():
    print("ジョブ1: データ抽出を開始します...")
    time.sleep(2) # 処理をシミュレート
    
    data = {
        'id':[1,2,3,4],
        'name':['Aさん', 'Bさん', 'Cさん', 'Dさん'],
        'sales':[120,200,65,99,],
        'status':['OK', 'NO', 'NO', 'OK']
    }
    
    df = pd.DataFrame(data)
    
    df.to_csv('temp_data.csv', index=False)

    print("ジョブ1: データを正常に抽出しました。")
    return True

if __name__ == '__main__':
    run()