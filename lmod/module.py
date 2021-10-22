import os
import subprocess


def get_user_collections():
    """Get all user collections that is retrieved by running ``module -t savelist``. The output
    is of type ``list`` and each entry in list is the name of the user collection.

    :return: Return all user collections
    :rtype: list
    """

    collections = "module -t savelist"
    ret = subprocess.run(
        collections,
        shell=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    output = ret.stdout.split()

    return output


class Module:
    """This is the class declaration of Module class which emulates the ``module`` command
    provided by Lmod

    Public Methods:

    avail: implements ``module avail`` option
    version: gets Lmod version by reading LMOD_VERSION
    is_avail: implements ``module is-avail`` option
    get_command: gets the ``module load`` command based on modules passed to the class
    test_modules: test the ``module load`` command based on modules passed to the class
    save: implements ``module save`` option
    describe: implements ``module describe`` option
    get_collection: gets the ``module restore`` command with the specified collection name
    test_collection: test the ``module restore`` command with the specified collection name
    """

    def __init__(self, modules=None, purge=True, force=False, debug=False):
        """Initialize method for Module class. This class can accept module names that
        can be used to load or test modules. You can tweak the behavior of how module
        command is generated such as purging of force purge modules. The debug option
        can be useful for troubleshooting.

        Parameters:

        :param modules: list of modules
        :type modules: list, optional
        :param purge: boolean to control whether to purge modules before loading
        :type purge: bool, optional
        :param force: boolean to control whether to force purge modules before loading
        :type force: bool, optional
        :param debug: debug mode for troubleshooting
        :type debug: bool, optional
        """

        self.debug = debug
        self.modules = modules

        # when no modules are passed into initializer, just return immediately
        if self.modules is None:
            return

        # catch all exceptions to argument modules. Must be of type list or string.
        if (not isinstance(modules, list)) and (not isinstance(modules, str)):
            raise TypeError(
                f"Expecting of type 'list' or 'string' for argument modules. Got of type {type(modules)}"
            )

        # if argument is a string, than use space as delimeter to get list of all modules.
        if isinstance(modules, str):
            self.modules = modules.split(" ")

        # building actual command. Note that we are doing command chaining when loading modules
        self.module_load_cmd = [f"module load {x} && " for x in self.modules]

        # remove last '&&' from module load command
        self.module_load_cmd[-1] = self.module_load_cmd[-1].replace("&&", "")

        if purge:
            # force purge modules before loading modules. Used when dealing with sticky modules
            if force:
                self.module_load_cmd = [
                    "module --force purge && "
                ] + self.module_load_cmd
            # purge modules before loading modules.
            else:
                self.module_load_cmd = ["module purge &&"] + self.module_load_cmd

    def avail(self, name=None):
        """This method implements the ``module avail`` command. The output of module avail will return available
        modules in the system. The output is returned as a list using the ``module -t avail`` which presents the
        output in a single line per module.

        Parameters:

        :param name: argument passed to ``module avail``. This is used for showing what modules are available
        :type name: str, optional

        :return: Return output of ``module avail`` as a list
        :rtype: list
        """

        cmd = "module -t avail"
        # if argument specified
        if name:
            cmd = f"module -t avail {name}"
        print(cmd)
        ret = subprocess.run(
            cmd,
            shell=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        return ret.stdout.split()

    def spider(self, name=None):
        """This method invokes ``module spider`` command. One can specify input arguments
        as a string or list type which are converted into string.

        If no arguments are specified to ``Module()`` and spider class we will return the output
        of ``module spider`` command which is a list of all modules.

        .. code-block:: python

            m = Module()
            m.spider()

        If modules are specified during instance creation then we will use those modules during module spider output.
        In this following example, we will run ``module spider gcc python``

        .. code-block:: python

            m = Module("gcc python")
            m.spider()

        We can also specify modules via spider method which will be read first even if modules are passed during object creation
        time. In example below

        .. code-block:: python

            >>> m = Module(["gcc", "python"])
            >>> m.modules
            ['gcc', 'python']
            >>> out = m.spider("gcc")
            >>> print(out)

            ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              gcc:
            ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                 Versions:
                    gcc/9.3.0-n7p74fd
                    gcc/10.2.0-37fmsw7

            ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              For detailed information about a specific "gcc" package (including how to load the modules) use the module's full name.
              Note that names that have a trailing (E) are extensions provided by other modules.
              For example:

                 $ module spider gcc/10.2.0-37fmsw7
            ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        :param name: Input modules to run ``module spider``. Input can be a string or list
        :type name: str, list
        :return: Output of ``module spider`` command as a string type
        :rtype: str

        """

        if name:
            # raise error if input is not string or list
            if not isinstance(name, (str, list)):
                raise TypeError(f"{name} must be a string or list")

            # for list items we convert each item to string and join list into a string
            if isinstance(name, list):
                name = [str(i) for i in name]
                name = " ".join(name)

            cmd = f"module spider {name}"

        elif self.modules:
            cmd = f"module spider {' '.join(self.modules)}"
        else:
            cmd = "module spider"

        ret = subprocess.run(
            cmd,
            shell=True,
            encoding="utf-8",
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        return ret.stdout

    def version(self):
        """Get Lmod version by reading environment variable ``LMOD_VERSION`` and return as a string

        :return: Return the Lmod version as a string
        :rtype: str
        """

        return os.getenv("LMOD_VERSION") or None

    def is_avail(self, name):
        """This method implements the ``module is-avail`` command which is used for checking if a module is available
        before loading it. The return value is a 0 or 1.

        Parameters:

        :param name: argument passed to ``module is-avail``. This is used for checking if module is available
        :type name: str, required

        :return: Return output of ``module is-avail``. This checks if module is available and return code is a 0 or 1
        :rtype: int
        """

        cmd = f"module is-avail {name}"

        ret = subprocess.run(
            cmd,
            shell=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        return ret.returncode

    def get_command(self):
        """Get the actual module load command that can be used to load the given modules.

        :return: return the actual module load command
        :rtype: str
        """

        return " ".join(self.module_load_cmd)

    def test_modules(self, login=False):
        """Test all modules passed to Module class by loading them using ``module load``. The default behavior
        is to run the command in a sub-shell but this can be changed to run in a new login shell if ``login=True`` is
        specified. The return value is a return code (type ``int``) of the ``module load`` command.

        Parameters:

        :param login: When ``login=True`` is set, it will run the test in a login shell, the default is to run in a sub-shell
        :type login: bool, optional

        :return: return code of ``module load`` command
        :rtype: int
        """

        cmd_executed = self.get_command()

        # run test in login shell
        if login:
            cmd_executed = 'bash -l -c "' + cmd_executed + '"'

        ret = subprocess.run(
            cmd_executed,
            shell=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        # print executed command for debugging
        if self.debug:
            print(f"[DEBUG] Executing module command: {cmd_executed}")
            print(f"[DEBUG] Return Code: {ret.returncode}")

        return ret.returncode

    def save(self, collection="default"):
        """Save modules specified in Module class into a user collection. This implements the ``module save`` command
        for active modules. In this case, we are saving modules that were passed to the Module class. If no argument
        is specified, we will save to ``default`` collection, but user can specify a collection name, in that case
        we are running ``module save <collection>``. The collection name must be of type ``str`` in order for
        this to work, otherwise an exception of ``TypeError`` will be raised.

        Parameters:

        :param collection: collection name to save modules. If none specified, ``default`` is the collection.
        :type collection: str, optional
        """

        # raise TypeError exception if collection is not a string type since that is required
        # when working with module collection
        if not isinstance(collection, str):
            raise TypeError(f"Type Error: {collection} is not of type string")

        module_save_cmd = f"{self.get_command()} && module save {collection}"

        ret = subprocess.run(
            module_save_cmd,
            shell=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        # print executed command for debugging
        if self.debug:
            print(f"[DEBUG] Executing module command: {module_save_cmd}")
            print(f"[DEBUG] Return Code: {ret.returncode}")

        print(f"Saving modules {self.modules} to module collection name: {collection}")
        print(ret.stdout)

    def describe(self, collection="default"):
        """Show content of a user collection and implements the command ``module describe``. By default, if no argument
        is specified it will resort to showing contents of ``default`` collection. One can pass a collection name
        which must be of type ``str`` that is the user collection name. Internally it will run ``module describe <collection>``.
        If collection name is not of type ``str``, then an exception of ``TypeError`` will be raised.

        Parameters:

        :param collection: name of user collection to show.
        :type collection: str, optional
        """

        # raise TypeError exception if collection is not a string type since that is required
        # when working with module collection
        if not isinstance(collection, str):
            raise TypeError(f"Type Error: {collection} is not of type string")

        module_describe_cmd = f"module describe {collection}"
        ret = subprocess.run(
            module_describe_cmd,
            shell=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        # print executed command for debugging
        if self.debug:
            print(f"[DEBUG] Executing module command: {module_describe_cmd}")
            print(f"[DEBUG] Return Code: {ret.returncode}")

        print(ret.stdout)

    def get_collection(self, collection="default"):
        """Return the module command to restore a collection. If no argument is specified, it will resort to the ``default``
        collection, otherwise one can specify a collection name of type ``str``. The output will be of type ``str``
        such as ``module restore default``. If argument to class is not of type ``str`` then an exception of type
        ``TypeError`` will be raised.

        Parameters:

        :param collection: collection name to restore
        :type collection: str, optional

        :return: return the ``module restore`` command with the collection name
        :rtype: str
        """

        # raise error if collection is not a string
        if not isinstance(collection, str):
            raise TypeError(f"Type Error: {collection} is not of type string")

        return f"module restore {collection}"

    def test_collection(self, collection="default"):
        """Test the user collection by running ``module restore`` against a collection name. This is useful, to test a
        user collection is working before using it in your scripts. If no argument is specified, it will test the
        ``default`` collection. One can specify a user collection name which must of be of type ``str`` and it must
        exist. The output will be a return code of the ``module restore`` command which would be of type ``int``.
        If argument to method is not of type ``str`` an exception of ``TypeError`` will be raised.

        Parameters:

        :param collection: collection name to test
        :type collection: str, optional

        :return: return code of ``module restore`` against the collection name
        :rtype: int
        """

        # raise error if collection is not a string
        if not isinstance(collection, str):
            raise TypeError(f"Type Error: {collection} is not of type string")

        module_restore_cmd = f"module restore {collection}"
        ret = subprocess.run(
            module_restore_cmd,
            shell=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        # print executed command for debugging
        if self.debug:
            print(f"[DEBUG] Executing command: {module_restore_cmd}")
            print(f"[DEBUG] Return Code: {ret.returncode}")

        return ret.returncode
