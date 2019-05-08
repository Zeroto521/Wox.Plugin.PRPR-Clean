# -*- coding: utf-8 -*-

import copy
import os
import shutil
import time
from getpass import getuser

from wox import Wox, WoxAPI

USERNAME = getuser()

PATH = r'C:\Users\{}\AppData\Local\Packages\55370laplamgor.PRPR_z94bv1n74kjxt\LocalState'.format(
    USERNAME)

LIMIT_DAYS = 7
LIMIT_TIME = LIMIT_DAYS * 24 * 60 * 60

RESULT_TEMPLATE = {
    'Title': '',
    'SubTitle': '',
    'IcoPath': 'Images/favicon.png',
}

ACTION_TEMPLATE = {
    'JsonRPCAction': {
        'method': '',
        'parameters': [],
    }
}


class Main(Wox):

    def query(self, param):
        """Wox dealing programm

        Arguments:
            param {str} -- wox window key in parameter

        Returns:
            list -- wox json list
        """
        os.chdir(PATH)

        result = []
        param = param.strip()

        counter = 0
        size = 0

        default_folder = ['Lockscreen', 'Wallpaper']
        for folder in default_folder:
            # to check folder exists or not?
            if os.path.exists(folder):
                for file in os.listdir(folder):
                    p = os.path.join(folder, file)
                    info = os.stat(p)  # to get file info

                    # compare file time
                    if time.time() - info.st_ctime > LIMIT_TIME:
                        if not os.path.isdir(p):
                            os.remove(p)  # delete file
                        else:
                            shutil.rmtree(p)  # delete folder

                        counter += 1
                        size += info.st_size

        fsize = self.btunitChange(size)
        title = "{} pictures have deleted and {} of space is freed .".format(
            counter, fsize)
        subtitle = 'Click to open the folder in window.'
        method = 'openFolder'

        result.append(self.genaction(title, subtitle, method, PATH))

        return result

    @staticmethod
    def genformat(title, subtitle=''):
        """Generate wox json data

        Arguments:
            title {str} -- as name

        Keyword Arguments:
            subtitle {str} -- additional information (default: {''})

        Returns:
            json -- wox json
        """

        time_format = copy.deepcopy(RESULT_TEMPLATE)
        time_format['Title'] = title
        time_format['SubTitle'] = subtitle

        return time_format

    @staticmethod
    def genaction(tit, subtit, method, actparam):
        """Generate wox json data with copy action

        Arguments:
            title {str} -- as name
            actparam {str} -- the paramter which need to copy

        Returns:
            json -- wox json
        """

        res = copy.deepcopy(RESULT_TEMPLATE)
        res['Title'] = tit
        res['SubTitle'] = subtit

        action = copy.deepcopy(ACTION_TEMPLATE)
        action['JsonRPCAction']['method'] = method
        action['JsonRPCAction']['parameters'] = [actparam]
        res.update(action)

        return res

    def openFolder(self, path):
        os.startfile(path)
        WoxAPI.change_query(path)

    @staticmethod
    def btunitChange(bts):
        """Make Bytes unit more Friendly to humans.

        [reference](https://www.cnblogs.com/misspy/p/3661770.html)
        """

        cutoffs = [1024**3, 1024**2, 1024**1, 0]
        labels = ['GB', 'MB', 'KB', 'B']

        for cutoff, label in zip(cutoffs, labels):
            if bts >= cutoff:
                res = "%.1f %s" % (bts / cutoff if cutoff else bts, label)
                break
        return res


if __name__ == '__main__':
    Main()
