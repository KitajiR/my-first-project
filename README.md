# Google Weather APIによるETLパイプラインの構築
ハワイ・ホノルルの天気予報データをAPIから取得し、Google cloud BigQueryへロード、SQLで分析を行う自動化されたデータパイプラインを構築したプロジェクト。

---

## プロジェクトの目的
手作業でのデータ収集・整形の手間をなくし、APIから取得した最新の気象データを直接BigQueryにロードすることで、即時分析可能なデータ基盤を確立することを目的とします。

---

## 使用技術とインフラ

| カテゴリ | 技術スタック | 備考 |
| :--- | :--- | :--- |
| **言語・ライブラリ** | `Python 3.11`, `Pandas`, `requests`, `google-cloud-bigquery` | ETL処理、データ整形に利用 |
| **クラウドサービス** | **Google Cloud Platform (GCP)**, **BigQuery** | データウェアハウスとして利用 |
| **オーケストレーション**| `subprocess` (`main.py`にてJobの順序を管理) | パイプラインの自動実行に利用 |
| **バージョン管理** | `Git`, `GitHub` | コード管理と公開に利用 |

---

## ETLパイプラインの詳細

本プロジェクトは、ETL（抽出・変換・ロード）の各フェーズを個別のPythonスクリプトとして実装し、`main.py`で一元管理しています。

### 1. E (抽出): `job1_data_extraction.py`
Google Weather APIから日別予報データを取得し、**`pd.json_normalize`** を使用してネストされたJSONをフラットなテーブル構造に変換。**冗長な単位情報や複雑な列（`.unit`, `interval`など）を動的に削除**し、クリーンなCSVを出力します。

### 2. T (変換): `job2_data_processing.py`
**BigQueryの命名規則**に合わせ、全てのドット（`.`）をアンダースコア（`_`）に置換。摂氏を華氏に変換し、日付を `YYYY-MM-DD` 形式に整形しました。

### 3. L (ロード): `job3_data_load.py`
Pandas DataFrameを`google-cloud-bigquery`ライブラリを使用してBigQueryテーブルに直接ロード。**認証情報を環境変数から読み込む**ことで、セキュリティと移植性を確保しています。

---

## BigQueryでの分析

作成中

---

## 実行方法

1.  **環境設定**
    ```bash
    # 仮想環境の作成と有効化
    python3 -m venv .venv
    source .venv/bin/activate
    
    # 必要なライブラリのインストール
    pip install pandas requests google-cloud-bigquery pandas-gbq
    ```

2.  **認証情報の設定 (重要)**
    ターミナルで以下の環境変数を設定してください。
    ```bash
    # Weather API Key
    export WEATHER_API_KEY="[YOUR_WEATHER_API_KEY]"
    
    # Google Cloud Credentials Path
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"
    ```

3.  **パイプラインの実行**
    ```bash
    python main.py
    ```
