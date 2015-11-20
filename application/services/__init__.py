from ..configuration import storage_folder
import os
from uuid import uuid4


def create_snapshot_directory():
    folder = storage_folder + os.path.sep + str(uuid4())
    os.makedirs(folder)

    return folder