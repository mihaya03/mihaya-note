---
title: "Go encoding/json"
date: 2024-02-17T20:16:36+09:00
draft: false
---

## encoding/jsonパッケージの使い方

### 概要

* encoding/jsonパッケージは、JSONデータのエンコード（Go構造体→JSON）とデコード（JSON→Go構造体）を行うための関数と型を提供する

### インメモリを扱うEncoding/Decoding

* `func Marshal(v any) ([]byte, error)`
  * Go構造体のフィールド名をkey、フィールドの値をvalueとしたJSONにエンコードする
    * keyの値は`string型`である必要がある
    * フィールドの値がポインタ型の場合、ポインタが指す値がエンコードされる
    * 構造体のフィールドのうち、大文字で始まる変数のみがエンコードの対象となる
    * SONのkey名称は、Go構造体のフィールドに指定されたjsonタグを優先し、存在しない場合はフィールド名を使用する

* `func Unmarshal(data []byte, v any) error`
  * JSONデータをGo構造体にデコードする
  * JSONデータのkeyの名称とGo構造体のフィールド名の対応は下記の優先順位で定義される
    * jsonタグの値と一致するGo構造体のフィールド名
    * Go構造体のフィールドの名称（大文字小文字は区別しない）

### ストリームを扱うEncoding/Decoding

JSONを扱うReaderとWriterを使用する

* Reader: `json.Endoer`
  * `func NewEncoder(w io.Writer) *Encoder`
    * 指定されたio.WriterにJSONを書き込むためのエンコーダを作成する
  * `func (enc *Encoder) Encode(v any) error`
    * JSON形式でエンコードし、それをストリームに書き込む
* Writer: `json.Decoder`
  * `func NewDecoder(r io.Reader ) *Decoder`
    * 指定されたio.ReaderからJSONを読み込むためのデコーダを作成する
  * `func (dec *Decoder) Decode(v any) error`
    * JSONを引数のGo構造体にデコードする
    
### 参考

* [JSON and Go](https://go.dev/blog/json)
* [jsonのドキュメント](https://pkg.go.dev/encoding/json)