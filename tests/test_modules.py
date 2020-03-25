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
        print(a.test_modules())
        assert 0 == a.test_modules()

        b = Module(mod_names, force=True)
        assert 0 == b.test_modules()

        c = Module(mod_names, debug=True)
        assert 0 == c.test_modules()

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
        a = Module()
        a.avail()
        a.avail("lmod")

    def test_collection(self):
        cmd = Module(["settarg"])
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

    def test_collection_exists(self):
        user_collections = get_user_collections()
        print(user_collections)
        assert "settarg" in user_collections

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
        a = Module(1)

    def test_modules_in_login(self):
        a = Module("lmod", debug=True)
        a.test_modules(login=True)
