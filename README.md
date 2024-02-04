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


## 参考
- https://asdf-vm.com/ja-jp/guide/getting-started.html
- https://dev.classmethod.jp/articles/asdf-python-introduction/
- https://python-poetry.org/docs/
