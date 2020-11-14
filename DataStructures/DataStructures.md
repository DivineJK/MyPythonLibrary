# DataStructures
データ構造いろいろ。

## UnionFind
みんな大好きUnionFind。

||引数|返り値|概要|
|:---|:---|:---|:---|
|class union_find|int n|None|self.parとかself.sizeとか。|
|root|int x|int |xの根を返す。|
|same|int x, int y|bool|xとyの根が同じかの判定。|
|unite|int x, int y|None|グラフをなんかいい感じにくっつける。|

### 

## segtree
ふつうのセグメントツリー。二分探索つき。
||引数|返り値|概要|
|:---|:---|:---|:---|
|class segment_tree|int n, function op, ? identity, function upd, |None|セグ木づくり。|
|update|int p, x|None|pで指定される要素をupd(segtree[p], x)に更新。|
|get_segment|int l, int r|type(op(a, b))|区間[l, r)の和を返す。|
|unite|int　lower, inr upper, val|int|区間[lower、upper)の中でval以上となる最小の添字を返す。|
