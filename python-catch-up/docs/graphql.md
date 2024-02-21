# VSCodeでStrawberryの静的型チェッカーを設定
StrawberryではMyPyとPylance（VSCode拡張）の静的型チェッカーがサポートされている  
VSCodeを使用しているため、Pylanceで静的型チェッカーを設定する  
1. VSCodeにPylanceの拡張機能をインストールする
2. setting.jsonに以下の設定を追加し、型チェックを有効にする
```
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic"
}
```

参考: https://strawberry.rocks/docs/editors/vscode
