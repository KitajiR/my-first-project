import pandas as pd

def run():
    print("ジョブ2: データ処理を開始します...")

    try:
        df = pd.read_csv('weather_forecast.csv')
    except FileNotFoundError:
        raise Exception('一時ファイルが見つかりません。抽出ジョブが失敗した可能性があります。')
    
    df.columns = df.columns.str.replace('.','_', regex=False)
    
    df['forcast_date'] = pd.to_datetime(
        df['displayDate_year'].astype(str) + '-' +
        df['displayDate_month'].astype(str) + '-' +
        df['displayDate_day'].astype(str)
    )
    
    df['max_Temperature_fahrenheit'] = df['maxTemperature_degrees'] * 9/5 + 32
    df['min_Temperature_fahrenheit'] = df['minTemperature_degrees'] * 9/5 + 32
    
    df = df.rename(columns={
        'daytimeForecast_weatherCondition_description_text':'day_condition',
        'nighttimeForecast_weatherCondition_description_text':'night_condition',
        'maxTemperature_degrees':'max_temp_celsius',
        'minTemperature_degrees':'min_temp_celsius'
    })
    
    df.columns = df.columns.str.lower()
    
    print(df.head())
    
    df.to_csv('processed_weather_forecast.csv', index=False)
    
    print("ジョブ2: データ処理が完了しました。")
    print("\n加工データを'processed_weather_forecast.csv'に保存")
    
    return True

if __name__ == '__main__':
    run()