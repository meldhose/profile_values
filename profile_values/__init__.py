# coding=utf-8
import sys

if sys.version_info > (3, 0):
    import importlib
    importlib.reload(sys)

    from .profile_encoding import *

    from .profile_numericalanalysis import *
    from .profile_stringanalysis import *
    from .profile_valuelengthanalysis import *

else:
    reload(sys)
    sys.setdefaultencoding("UTF-8")

    from profile_encoding import *

    from profile_numericalanalysis import *
    from profile_stringanalysis import *
    from profile_valuelengthanalysis import *
    