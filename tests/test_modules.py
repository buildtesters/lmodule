import pytest

from lmod.module import Module, get_all_collections

class TestModule:

    def test_module(self):
        mod_names = ["lmod"]
        a = Module(mod_names)
        print(a.get_command())
        assert 0 == a.test_modules()

        b = Module(mod_names, force=True)
        assert 0 == b.test_modules()

        c = Module(mod_names, debug=True)
        assert 0 == c.test_modules()


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
        user_collections = get_all_collections()
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
        reason="Type error when a non-string argument to ModuleCollection class",
        raises=TypeError,
    )
    def test_type_error(self):
        a = Module(1)