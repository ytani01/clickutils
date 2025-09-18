#
# (c) 2025 Yoichi Tanibayashi
#
import click
import os
import datetime

from click_utils import click_common_opts, get_logger

@click.command()
@click_common_opts()
@click.argument('target_file', type=click.Path(exists=True))
def main(ctx, debug, target_file):
    """
    指定されたファイルをリネームします。
    """
    log = get_logger(__name__, debug)
    log.debug("command name = %a", ctx.command.name)

    print(f"Target file: {target_file}")

    # ここにリネーム処理を実装します
    # 例: タイムスタンプを付加してリネーム
    base, ext = os.path.splitext(target_file)
    timestamp = datetime.datetime.now().strftime("-%Y%m%d-%H%M%S")
    new_file_name = f"{base}{timestamp}{ext}"

    try:
        os.rename(target_file, new_file_name)
        print(f"Renamed '{target_file}' to '{new_file_name}'")
    except OSError as e:
        log.error(f"Error renaming file: {e}")
        print(f"Error: Could not rename file '{target_file}'.")

if __name__ == "__main__":
    main()