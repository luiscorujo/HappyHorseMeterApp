from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import model as custom_model
import sys
import time
from PyQt5.QtCore import pyqtSlot, QRunnable, QThreadPool
from PyQt5.QtGui import QMovie


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 655)
        MainWindow.setFixedSize(894, 655)

        self.threadpool = QThreadPool()
        models_worker = Worker(self.start_models, None, None)
        self.threadpool.start(models_worker)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(801, 576))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.uploadImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadImageButton.setGeometry(QtCore.QRect(660, 90, 171, 41))
        self.uploadImageButton.setStyleSheet("border: 2px solid #555;\n"
                                             "border-radius: 20px;\n"
                                             "border-style: outset;\n"
                                             "background-color: rgb(93, 155, 255);\n")
        self.uploadImageButton.setObjectName("uploadImageButton")

        self.uploadImageButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.uploadImageButton2.setGeometry(QtCore.QRect(660, 90, 171, 41))
        self.uploadImageButton2.setStyleSheet("border: 2px solid #555;\n"
                                             "border-radius: 20px;\n"
                                             "border-style: outset;\n"
                                             "background-color: rgb(236, 236, 236);\n")
        self.uploadImageButton2.setObjectName("uploadImageButton2")
        self.uploadImageButton2.setVisible(False)

        self.originalImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.originalImageLabel.setGeometry(QtCore.QRect(160, 190, 131, 21))
        self.originalImageLabel.setStyleSheet("font: 18pt \"Arial\";\n"
                                              "color: rgb(0, 0, 0);\n"
                                              "border-bottom-width: 1px;\n"
                                              "border-bottom-style: solid;\n"
                                              "border-radius: 0px;")
        self.originalImageLabel.setObjectName("originalImageLabel")

        self.predictionLabel = QtWidgets.QLabel(self.centralwidget)
        self.predictionLabel.setGeometry(QtCore.QRect(630, 190, 90, 21))
        self.predictionLabel.setStyleSheet("font: 18pt \"Arial\";\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-bottom-width: 1px;\n"
                                           "border-bottom-style: solid;\n"
                                           "border-radius: 0px;")
        self.predictionLabel.setObjectName("predictionLabel")

        self.originalImage = QtWidgets.QLabel(self.centralwidget)
        self.originalImage.setGeometry(QtCore.QRect(20, 230, 421, 341))
        self.originalImage.setStyleSheet("border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-style: solid;\n"
                                         "border-radius: 0px;")
        self.originalImage.setText("")
        self.originalImage.setScaledContents(True)
        self.originalImage.setObjectName("originalImage")

        self.predictionImage = QtWidgets.QLabel(self.centralwidget)
        self.predictionImage.setGeometry(QtCore.QRect(460, 230, 421, 341))
        self.predictionImage.setStyleSheet("border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-style: solid;\n"
                                           "border-radius: 0px;")
        self.predictionImage.setText("")
        self.predictionImage.setScaledContents(True)
        self.predictionImage.setObjectName("predictionImage")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 20, 551, 131))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap("images/app_logo.png"))
        self.title.setObjectName("title")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.loadingVideo = QtWidgets.QLabel(self.centralwidget)
        self.loadingVideo.setGeometry(QtCore.QRect(460, 230, 421, 341))
        self.loadingVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.movie = QMovie("images/app_loading.gif")

        self.loadingVideo.setMovie(self.movie)
        self.movie.start()
        self.loadingVideo.setVisible(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.uploadImageButton.clicked.connect(self.startBrowseFiles)

        self.model = None
        self.model_ready=False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Horse Happy Meter"))
        self.uploadImageButton.setText(_translate("MainWindow", "Upload Image"))
        self.uploadImageButton2.setText(_translate("MainWindow", "Upload Image"))
        self.originalImageLabel.setText(_translate("MainWindow", "Original Image:"))
        self.predictionLabel.setText(_translate("MainWindow", "Prediction:"))

    def showImage(self, path):
        self.originalImage.setPixmap(QtGui.QPixmap(path))

    def showPrediction(self, path):
        self.predictionImage.setPixmap(QtGui.QPixmap(path))
        self.uploadImageButton2.setVisible(False)
        self.uploadImageButton.setVisible(True)

    def startBrowseFiles(self):
        self.uploadImageButton.setVisible(False)
        self.uploadImageButton2.setVisible(True)
        self.browseFiles()

    def loading(self, a=None):
        if self.loadingVideo.isVisible():
            self.loadingVideo.setVisible(False)
        else:
            self.loadingVideo.setVisible(True)

    def browseFiles(self):
        try:
            file_path = QFileDialog.getOpenFileName()[0]
            if file_path.endswith('jpg') or file_path.endswith('png') or file_path.endswith('jpeg') or file_path.endswith('JPG') or file_path.endswith('PNG') or file_path.endswith('JPEG'):
                self.showImage(file_path)
                loading_worker = Worker(self.loading, None, None)
                self.threadpool.start(loading_worker)
                prediction_worker = Worker(self.predict, file_path, None)
                self.threadpool.start(prediction_worker)
            else:
                raise NameError('Not valid file path')
        except NameError:
            warning = QMessageBox()
            warning.setText("Invalid file type, please try again")
            warning.exec()
            self.predictionImage.setPixmap(QtGui.QPixmap())
            self.uploadImageButton2.setVisible(False)
            self.uploadImageButton.setVisible(True)
            self.predictionLabel.setGeometry(QtCore.QRect(630, 190, 90, 21))
            self.predictionLabel.setText('Prediction:')

    def predict(self, file_path):
        while self.model_ready is False:
            time.sleep(1)
        file = file_path[0]
        roi = self.model.detect_roi(file)
        img = self.model.preprocess_image_for_model(roi)
        img = img.reshape(1, 150, 150, 3)
        prediction = self.model.predict_result(img)
        emotion, prob = self.model.predict_emotion(prediction)
        text = f'Prediction: {emotion}'
        self.loadingVideo.setVisible(False)
        self.predictionLabel.setGeometry(QtCore.QRect(590, 190, 165, 21))
        self.predictionLabel.setStyleSheet("font: 18pt \"Arial\";\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-bottom-width: 1px;\n"
                                           "border-bottom-style: solid;\n"
                                           "border-radius: 0px;")
        self.predictionLabel.setText(text)
        self.showPrediction('result.jpg')

    def start_models(self, a=None):
        self.model = custom_model.Model()
        self.model_ready = True


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(self.args)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('images/app_icon.png', QtCore.QSize(16, 16))
    app.setWindowIcon(app_icon)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Happy Horse Meter")
    MainWindow.show()
    sys.exit(app.exec_())


