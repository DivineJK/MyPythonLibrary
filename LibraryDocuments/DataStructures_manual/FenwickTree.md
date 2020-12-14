# FenwickTree

## 概要
Fenwick TreeもしくはBIT(Binary Indexed Tree)と呼ばれる木構造。
一点加算、区間和の取得がどちらもO(logN)時間でできる。

## 注意点
数列の添字は1-indexedとする。

## 内容
### クラスオブジェクト
|オブジェクト名|型|説明|
|:--|:--|:--|
|n|int|Fenwick treeの大きさ。|
|ft|list[n+1]|Fenwick tree。|
### クラス関数
|関数名|入力値の型|返り値の型|説明|
|:-|:-|:-|:-|
|ft_add|p: int, x: int, float...|None|p番目の要素にxを加算する。|
|ft_sum|x: int|int, float...|区間[1, x]間の和を求める。|
