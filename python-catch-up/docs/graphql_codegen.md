# GraphQLのコード自動生成
## コードファーストとスキーマファースト  
GraphQLのデータモデルを表すために作成された構文をスキーマ定義言語(SDL)と言う

### コードファースト
リゾルバーとデータモデルをコード上で定義し、コードからSDLを作成する

### スキーマファースト
SDLを定義し、SDLをもとにコードを実装する

### fastapiに対応するGraphQLライブラリ
今回使用しているstrawberryはコードファーストなGraphQLライブラリであるため、SDLからschemaコードをうまく自動生成することができない。  
SDLからschemaコードの自動生成はできるが、リゾルバーとの連携がうまくできないため生成されたコードに対して追記する形でリゾルバーを書く必要がある。

他ライブラリの [ariadne](https://ariadnegraphql.org/) は、スキーマファーストなライブラリでSDLからschemaコードを作成でき、リゾルバーとの連携もうまくできそう。

参考
- https://zenn.dev/chillnn_tech/articles/15462cffcdecd3
- https://fastapi.tiangolo.com/how-to/graphql/#graphql-libraries
- https://strawberry.rocks/docs/general/schema-basics#schema-basics


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
