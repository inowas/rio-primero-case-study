import flopy.modflow as mf


class RchAdapter:
    _data = None

    def __init__(self, data):
        self._data = data

    def validate(self):
        # should be implemented
        # for key in content:
        #   do something
        #   return some hints
        pass

    def is_valid(self):
        # should be implemented
        # for key in content:
        #   do something
        #   return true or false
        return True

    def merge(self):
        default = self.default()
        for key in self._data:
            default[key] = self._data[key]
        return default

    def get_package(self, _mf):
        content = self.merge()
        return mf.ModflowRch(
            _mf,
            **content
        )

    @staticmethod
    def default():
        return {
            "nrchop": 3,
            "ipakcb": None,
            "rech": 0.001,
            "irch": 0,
            "extension": 'rch',
            "unitnumber": None,
            "filenames": None,
        }

    @staticmethod
    def read_package(package):
        return {
            "nrchop": package.nrchop,
            "ipakcb": package.ipakcb,
            "rech": package.rech,
            "irch": package.irch,
            "extension": package.extension,
            "unitnumber": package.unitnumber
        }
