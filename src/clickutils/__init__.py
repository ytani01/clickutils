#
# (c) 2025 Yoichi Tanibayashi
#

# 重要: 下記、コメントの ``type: ...`` は、mypy対策で必要
try:
    import asyncclick as click  # type: ignore[import]
except ImportError:
    import click as click  # type: ignore[no-redef]

from .clickutils import click_common_opts
from .my_logger import get_logger
from .version import __version__


__all__ = [
    "__package__",
    "__version__",
    "click",
    "click_common_opts",
    "get_logger",
]
