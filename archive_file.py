#
# (c) 2025 Yoichi Tanibayashi
#
import datetime
import os
import sys

from clickutils import click_common_opts, get_logger, import_click


click = import_click()


@click.command()
@click.argument('src_file', type=click.Path())
@click.option(
    '--dir', '-d', type=str,
    default='archives', show_default=True,
    help='アーカイブ先のディレクトリ'
)
@click_common_opts(click, "0.1.0", use_d=False)
def main(ctx, archivedir, src_file, debug):
    """
    指定されたファイルをアーカイブディレクトリに移動し、リネーム。
    """
    log = get_logger(__name__, debug)
    log.debug("click = %a", click.__name__)
    log.debug("command name = %a", ctx.command.name)
    log.debug("archivedir = %s/", archivedir)

    print(f"file: {src_file}")

    # ファイルの存在確認
    if not os.path.exists(src_file):
        log.error("File not found: %a", src_file)
        sys.exit(1)

    # archives ディレクトリが存在しない場合は作成
    archive_dir_to_use = archivedir
    if not os.path.exists(archive_dir_to_use):
        os.makedirs(archive_dir_to_use)
        log.warning("Created directory: %s/", archive_dir_to_use)

    # ファイル名と拡張子を分割
    base_name = os.path.basename(src_file)
    file_root, file_ext = os.path.splitext(base_name)

    log.debug(
        "base_name:%a, file_root:%a, file_ext:%a",
        base_name, file_root, file_ext
    )

    # タイムスタンプを付加
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y%m%d-%H%M")
    new_filename = f"{timestamp}-{file_root}-done{file_ext}"
    log.debug("new_filename: %a", new_filename)

    # 新しいパスを生成
    new_path = os.path.join(archivedir, new_filename)
    log.debug("new_path: %a", new_path)

    try:
        os.rename(src_file, new_path)
        print(f"Archived '{src_file}' to '{new_path}'")
    except OSError as e:
        log.error("%s: %s", type(e).__name__, e)
        sys.exit(1)

if __name__ == "__main__":
    main()
