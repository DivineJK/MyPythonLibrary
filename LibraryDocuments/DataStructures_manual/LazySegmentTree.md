# Lazy Segment Tree
## 概要
遅延評価付きセグメントツリー。

## 内容
Tをセグメントツリーに乗せる要素の型、Sを要素更新の型とする。
### クラスオブジェクト
|名称|型|説明|
|:--|:--|:--|
|n|int|セグ木にのせる列の大きさ。|
|cnt|int|セグ木の深さ。|
|bin_top|int|セグ木最深部の長さ。|
|segtree|list\<T\>(2 * bin_top)|セグメントツリー本体。|
|subtree|list\<S\>(2 * bin_top)|遅延の木。|
|zone|list\<int\>(2 * bin_top)|区間の長さ。|
|op|function(a: T, b: T) -> ab: T|二項演算。|
|identity|T|二項演算opの単位元。|
|upd|function(lg: int, x: S, a: T) -> x[lg]\(a\): T|区間更新の演算。|
|upd_id|T|区間更新の演算の単位元。|
|renew|function(S, S) -> S|遅延部分の更新の演算。|
### クラス関数
|名称|引数の型|返り値の型|説明|
|:--|:--|:--|:--|
|get_lower|l: int, r: int|list\<int\>(?)|\[l, r\)の更新について、更新するべきセグ木の区間を返す。|
|update|l: int, r: int, x: S|None|区間\[l, r\)をxで更新。|
|get_segment|l: int, r: int|T|区間\[l, r\)の区間積を返す。|

## 追加説明
### 二項演算opについて
a, b, cをセグ木にのせる要素とすると、op(op(a, b), c) = op(a, op(b, c))が成り立たなければならない。

のせられる演算の例
|名称|単位元|
|:--|:--|
|max|-INF|
|min|INF|
|gcd|0|
|xor|0|
|or|0|
|and|(1<<INF)-1|
|足し算|0|
|掛け算|1|

## 時間計算量
<ul>
    <li>構築: O(nlogn)</li>
    <li>更新: O(logn)</li>
    <li>区間積の取得: O(logn)</li>
</ul>

## 使用方法
<ol>
    <li>二項演算op、区間更新の演算upd、遅延部分の更新の演算renewを定義する。</li>
    <li>lst = lazy_segment_tree(n, op, identity, upd, upd_id, renew, initial)で構築。initial==[]のときは、要素はidentityで更新される。</li>
    <li>lst.update(l, r, x)で区間[l, r)をxによって更新。</li>
    <li>lst.get_segment(l, r)で区間[l, r)の区間積を取得。</li>
</ol>

## 使用上の注意点
<ul>
    <li><s>ACLBC-Eが解けません。</s> ACLBC-Eを通せました。(更新：2020/12/25)</li>
</ul>
