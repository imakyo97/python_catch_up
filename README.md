# 環境構築
asdf + poetryで開発環境を構築

## .tool-versionsが存在する場合
asdfと必要なasdfプラグインをインストールしてinstallを実行
```
$ asdf install
```

## asdfのインストール
1. asdfの動作に必要な`git`および`curl`をインストール
```
$ brew install coreutils curl git
```
2. asdfのダウンロード
```
$ git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0
```
3. .zshrcに下記の行を追記
```
. "$HOME/.asdf/asdf.sh"
```

## pythonを例にしたasdfの使い方
1. プラグインを表示
```
$ asdf plugin list all | grep python
```
2. プラグインをインストール
```
$ asdf plugin add python https://github.com/danhper/asdf-python.git
```
3. インストール済みのプラグインを一覧表示
```
$ asdf plugin list
```
4. インストール可能なバージョンを一覧表示
```
$ asdf list all python
```
5. バージョンを指定してインストール
```
$ asdf install python 3.12.1
```
6. インストール済みのバージョンを一覧表示
```
$ asdf list python
```
7. プロジェクトで使用するバージョンを指定
```
$ asdf local python 3.12.1
```

## poetryの使い方
-  プロジェクトの作成
```
$ poetry new python-catch-up
```
-  poetryの導入（既存プロジェクトの場合）
```
$ poetry init
```
- プロジェクトルートに仮想環境を持ってくる
```
$ poetry config virtualenvs.in-project true --local // --localをつけることでpoetry.tomlで管理できる
```
- 依存関係の指定
```
$ poetry add {パッケージ名}
```
- 依存関係のインストール
```
$ poetry install
```
- 仮想環境でPythonスクリプトを実行
```
$ poetry run python {ファイル名}.py
```
- ネストされたシェルで仮想環境をアクティブにする
```
$ poetry shell
```
- 仮想環境を非アクティブにし、ネストされたシェルを終了する
```
$ exit
```

## Ruffの設定
PythonのリンターおよびコードフォーマッタであるRuffの設定をする
1. VSCodeでRuffの拡張機能を追加
2. ユーザー設定のsetting.jsonに以下の設定を追加
```
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnType": true,
  }
```

## Pylanceのimport警告
VSCodeにPylanceの拡張機能を追加すると、`from fastapi import FastAPI`などで下記のエラーが発生する

`インポート "fastapi" を解決できませんでしたPylancereport(MissingImports)`

**ライブラリの場合**：Pythonインタープリターを設定して、警告が出ないようにする
1. コマンドパレット（Shift + Command + P）からPython: Select Interpreterコマンドを使用し、仮想環境を選択する

**自作モジュールの場合**：settings.jsonで`python.analysis.extraPaths`を指定する
1. コマンドパレット（Shift + Command + P）から基本設定：ワークスペース設定を開く
2. python.analysis.extraPathsを設定する
```
{
    "python.analysis.extraPaths": [
        "${workspaceFolder}/python-catch-up/python_catch_up/"
    ]
}
```


# Rancher Desktopのインストール
Dockerの実行環境を用意するため、Rancher Desktopをインストールする
1. https://rancherdesktop.io/ からRancher Desktopをインストール
2. アプリケーションからRancher Desktopを起動
3. Rancher Desktopの設定ダイアログで設定を選択し「Accept」押下
    - ローカルで Kubernetes クラスタを動かす必要がない場合、Enable Kubernetesのチェックを外す
    - containerdもしくはdockerd(moby)を選択。containerdの場合nerdctlコマンドになり、dockerdの場合dockerコマンドになる
    - Configure PATHではAutomaticを選択することで、現在使用しているシェルにパスを通してくれる

# redisサーバーの起動と停止
1. `redis_container`という名前のredisコンテナをデタッチモード（バックグラウンド）で実行（初回のみ）
```
$ docker run --name redis_container -d -p 6379:6379 redis
```
2. 停止しているコンテナを再開する
```
$ docker container ls --all // 全てのコンテナを表示
$ docker container start redis_container // コンテナを再開
```
2. redisがコンテナ内で実行されているかを確認
```
$ docker ps
```
3. redisコンテナのログを確認
```
$ docker logs redis_container
```
4. redisのCLIを使用
```
$ docker exec -it redis_container redis-cli
```
5. redisのCLIを終了
```
> exit
```
6. redisコンテナの終了
```
$ docker stop redis_container
```

## 参考
- https://asdf-vm.com/ja-jp/guide/getting-started.html
- https://dev.classmethod.jp/articles/asdf-python-introduction/
- https://python-poetry.org/docs/
- https://zenn.dev/takanori_is/articles/let-poetry-create-virtualenv-under-project-folder
- https://qiita.com/ciscorn/items/bf78b7ad8e0e332f891b
- https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters
- https://zenn.dev/miyajan/articles/migrate-from-docker-desktop-to-rancher-desktop
- https://kinsta.com/jp/blog/redis-docker/
