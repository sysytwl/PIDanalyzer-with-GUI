from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QThread, QMutex, pyqtSignal
from PyQt5 import QtCore, QtWidgets
import os
import analyzer
import sys
import time


noise_bounds = [[1.,10.1],[1.,100.],[1.,100.],[0.,4.]]

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 407)
        self.PIDanalyzer = QtWidgets.QWidget(MainWindow)
        self.PIDanalyzer.setObjectName("PIDanalyzer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PIDanalyzer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        #self.checkBox_3 = QtWidgets.QCheckBox(self.PIDanalyzer)
        #self.checkBox_3.setObjectName("checkBox_3")
        #self.gridLayout_3.addWidget(self.checkBox_3, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        #self.checkBox = QtWidgets.QCheckBox(self.PIDanalyzer)
        #self.checkBox.setObjectName("checkBox")
        #self.gridLayout_3.addWidget(self.checkBox, 4, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.PIDanalyzer)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 3, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.PIDanalyzer)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.PIDanalyzer)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.PIDanalyzer)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.PIDanalyzer)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.PIDanalyzer)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 100.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 4, 6, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox_4.setDecimals(1)
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_4.setProperty("value", 1.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 3, 6, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox_6.setDecimals(1)
        self.doubleSpinBox_6.setSingleStep(0.1)
        self.doubleSpinBox_6.setProperty("value", 1.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 3, 4, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox_7.setDecimals(1)
        self.doubleSpinBox_7.setSingleStep(0.1)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout.addWidget(self.doubleSpinBox_7, 3, 8, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox_5.setDecimals(1)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.setProperty("value", 100.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 4, 4, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setProperty("value", 10.1)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 4, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setProperty("value", 1.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 3, 2, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.PIDanalyzer)
        self.doubleSpinBox_8.setDecimals(1)
        self.doubleSpinBox_8.setSingleStep(0.1)
        self.doubleSpinBox_8.setProperty("value", 4.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout.addWidget(self.doubleSpinBox_8, 4, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.PIDanalyzer)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 8, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 3, 2, 1, 1)
        #self.progressBar = QtWidgets.QProgressBar(self.PIDanalyzer)
        #self.progressBar.setProperty("value", 24)
        #self.progressBar.setObjectName("progressBar")
        #self.gridLayout_3.addWidget(self.progressBar, 4, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.PIDanalyzer)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.PIDanalyzer)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.PIDanalyzer)

        self.retranslateUi(MainWindow)
        
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox_8.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox_7.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox_4.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox_5.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox_6.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox_3.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.doubleSpinBox_2.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.noise_bounds)
        
        #self.checkBox_3.toggled['bool'].connect(self.lineEdit_2.setDisabled)
        #self.checkBox_3.toggled['bool'].connect(self.pushButton_2.setDisabled)
        #self.checkBox_3.toggled['bool'].connect(self.tmp)
        
        self.pushButton.clicked.connect(self.getopenfilename)
        
        self.pushButton_2.clicked.connect(self.getsavefilename)
        
        self.pushButton_3.clicked.connect(self.textBrowser.clear)
        self.pushButton_3.clicked.connect(self.start)
        
        #self.checkBox.toggled['bool'].connect(self.show)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIDAnalyzer"))
        #self.checkBox_3.setText(_translate("MainWindow", "自动生成文件夹"))
        self.label_2.setText(_translate("MainWindow", "文件："))
        #self.checkBox.setText(_translate("MainWindow", "完成时打开"))
        self.checkBox_2.setText(_translate("MainWindow", "自动比例"))
        self.pushButton.setText(_translate("MainWindow", "浏览"))
        self.pushButton_2.setText(_translate("MainWindow", "浏览"))
        self.label_3.setText(_translate("MainWindow", "生成文件的位置:"))
        self.label.setText(_translate("MainWindow", "噪声强弱的比例尺:"))
        self.label_6.setText(_translate("MainWindow", "D-term"))
        self.label_5.setText(_translate("MainWindow", "Debug"))
        self.label_9.setText(_translate("MainWindow", "Max:"))
        self.label_8.setText(_translate("MainWindow", "Min:"))
        self.label_4.setText(_translate("MainWindow", "Gyro"))
        self.label_7.setText(_translate("MainWindow", "Log"))
        self.pushButton_3.setText(_translate("MainWindow", "分析"))

    def getopenfilename(self): #get the file
        #global path
        
        openfilename = QtWidgets.QFileDialog.getOpenFileName(self.PIDanalyzer, "浏览", "./", "BBL files (*.BBL)")
        #path = openfilename[0]
        self.lineEdit.setText(openfilename[0])
    
    def getsavefilename(self): #get the place for saving
        #global plot_name
        
        savefilename = QtWidgets.QFileDialog.getExistingDirectory(self.PIDanalyzer, "浏览")
        #plot_name = savefilename
        self.lineEdit_2.setText(savefilename)
        
    def show(self,status): #show the pic when finished or not
        global show
        
        if status:
            show = 'Y'
        else:
            show = 'N'
        
    def noise_bounds(self,status): #auto or manual noise_bounds
        global noise_bounds
        
        if status:
            noise_bounds = 'auto'
        else:
            noise_bounds = ''
        
    def status(self,status):
        if status:
            self.textBrowser.append('开始...')
        else:
            self.textBrowser.append('完成。')
            self.thread_1.quit()
            
    def start(self): # start
        global plot_name
        global path
        global noise_bounds
        global blackbox_decode
        
        # get path
        path = self.lineEdit.text()
        self.textBrowser.append('Blackbox Data: %r' % path)
        
        # get plot_name
        plot_name = self.lineEdit_2.text()
        if not os.path.isdir(plot_name): # autoname
            plot_name = os.path.join(os.getcwd(), str(time.time()))
        self.textBrowser.append('result path: %r' % plot_name)
        
        # get noise_bounds
        if noise_bounds == 'auto': 
            pass
        else:
            gyro = [self.doubleSpinBox_2.value(), self.doubleSpinBox_3.value()]
            Debug = [self.doubleSpinBox_6.value(), self.doubleSpinBox_5.value()]
            D_term = [self.doubleSpinBox_4.value(), self.doubleSpinBox.value()]
            log = [self.doubleSpinBox_7.value(), self.doubleSpinBox_8.value()]
            noise_bounds = [gyro, Debug, D_term, log]
        self.textBrowser.append('noise: %r' % noise_bounds)
        
        # define the blackbox decode path & test if it is exsit
        blackbox_decode = os.path.join(os.getcwd(), 'Blackbox_decode.exe')
        if not os.path.isfile(blackbox_decode):
            self.textBrowser.append('找不到 "Blackbox_decode.exe". 下载链接 ''https://github.com/cleanflight/blackbox-tools/releases.')
        else:
            self.textBrowser.append('Decoding with %r' % blackbox_decode)
        
        #print("文件：", os.path.isfile(path), "存储位：", os.path.isdir(plot_name), "BlackBOX_decode:", os.path.isfile(blackbox_decode))
        if os.path.isfile(path) and os.path.isfile(blackbox_decode):

            if not os.path.isdir(plot_name): # test the plot_name
                os.makedirs(plot_name)
                self.textBrowser.append('因为生成文件的位置无效，已存到' + plot_name)

            try:
                self.thread_1 = Thread_1()
                self.thread_1._signal.connect(self.pushButton_3.setDisabled)
                self.thread_1.start()
                self.thread_1._signal.connect(self.status)
            except Exception as e:
                self.textBrowser.append('错误:' + repr(e))
        elif not os.path.isfile(path):
            self.textBrowser.append('请填入要分析的数据！！！')
        else:
            self.textBrowser.append('Error!!!')

qmut_1 = QMutex()
class Thread_1(QThread):
    _signal = pyqtSignal(bool)
    def __init__(self):
        super().__init__()

    def run(self):
        self._signal.emit(True)
        qmut_1.lock()
        analyzer.BB_log(path, plot_name, blackbox_decode, noise_bounds)
        qmut_1.unlock()
        self._signal.emit(False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())