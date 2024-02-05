# サーバーを起動
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
