#
# シンプルなサンプル
#
#   これだけで、以下のオプションが使えるようになります。
#
"""
Options:
  -V, --version  Show the version and exit.
  -d, --debug    debug flag
  -h, --help     Show this message and exit.
"""
import click

from click_utils import click_common_opts


@click.command()
@click_common_opts(ver_str="v1.2.3")
def main(ctx, debug):
    print(f"Hello, world!")

    if debug:
        print(f"[DEBUG] command.name = '{ctx.command.name}'")

if __name__ == "__main__":
    main()
