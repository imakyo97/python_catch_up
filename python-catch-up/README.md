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