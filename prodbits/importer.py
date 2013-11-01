import os
import sys
import imp
import json


class Loader:

    def get_settings_from_json(self, path):
        with open(path) as fp:
            return json.load(fp)

    def get_settings_from_py(self, path):
        g = {}
        l = {}
        execfile(path, g, l)
        return g

    def get_settings_from_dir(self, path):
        p = os.path.join(path, "settings.json")
        if os.path.exists(p):
            return self.get_settings_from_json(p)

        p = os.path.join(path, "settings.py")
        if os.path.exists(p):
            return self.get_settings_from_py(p)

    def find_settings(self):
        for d in [os.path.join(sys.prefix, "etc")]:
            settings = self.get_settings_from_dir(d)
            if settings:
                return settings
        raise ImportError("django_prodbits can't find any settings")

    def load_module(self, fullname):
        try:
            return sys.modules[fullname]
        except KeyError:
            pass

        m = imp.new_module(fullname)
        m.__file__ = "django_prodbits:" + fullname
        m.__path__ = []
        m.__loader__ = self

        for k, v in self.find_settings().items():
            setattr(m, k, v)

        sys.modules.setdefault(fullname, m)
        return m

class Finder:
    def find_module(self, fullname, path=None):
        if fullname.startswith("prodbits.settings"):
            return Loader()
        return None


__path__ = []
sys.meta_path.append(Finder())

