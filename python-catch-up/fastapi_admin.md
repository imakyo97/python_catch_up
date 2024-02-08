# fastapi_adminのまとめ
## fields.ManyToManyField()のエラー
以下のようにFieldでtortoiseORMのModelのManyToManyFieldを画面に表示し、データをupdateしようとするとエラーが発生する。
```python
        Field(
            name="technologies",
            label="technologies",
            input_=inputs.ManyToMany(model=Technology)
        ),
```
GitHubのissuesを見ると内部実装に問題があるっぽく、直でissues通りにコードを書き換えてみたところ正常に動作するようになった。
https://github.com/fastapi-admin/fastapi-admin/issues/62

`fastapi_admin/routes/resources.py`148行目のobjを以下のように書き換える
```python
    obj = await model.get(pk=pk).prefetch_related(*model_resource.get_m2m_field())
```
