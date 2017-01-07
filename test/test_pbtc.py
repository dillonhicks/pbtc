

from pbtc import ProtobufPackage




class TestProtobufPackage(object):

    def test_compile(self):

        pkg = ProtobufPackage(
                "protobuftoolchain.v1", ".",
                "--descriptor_set_out=./test/srcinfo.descriptor",
                "--include_source_info",
                "--include_imports",
                "--python_out=.")

        assert pkg.compile() == 0
