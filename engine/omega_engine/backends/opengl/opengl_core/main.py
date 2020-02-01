import os
import sys
import importlib.util

tests_path = "test"


if __name__ == "__main__":
    args = sys.argv
    
    if len(args) > 1:
        if args[1] == "test":
            if len(args) == 3:
                file_name = args[2]
                spec = importlib.util.spec_from_file_location(f"{tests_path}.{file_name}" , os.path.join(tests_path, file_name))
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
                foo.test()
            else:
                raise Exception("invalid test input")
        else:
            raise Exception("command not found")


