from minimock import Mock
from kaa import model

def setup_test(test):
    model.uuid = Mock('model.uuid')
    model.r = Mock('model.r')
    model.r.get.return_value = {'name' : "foo"}
    test.globs['Base'] = model.Base

setup_test.__test__ = False
