#
#  独自の引数やオプションを加えるサンプル
#
import click

from click_utils import click_common_opts


@click.command()
@click.argument("arg1")
@click.option("--opt1", "-o", type=str)
@click_common_opts(ver_str="v1.2.3")
def main(ctx, arg1, opt1, debug):
    print(f"arg1 = '{arg1}', opt1 = '{opt1}'")

    if debug:
        print(f"[DEBUG] command.name = '{ctx.command.name}'")

if __name__ == "__main__":
    main()
