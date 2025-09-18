import os
import pytest
from click.testing import CliRunner
from click_utils import get_logger
from archive_file import main as archive_file_main

# テスト用のアーカイブディレクトリ
TEST_ARCHIVE_DIR = "test_archives"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # テスト前にアーカイブディレクトリをクリーンアップ
    if os.path.exists(TEST_ARCHIVE_DIR):
        for f in os.listdir(TEST_ARCHIVE_DIR):
            os.remove(os.path.join(TEST_ARCHIVE_DIR, f))
        os.rmdir(TEST_ARCHIVE_DIR)
    
    # テスト実行
    yield

    # テスト後にアーカイブディレクトリをクリーンアップ
    if os.path.exists(TEST_ARCHIVE_DIR):
        for f in os.listdir(TEST_ARCHIVE_DIR):
            os.remove(os.path.join(TEST_ARCHIVE_DIR, f))
        os.rmdir(TEST_ARCHIVE_DIR)

def test_archive_file_success():
    runner = CliRunner()
    test_file_name = "test_file.txt"
    
    # テストファイルを作成
    with open(test_file_name, "w") as f:
        f.write("This is a test file.")

    result = runner.invoke(archive_file_main, ["--debug", "--archive-path", TEST_ARCHIVE_DIR, test_file_name])
    assert result.exit_code == 0
    assert f"Archived '{test_file_name}' to '{TEST_ARCHIVE_DIR}/test_file" in result.output
    assert not os.path.exists(test_file_name) # 元のファイルは削除されているはず

    # アーカイブディレクトリにファイルが存在することを確認
    archive_files = os.listdir(TEST_ARCHIVE_DIR)
    assert len(archive_files) == 1
    assert archive_files[0].startswith("test_file")
    assert archive_files[0].endswith(".txt")

def test_archive_file_not_found():
    runner = CliRunner()
    non_existent_file = "non_existent_file.txt"
    result = runner.invoke(archive_file_main, ["--debug", "--archive-path", TEST_ARCHIVE_DIR, non_existent_file])
    assert result.exit_code == 1 # ファイルが見つからない場合はエラー終了
    assert f"Error: File '{non_existent_file}' not found." in result.output

