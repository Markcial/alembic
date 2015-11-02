from minimock import Mock
from kaa.model import Identifier

def globs(globs):
    uuid = Mock('uuid')
    uuid.uuid4.mock_returns = "some-random-uuid"
    globs['uuid'] = uuid
    globs['Identifier'] = Identifier
    return globs
