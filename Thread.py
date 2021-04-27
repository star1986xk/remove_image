import os
from hashlib import md5
from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal


class Thread(QThread):
    sig_msg = pyqtSignal(str)

    def __init__(self, parent, old_path, new_path):
        super().__init__(parent=parent)
        self.old_path = old_path
        self.new_path = new_path

    def md5_list(self, path_list):
        img_md5_list = []
        for path in path_list:
            with open(path, 'rb') as f:
                img_md5_list.append(md5(f.read()).hexdigest())
        return img_md5_list

    def get_filename_list(self, path, filename_list, name_list):
        for li in os.listdir(path):
            file = os.path.join(path, li)
            if os.path.isfile(file):
                filename_list.append(file)
                name_list.append(li.lower())
            else:
                self.get_filename_list(file, filename_list)
        return filename_list, name_list

    def check(self, new_path_list, new_name_list, old_path_list, old_name_list):
        for n, name in enumerate(new_name_list):
            self.sig_msg.emit('检测:' + new_path_list[n])
            if name in old_name_list:
                os.remove(new_path_list[n])
                self.sig_msg.emit('删除:' + new_path_list[n])

    def run(self):
        old_path_list, old_name_list = self.get_filename_list(self.old_path, [], [])
        new_path_list, new_name_list = self.get_filename_list(self.new_path, [], [])
        self.check(new_path_list, new_name_list, old_path_list, old_name_list)
