# import order of the fixtures matter:
from test_03 import *

# dependency_2 from test_03 is overridden as dependency_2 from test_01 is now
# imported later. It doesn't matter that in test_01, the scope is session.
# The scope from the latest definition of the fixture is actually applied when
# imported from conftest.py
from test_01 import *
from test_02 import *

#: Example:
# from test_01 import *
# from test_02 import *
# from test_03 import *

# test_04 gets the dependency_2 fixture from test_03, as it is imported latest,
# with the function scope from test_03


#: Example:
# from test_03 import *
# from test_02 import *
# from test_01 import *

# test_04 gets the dependency_2 fixture from test_01, as it is imported latest,
# with the session scope from test_03. In test_03 however, the local definition
# of the fixture is used
