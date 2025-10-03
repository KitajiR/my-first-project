import pandas as pd
import requests

def run():
    print('ジョブ1:抽出を開始します')
    res = requests.get('https://weather.googleapis.com/v1/forecast/days:lookup?key=AIzaSyCI7dw-34eQdYDN4AbOBiDOlUFYACJWELc&location.latitude=21.3&location.longitude=-157.8')
    #print('レスポンスレコード：',res.status_code)
    if res.status_code == 200:
        data = res.json()
     
        df = pd.json_normalize(data['forecastDays'])
        
        keywords_to_drop = [
            '.unit',
            'interval',
            'iconBaseUri',
            'languageCode',
            'snowQpf',
            'iceThickness'
        ]
        
        columns_to_drop_final = []
        for col in df.columns:

            if any(keyword in col for keyword in keywords_to_drop):

                columns_to_drop_final.append(col)
                
        print("【削除する列】：", columns_to_drop_final)        
     
        df = df.drop(columns= columns_to_drop_final, errors='ignore')
     
        df.to_csv('weather_forecast.csv',index=False, encoding="UTF-8")
        print('ホノルルの天気予報情報を抽出できました。')
        print('ファイル名:weather_forecast.csv')
     
    else:
        print("リクエストに失敗しました。ステータスコード：",res.status_code)
        print("エラーメッセージ：",res.text)

if __name__== '__main__':
    run()    
    