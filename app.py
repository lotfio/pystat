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
import json
import core.Vstat as v
from   pprint import pprint


def main():
    vstat = v.Vstat()
    data  = json.loads(vstat.get_data())
    pprint(data)


if __name__ == '__main__':
    main()