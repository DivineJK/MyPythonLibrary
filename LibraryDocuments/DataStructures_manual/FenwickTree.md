# FenwickTree

## 概要
Fenwick TreeもしくはBIT(Binary Indexed Tree)と呼ばれる木構造。
一点加算、区間和の取得がどちらもO(logN)時間でできる。

## 内容
### 関数
|関数名|入力値の型|返り値の型|説明|
|:-|:-|:-|:-|
|ft_add|p: int, x: int, float...|None|p番目の要素にxを加算する。|
|ft_sum|l: int, r: int|int, float...|区間[l, r)間の和を求める。|
