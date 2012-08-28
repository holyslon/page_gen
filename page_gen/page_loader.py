import glob
import os
import imp
from Page import Page


class PageLoader:

    def __init__(self, root_folder):
        def create_page(page_file):
            folder_path, _ = os.path.split(os.path.abspath(page_file))
            _, folder_name = os.path.split(folder_path)
            print "file %s, name %s" % (page_file, folder_name)
            mod_name, file_ext = os.path.splitext(os.path.split(page_file)[-1])

            if file_ext.lower() == '.py':
                py_mod = imp.load_source(mod_name, page_file)
            elif file_ext.lower() == '.pyc':
                py_mod = imp.load_compiled(mod_name, page_file)

            def read_file(file_name):
                with open(os.path.join(folder_path, file_name), "r") as f:
                    return f.read()
            text = read_file(getattr(py_mod, "path_to_text", "text.md"))
            name = getattr(py_mod, "name")
            return Page(text, name, folder_name)

        self.pages = [create_page(page_file) for page_file in glob.iglob("%s/*/meta.py" % root_folder)]



