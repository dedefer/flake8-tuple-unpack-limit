from typing import Tuple, Iterator
import ast

__version__ = '0.0.1'


class TupleUnpackLimitChecker:
    name = 'flake8-tuple-unpack-limit'
    version = __version__

    default_max_unpack_length = 4
    max_unpack_length = default_max_unpack_length

    _error_message_template = 'TUL001 unpack too many variables ({0} > {1})'

    def __init__(self, tree: ast.AST):
        self.tree = tree

    def run(self) -> Iterator[Tuple[int, int, str, type]]:
        for node in ast.walk(self.tree):
            if (
                isinstance(node, ast.Assign) and
                isinstance(node.targets[0], ast.Tuple) and
                len(node.targets[0].elts) > self.max_unpack_length
            ):
                tup: ast.Tuple = node.targets[0]
                yield (
                    tup.lineno,
                    tup.col_offset,
                    self._error_message_template.format(
                        len(tup.elts), self.max_unpack_length,
                    ),
                    type(self),
                )

    @classmethod
    def add_options(cls, parser) -> None:
        parser.add_option(
            '--max-unpack-length',
            type=int,
            parse_from_config=True,
            default=cls.default_max_unpack_length,
        )

    @classmethod
    def parse_options(cls, options) -> None:
        cls.max_unpack_length = int(options.max_unpack_length)
