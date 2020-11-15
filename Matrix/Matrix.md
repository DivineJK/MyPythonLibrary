# Matrix
行列に関するライブラリ。

## MatrixCollections
行列演算詰め合わせ。

matrix型 = list[list[(int, float, ...)]]
### クラスオブジェクト
|名称|型|概要|
|:--|:--|:--|
|number_type|set|matrixにのせる型を定義。|
### 関数
|名称|引数|返り値|概要|
|:--|:--|:--|:--|
|MatrixCollection|set additional_type=set()|None|行列ライブラリ。additional_typeに型を追加することもある。|
|zeros|int n, int m|matrix|ゼロ行列。|
|identity|int n|matrix|単位行列。|
|inved|int a, int mod|int|aの逆元。|
|ismatrix|? a|bool|引数が正しい行列かどうかを返す。|
|mat_sum|matrix a, matrix b, int weight=1, int modulo=0|matrix|行列の和を返す。|
|mat_prod|matrix a, matrix b, int modulo=0|matrix|行列の積を返す。|
|mat_inv|matrix a, int modulo=0|matrix|逆行列を返す。|
|mat_pow|matrix a, int m, int modulo=0|matrix|行列の累乗を返す。|
|kronecker_product|matrix a, matrix b, int modulo=0|matrix|行列のクロネッカー積を返す。|
### zeros

整数<img src="https://latex.codecogs.com/gif.latex?n" title="n" />, <img src="https://latex.codecogs.com/gif.latex?m" title="m" />に対し、<img src="https://latex.codecogs.com/gif.latex?n\times&space;m" title="n\times&space;m" />ゼロ行列を返す。

### identity
整数<img src="https://latex.codecogs.com/gif.latex?n" title="n" />に対し、<img src="https://latex.codecogs.com/gif.latex?n" title="n" />次単位行列を返す。

### inved
整数<img src="https://latex.codecogs.com/gif.latex?n" title="n" />の<img src="https://latex.codecogs.com/gif.latex?\mathrm{mod}" title="\mathrm{mod}" />に対する逆元を返す。

### ismatrix
行列の型チェックを行う。

【排除対象】
<ol>
  <li>引数がlist型でない。</li>
  <li>listの各要素がlist型でない。</li>
  <li>各行の長さが等しくない。</li>
  <li>各要素の型が指定された型の中にない。</li>
</ol>

### mat_sum
行列<img src="https://latex.codecogs.com/gif.latex?a" title="a" />, <img src="https://latex.codecogs.com/gif.latex?b" title="b" />に対し、行列の和<img src="https://latex.codecogs.com/gif.latex?a+b" title="a+b" />を返す。正当な行列でないか、行列のサイズが正しくなければエラーを返す。
