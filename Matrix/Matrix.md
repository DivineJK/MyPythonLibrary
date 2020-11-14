# Matrix
行列に関するライブラリ。

## MatrixCollections
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
