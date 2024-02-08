# Dockerを使ったアプリの起動と停止
`docker-compose.yml`を使ってアプリの起動と停止を行う
1. 以下のコマンドを実行し、アプリを起動
```
$ docker compose up
```
2. `ctrl + c`でアプリを停止

# フォルダ構成
```
python-catch-up/
├── python_catch_up/
│   ├── database/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── __init__.py
│   └── main.py
├── test/
├── poetry.lock
├── poetry.toml
├── pyproject.toml
└── firebase.json
```
- `database/` : データベースの設定などのディレクトリ
- `models/` : データベースモデルのディレクトリ
- `routers/` : エンドポイント定義のディレクトリ
- `schemas/` : APIモデルのディレクトリ
- `services/` : DBアクセスなどのビジネスロジックのディレクトリ

# Dockerを使わないアプリの起動と停止
python_catch_up/admin/admin.pyに記載されているredisのURLを`redis://localhost:6379`に書き換える

以下のコマンドを実行し、dockerでredisサーバーを立ち上げる
```
$ doker container start redis
```

## launch.jsonから実行する場合
VSCodeの実行とデバックから`FastAPI：Debug`を実行する

## コマンドから実行する場合
poetryで作成された仮想環境をアクティブにし、uvicornでサーバーを起動する
```
$ poetry shell // 仮想環境をアクティブにする
$ uvicorn main:app --reload // ライブサーバーを起動
```
> [!NOTE]
> uvicorn main:appは以下を示します
> - `main`: `main.py`ファイル
> - `app`: `main.py`内部で作られるobject（`app = FastAPI()`のように記述される）
> - `--reload`: コードの変更時にサーバーを再起動させる。開発用。

以下のコマンドで仮想環境を非アクティブにする
```
$ exit
```
