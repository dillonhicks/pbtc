from __future__ import absolute_import

import fnmatch
import pkg_resources
from subprocess import PIPE, Popen

try:
    from os import scandir
except ImportError:
    from scandir import scandir

try:
    from pathlib import Path, PurePath
except ImportError:
    from pathlib2 import Path, PurePath


__version__ = '0.0.3'
__all__ = (
    'find_files',
    'ProtobufPackage'
)


def find_files(directory, pattern):
    for entry in scandir(str(directory)):
        if entry.is_dir():
            for file in find_files(entry.path, pattern):
                yield file
        elif fnmatch.fnmatch(entry.name, pattern):
            yield Path(str(entry.path))


class ProtobufPackage(object):

    def __init__(self, name, src_dir, *options):
        self.name = name
        self.src_dir = Path(src_dir)
        self.options = options


    def compile(self):
        proto_include = pkg_resources.resource_filename('grpc_tools', '_proto')
        proto_files = [str(p.absolute()) for p in find_files(self.src_dir, '*.proto')]

        args = [
                   'python', '-m', 'grpc.tools.protoc',
                   '-I{}'.format(proto_include),
                   '-I{}'.format(self.src_dir.absolute())
               ] + list(self.options) + proto_files

        return Popen(args).wait()


    def __repr__(self):
        return '<{}(name={!r:}, src_dir={!r:})>'.format(self.__class__.__name__, self.name, self.src_dir)
