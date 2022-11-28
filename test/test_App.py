# import os
# import sys

# currentPosition = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.join(currentPosition, '../'))

# from src.app import index

from app import index

def test():
    assert index() == 'Hello World'
