---
title: "Go os"
date: 2024-03-01T16:10:58+09:00
draft: false
tags: ["Go", "os"]
categories: ["usage & config"]
---
## 概要

* ファイル操作を中心にosパッケージの使用方法を記載する。

## ファイル操作

| 関数 | 説明 |
| --- | --- |
| `os.Create(name string) (*File, error)` | 新しいファイルを作成する|
| `os.Open(name string) (*File, error)` | 読み取り専用でファイルを開く |
| `MkdirAll(path string , perm FileMode ) erro` |指定されたディレクトリを作成する。親ディレクトリがない場合は親とともにディレクトリを作成する。|
| `os.ReadDir(name string) ([]DirEntry, error)` | 指定されたディレクトリ内にあるファイル名を取得する |
| `os.Remove(name string) error` | 指定された名前のファイルまたはディレクトリを削除する |
| `os.Rename(oldpath, newpath string) error` | ファイル名を変更する |

【補足】

* `os.File`はファイルを表す構造体で、`io.Reader`および`io.Writer`インターフェースを満たしており、読み書きができる
* `DirEntry`構造体は以下の関数を使用してディレクトリ名を取得できる

```Go
type DirEntry interface {
    Name() string
    // 以下省略
}

```

## ファイル/ディレクトリ属性

| 関数 | 説明 |
| --- | --- |
| `Stat(name string) (FileInfo, error)` | 指定されたファイルの情報を取得する |
| `Chmod(name string, mode FileMode) error` | ファイルのモードを変更する |
| `Chown(name string, uid, gid int) error` | ファイルの所有者を変更する |

【補足】

* `FileInfo`構造体は以下の関数を使用してファイル情報を取得できる

```Go
type FileInfo interface {
	Name() string       // ファイル名 (ディレクトリ名を除く)
	Size() int64        // ファイルサイズ
	Mode() FileMode     // ファイルモード (0xxxの形式)
	ModTime() time.Time // 変更日時
	IsDir() bool        // ディレクトリかどうかを表すフラグ
	Sys() any           // ???
}
```

## 環境変数

| 関数 | 説明 |
| --- | --- |
| `Getenv(key string) string` | 環境変数の値を取得する |
| `Setenv(key, value string) error` | 環境変数を設定する |
| `LookupEnv(key string) (string, bool)` | 環境変数が設定されているかを確認し、設定されていればその値を返す|
| `Unsetenv(key string) error` | 環境変数を削除する |

## 参考

* [公式ドキュメント](https://pkg.go.dev/os)
