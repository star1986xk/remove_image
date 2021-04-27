import sys
from ui.ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Thread import Thread


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())

        self.signals()

    def signals(self):
        self.pushButton_old.clicked.connect(lambda: self.open_file(self.lineEdit_old))
        self.pushButton_new.clicked.connect(lambda: self.open_file(self.lineEdit_new))
        self.pushButton_run.clicked.connect(self.run)

    # 槽函数-----------------------------------------------------------------------------------------------------------
    # 打开文件
    def open_file(self, lineEdit):
        try:
            filename = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
            lineEdit.setText(filename)
        except Exception as e:
            self.log.logger.warning(str(e))

    def update_label(self, msg):
        self.label.setText(msg)

    # 生成主逻辑
    def run(self):

        try:
            old_path = self.lineEdit_old.text()
            new_path = self.lineEdit_new.text()
            if not all([old_path, new_path]): return
            self.t = Thread(self, old_path, new_path)
            self.t.sig_msg.connect(self.update_label)
            self.t.finished.connect(self.t.deleteLater)
            self.t.start()
            QMessageBox.information(self, '提示', '运行完成')
        except Exception as e:
            QMessageBox.warning(self, '错误', str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
