# GraphQLのコード自動生成
## コードファーストとスキーマファースト  
GraphQLのデータモデルを表すために作成された構文をスキーマ定義言語(SDL)と言う

### コードファースト
リゾルバーとデータモデルをコード上で定義し、コードからSDLを作成する

### スキーマファースト
SDLを定義し、SDLをもとにコードを実装する

参考：https://zenn.dev/chillnn_tech/articles/15462cffcdecd3

## Strawberryでのコード自動生成
### コードからSDLを出力する（コードファースト）
strawberryのコードからSDLを出力する
以下のコマンドを実行し、schema.graphqlにSDLを出力する
```shell
strawberry export-schema graphql_api.schemas.operations.client:schema > schema.graphql
```
参考：https://strawberry.rocks/docs/guides/schema-export

### SDLからコードを出力する（スキーマファースト）
SDLからstrawberryのコードを出力する
以下のコマンドを実行し、SDLからschema.pyを出力する
```shell
strawberry schema-codegen schema.graphql > ./graphql_api/schema.py  
```
参考；https://strawberry.rocks/docs/codegen/schema-codegen
