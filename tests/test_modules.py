import pytest
import subprocess
from lmod.module import Module, get_user_collections


class TestModule:
    def test_module(self):
        ret = subprocess.run(
            "module --version",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(ret.stdout)

        mod_names = ["lmod"]
        a = Module(mod_names, debug=True)
        print(a.get_command())
        print(a.test_modules(login=True))
        assert 0 == a.test_modules(login=True)

        b = Module(mod_names, force=True)
        assert 0 == b.test_modules(login=True)

        c = Module(mod_names, debug=True)
        assert 0 == c.test_modules(login=True)

        d = Module(mod_names, purge=True)
        d.get_command()

        e = Module("lmod settarg", debug=True)
        e.get_command()

    def test_is_avail(self):
        a = Module()
        assert 0 == a.is_avail("lmod")

    def test_version(self):
        a = Module()
        a.version()

    def test_avail(self):
        a = Module(debug=True)
        a.avail()
        a.avail("lmod")

        a = Module(debug=False)
        a.avail()

    def test_collection(self):
        cmd = Module(["settarg"], debug=True)
        # save as collection name "settarg"
        cmd.save("settarg")
        # save as "default" collection
        cmd.save()
        # show "default" collection
        cmd.describe()
        # show "settarg" collection
        cmd.describe("settarg")

        assert 0 == cmd.test_collection("settarg")
        assert 0 == cmd.test_collection()

        # test if collection exists
        user_collections = get_user_collections()
        print(user_collections)
        assert "settarg" in user_collections

        cmd = Module(["lmod"], debug=False)
        cmd.save()
        cmd.describe()
        cmd.test_collection()

    @pytest.mark.xfail(
        reason="Collection Name must be string when saving", raises=TypeError
    )
    def test_type_error_save_collection(self):
        cmd = Module()
        cmd.save(1)

    @pytest.mark.xfail(
        reason="Collection Name must be string when showing content of collection",
        raises=TypeError,
    )
    def test_type_error_describe_collection(self):
        cmd = Module()
        cmd.describe(1)

    def test_get_collection(self):
        a = Module()
        assert "module restore settarg" == a.get_collection("settarg")
        assert "module restore default" == a.get_collection()

    @pytest.mark.xfail(
        reason="Type error when passing non-string argument to get_collection method",
        raises=TypeError,
    )
    def test_get_collection_type_mismatch(self):

        a = Module()
        a.get_collection(1)

    @pytest.mark.xfail(
        reason="Type error when passing non-string argument to test_collection method",
        raises=TypeError,
    )
    def test_test_collection_type_mismatch(self):

        a = Module()
        a.test_collection(1)

    @pytest.mark.xfail(
        reason="Type error when a non-string argument to Module class",
        raises=TypeError,
    )
    def test_type_error(self):
        Module(1)

    def test_modules_in_login(self):
        a = Module("lmod", debug=True)
        a.test_modules(login=True)

    def test_spider(self):
        a = Module()
        a.spider()

        a = Module("gcc")
        a.spider()
        a.spider("gcc")
        a.spider(["lmod", "settarg"])

        with pytest.raises(TypeError):
            a.spider(1)

    def test_checkSyntax(self):
        a = Module("lmod", debug=True)
        assert 0 == a.checkSyntax()

        with pytest.raises(TypeError):
            a.checkSyntax(1)

        a.checkSyntax("lmod")

        a = Module("lmod", debug=False)
        a.checkSyntax()

    def test_module_overview(self):
        # module overview
        a = Module()
        a.overview()

        # module overview lmod
        print(a.overview("lmod"))

        # module overview lmod settarg
        print(a.overview(["lmod", "settarg"]))

        # input must be string or list of strings. Passing an integer should raise TypeError
        with pytest.raises(TypeError):
            a.overview(1)

        b = Module("lmod")
        b.overview()
