'''
*+----------------------------------------------
*| This file is part of VstatPy application
*|
*| @package     VstatPy Vatsim statistics python
*| @author      <lotfio lakehal>
*| @license     MIT
*| @version     0.1.0
*| @copyright   2019 lotfio lakehal
*+----------------------------------------------
'''

from urllib.request import urlopen
from core.conf import url

class Vstat:

    def __init__(self):
        ''' initialize '''
        self.req = urlopen(url)

    def get_data(self):
        ''' get data '''
        return self.req.read()