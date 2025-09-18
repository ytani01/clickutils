import os
import pytest
import subprocess


TEST_ARCHIVE_DIR = "test_archives"
TEST_FILE_NAME = "test_file"
TEST_FILE_EXT = "md"
TEST_FILE = f"{TEST_FILE_NAME}.{TEST_FILE_EXT}"
TEST_FILE_NOTFOUND = "test_file_notfile.md"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # テスト前にアーカイブディレクトリをクリーンアップ
    if os.path.exists(TEST_ARCHIVE_DIR):
        for f in os.listdir(TEST_ARCHIVE_DIR):
            os.remove(os.path.join(TEST_ARCHIVE_DIR, f))
        os.rmdir(TEST_ARCHIVE_DIR)

    yield

    # テスト後にアーカイブディレクトリをクリーンアップ
    if os.path.exists(TEST_ARCHIVE_DIR):
        for f in os.listdir(TEST_ARCHIVE_DIR):
            os.remove(os.path.join(TEST_ARCHIVE_DIR, f))
        os.rmdir(TEST_ARCHIVE_DIR)


def test_archive_file_success():
    # テストファイルを作成
    with open(TEST_FILE, "w") as f:
        f.write("This is a test file.")

    cmdline = f"uv run archive_file.py --debug --archive-path {TEST_ARCHIVE_DIR} {TEST_FILE}"
    print()
    print()
    print(f"* cmdline = {cmdline}")

    result = subprocess.run(cmdline.split(), capture_output=True, text=True)

    print()
    print(f"* returncode = {result.returncode}")

    assert result.returncode == 0

    print()
    print(f"* stdout = {result.stdout}")

    assert f"Archived '{TEST_FILE}' to " \
           f"'{TEST_ARCHIVE_DIR}/test_file" in result.stdout
    assert not os.path.exists(TEST_FILE)  # 元のファイルは削除されているはず

    # アーカイブディレクトリにファイルが存在することを確認
    archive_files = os.listdir(TEST_ARCHIVE_DIR)
    assert len(archive_files) == 1
    assert archive_files[0].startswith(TEST_FILE_NAME)
    assert archive_files[0].endswith("." + TEST_FILE_EXT)


def test_archive_file_not_found():
    cmdline = f"uv run archive_file.py --debug --archive-path {TEST_ARCHIVE_DIR} {TEST_FILE_NOTFOUND}"
    print()
    print()
    print(f"* cmdline = {cmdline}")

    result = subprocess.run(cmdline.split(), capture_output=True, text=True)

    print()
    print(f"* returncode = {result.returncode}")
    assert result.returncode == 1

    print()
    print(f"* stderr = {result.stderr}")
    assert f"Error: File not found: {TEST_FILE_NOTFOUND}" in result.stderr
