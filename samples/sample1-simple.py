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

from clickutils import click_common_opts


@click.command()
@click_common_opts()
def main(ctx, debug):
    print("Hello, world!")

    if debug:
        print(f"[DEBUG] command.name = '{ctx.command.name}'")

if __name__ == "__main__":
    main()
