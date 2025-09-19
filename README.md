# clickutils

`clickutils` は、Python の `click` ライブラリを使用したコマンドラインインターフェース (CLI) アプリケーション開発を支援するユーティリティ集です。


## == 目的

`click` を用いて CLI アプリケーションを開発する際、バージョン表示、デバッグフラグ、ヘルプ表示といった共通オプションの設定は反復的な作業となりがちです。`clickutils` は、これらの共通オプションを単一のデコレータで一括して適用可能にすることで、開発の効率化とコードの一貫性向上に貢献します。


## == 特徴

- **共通オプションの簡素化**

  バージョン、デバッグ、ヘルプといった共通の CLI オプションを、
  `click_common_opts` デコレータ一つで設定できます。

- **柔軟な設定**

  各オプションのショートカット (`-v`, `-d`, `-h`) の有効/無効を制御可能です。

- **`click` との統合**

  `click` のデコレータとして機能するため、
  既存の `click` アプリケーションに容易に組み込むことができます。


## == 参考情報

- [click: Python package for creating beautiful command line interfaces](https://github.com/pallets/click)


## == インストール

以下は、`uv`で管理された既存のプロジェクト(`myproject`)に、
本パッケージを組み込む方法です。

```bash
cd work   # `myproject`の親ディレクトリに移動

git clone https://github.com/ytani01/clickutils.git
# work/clickutils ディレクトリが作成されるので、
# 以下のようなディレクトリ構成になります。
# 
# work/
# ├── clickutils/
# └── myproject/

cd myproject  # `uv`で作られた既存のプロジェクト

uv add ../clickutils  # 相対パスで本パッケージを`add`する。
```


## == 使用方法

### === `click_common_opts` デコレータ

`click_common_opts` は、`click` コマンドやグループに共通オプションを追加するためのデコレータです。基本的な使用方法は以下の通りです。

※ **注意**
※ `click` は、個別に`import click`しないでください
※
※ 以下のように、本パッケージからインポートするようにしてください
※
※   from clickutils, import click, click_common_opts
※   click = import_click()

```python
from clickutils import click_common_opts, import_click

click = import_click()

VERSION = "1.0.0"

# CLI のトップレベルコマンドを定義
@click.group(invoke_without_command=True)
@click_common_opts(click, VERSION)
def cli(ctx, debug):
    """CLI top."""
    if debug:
        print(f"[DEBUG] command name = '{ctx.command.name}'")
        print(f"[DEBUG] sub command name = '{ctx.invoked_subcommand}'")

    print(f"Hello from {ctx.command.name}")

    if ctx.invoked_subcommand:
        log.debug("subcommand = %a", ctx.invoked_subcommand)
    else:
        print(ctx.get_help())

# サブコマンドを定義
@cli.command()
@click_common_opts(click, VERSION)
def sub1(ctx, debug):
    """Subcommand #1."""
    if debug:
        print(f"command name = '{ctx.command.name}'")

    print(f"  Hello from {ctx.command.name}")

if __name__ == '__main__':
    cli()
```

#### ==== パラメータ

- `click` 引数名固定

  `import_click()` で取得した `click`
  `import_click(async_flag=Tree)`で取得すると、内部的に`asyncclick`になる。

- `ver_str` (str, 省略可)

  バージョンオプション (`--version`, `-V`) で表示される文字列を指定します。
  省略した場合、プログラム名と、
  **本パッケージの**バージョン情報が設定されます。

- `use_h` (bool, 省略可): デフォルト = `True`

  ヘルプオプションとして、 `-h` を有効にするかどうか。
  `--help` は、常に有効。

- `use_d` (bool, 省略可): デフォルト = `True`

  デバッグオプションとして、`-d` を有効にするかどうか。
  `--debug` は、常に有効。

- `use_v` (bool, 省略可): デフォルト = `False`

  バージョンオプションとして、小文字の `-v` を有効にするかどうか。
  `--version` と `-V` は、常に有効。


### === コマンドラインでの実行例

以下のコマンドで、本パッケージの動作を確認できます。

```bash
# ヘルプの表示
clickutils --help
clickutils -h

# バージョンの表示
clickutils --version
clickutils -V
clickutils -v # `use_v=True` に設定した場合に有効

# デバッグモードでのサブコマンド実行
clickutils --debug sub1
clickutils -d sub1

# サブコマンドの実行
clickutils sub1
clickutils sub2 sub2sub
```


## ライセンス

このプロジェクトは [MIT License](LICENCE) の下で公開されています。
