# VSCodeでStrawberryの静的型チェッカーを設定
StrawberryではMyPyとPylance（VSCode拡張）の静的型チェッカーがサポートされている  
VSCodeを使用しているため、Pylanceで静的型チェッカーを設定する  
1. VSCodeにPylanceの拡張機能をインストールする
2. setting.jsonに以下の設定を追加し、型チェックを有効にする
```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic"
}
```

参考: https://strawberry.rocks/docs/editors/vscode


# GraphQLでのデータ取得を定義
サーバーからのデータ取得にはQueryを使用する  
`@strawberry.type`のデコレータがついた`Query`クラスを定義し、strawberryのSchema作成時にguery引数に渡す
```python
def get_name() -> str:
    return "Strawberry"
 
 
@strawberry.type
class Query:
    name: str = strawberry.field(resolver=get_name)
 
 
schema = strawberry.Schema(query=Query)

```

参考: https://strawberry.rocks/docs/general/queries


# GraphQLでのデータ作成、更新、削除を定義
Queryではデータ取得を定義するが、サーバーのデータを更新したり、サーバーに副作用を引き起こす操作をする場合は`Mutations`を使用する  
`@strawberry.type`のデコレータがついた`Mutation`クラスを定義し、strawberryのSchema作成時にmutation引数に渡す
```python
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f"Adding {title} by {author}")
 
        return Book(title=title, author=author)
 
 
schema = strawberry.Schema(query=Query, mutation=Mutation)

```

参考: https://strawberry.rocks/docs/general/mutations

### 入力の型を定義してMutationで使用する
graphqlのスキーマにはプライマリーキー用のIDなどが含まれるが、IDはデータ作成時にサーバー側で自動作成するため、データ作成時のリクエストには不要である  
そのような不要なものを除くために入力専用の入力型を定義して使用する  
入力型は`@strawberry.input`のデコレータを使って定義する
```python
@strawberry.input
class Point2D:
    x: float
    y: float

@strawberry.type
class Mutation:
    @strawberry.mutation
    def store_point(self, a: Point2D) -> bool:
        return True

```

参考: https://strawberry.rocks/docs/types/input-types

# データを返す関数を定義
`Resolver`というデータを返す関数をフィールド定義に渡すことで、レスポンスを返すことができる  
リゾルバーを定義する方法は以下の2つがある
1. `strawverry.field(resolver:)`を使って定義する方法
```python
def get_last_user() -> User:
    return User(name="Marco")
 
 
@strawberry.type
class Query:
    last_user: User = strawberry.field(resolver=get_last_user)

```
2. `@strawberry.field`のデコレータをつけて定義する方法
```python
@strawberry.type
class Query:
    @strawberry.field
    def last_user(self) -> User:
        return User(name="Marco")

```

### リゾルバーに引数がある場合
リゾルバーに引数がある場合は`@strawberry.field`のデコレータをつけて定義する
```python
@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: Optional[str] = None) -> str:
        if name is None:
            return "Hello world!"
        return f"Hello {name}!"

```
リクエスト時には以下のようなクエリを使用する
```graphql
{
    hello(name: "太郎")
}

# 上記もしくは、複数リクエストする場合は以下

{
  unset: hello
  null: hello(name: null)
  name: hello(name: "Dominique")
}
```

参考: https://strawberry.rocks/docs/types/resolvers
