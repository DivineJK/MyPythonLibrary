# Fenwick Tree

## 概要
Fenwick TreeもしくはBIT(Binary Indexed Tree)と呼ばれる木構造。
一点加算、区間和の取得がどちらもO(logN)時間でできる。

## 内容
### クラスオブジェクト
|オブジェクト名|型|説明|
|:--|:--|:--|
|n|int|Fenwick treeの大きさ。|
|ft|list\<number\>(n+1)|Fenwick tree。|
### クラス関数
|関数名|引数の型|返り値の型|説明|
|:-|:-|:-|:-|
|ft_add|p: int, x: number|None|p番目の要素にxを加算する。|
|ft_sum|x: int|number|区間\[0, x\)の和を求める。|
|get_segment|l: int, r: int|number|区間\[l, r\)の和を求める。|

## 時間計算量
<ul>
  <li>構築: O(NlogN)</li>
  <li>一点更新: O(logN)</li>
  <li>区間和の取得: O(logN)</li>
</ul>

## 使用方法
<ol>
  <li>ft = fenwick_tree(n, initial)で構築する。数列はinitialで初期化される。initialを指定しない場合、全ての要素は0で初期化される。</li>
  <li>ft.ft_add(p, x)で一点加算を行う。</li>
  <li>ft.get_segment(l, r)で区間和を取得できる。</li>
</ol>

## 使用上の注意点
<ul>
  <li>initialの長さはnに一致させる。そうしない場合、Runtime Errorとなる場合がある。</li>
</ul>
