from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QCoreApplication
import sys

import extractor

class start(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FIXTRACTOR')
        self._height = 500
        self._width = 400
        self.resize(self._height, self._width)
        self.mainLayout = QVBoxLayout()
        self.secondaryLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.secondaryLayout)
        #self.label = QLabel('Please login to continue')
        # self.source = QFileDialog()
        # self.sourceLayout = QHBoxLayout()
        # self.destinationLayout = QHBoxLayout()
        # self.mainLayout.addLayout(self.sourceLayout)
        # self.mainLayout.addLayout(self.destinationLayout)
        self.source_text = QLineEdit()
        self.source_text.setReadOnly(True)
        self.source_text.setFixedHeight(50)
        self.source = QPushButton("Choose source path")
        self.source.setFixedHeight(50)
        
        self.destination_text = QLineEdit()
        self.destination_text.setReadOnly(True)
        self.destination_text.setFixedHeight(50)
        self.destination = QPushButton("Choose destination path")
        self.destination.setFixedHeight(50)
        # self.source.setFixedHeight(50)
        # self.source.setPlaceholderText('Enter username')
        # self.destination = QFileDialog()
        # self.password.setFixedHeight(50)
        # self.password.setPlaceholderText('Enter password')
        self.button = QPushButton('Extract')
        self.button.setFixedHeight(50)
        #self.secondaryLayout.addWidget(self.label)
        self.secondaryLayout.addWidget(self.source_text)
        self.secondaryLayout.addWidget(self.source)
        
        self.secondaryLayout.addWidget(self.destination_text)
        self.secondaryLayout.addWidget(self.destination)
        # self.secondaryLayout.addWidget(self.destination)
        self.secondaryLayout.addWidget(self.button)
        self.button.clicked.connect(self.start_extraction)
        self.destination.clicked.connect(self.set_destination)
        self.source.clicked.connect(self.set_source)

    # def moveThis(self):
    #     self._width += 100
    #     self._height += 100
    #     self.resize(self._height, self._width)

    def set_destination(self):
      path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
      self.destination_text.setText(path)
      extractor.restore_folder = path
    
    def set_source(self):
      path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
      self.source_text.setText(path)
      extractor.args.extract = path

    def start_extraction(self):
        if self.destination_text.text() and self.source_text.text():
            self.button.setText("Extraction started")
            self.button.setEnabled(False)
            result = extractor.extract()
            message = f"{result.get('success')} files where successfully extracted {result.get('error')} failed! Want to run another?"
            alert = QMessageBox.question(self,'', message, QMessageBox.Yes | QMessageBox.No)
            if alert == QMessageBox.No:
                QCoreApplication.instance().quit()
            self.button.setText("Extract")
            self.destination_text.setText("")
            self.source_text.setText("")
            self.button.setEnabled(True)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Missing directories")
            msg.setInformativeText("Both source and destination directories are required!")
            msg.setWindowTitle("Error!")
            msg.setDetailedText("Please choose a source directory and a destination directory.")
            msg.exec_()
    
    # def shuffle_color(self):
    #     global EXTRACTION:
    #     while type(EXTRACTION) != dict:
    #         colors = ['red', 'green', 'blue', 'black', 'white']
    #         color = random.choice(colors)
    #         self.button.setStyleSheet(f"background-color:{color};")
    #     color = ""
    #     self.button.setStyleSheet(f"background-color:{color};")

# class worker(QWidget):
#     def __init__(self):
#         super().__init__()

#         # self.setWindowTitle('FIXTRACTOR')
#         self._height = 500
#         self._width = 400
#         self.resize(self._height, self._width)
#         self.mainLayout = QVBoxLayout()
#         # self.secondaryLayout = QVBoxLayout()
#         self.setLayout(self.mainLayout)
#         # self.mainLayout.addLayout(self.secondaryLayout)

#         self.setWindowTitle('extraction in progress')
#         # self.resize(400, 500)
#         # self.mainLayout = QVBoxLayout()
#         # self.mainWidget = QWidget()
#         # self.setCentralWidget(self.mainWidget)
#         # self.mainWidget.setLayout(self.mainLayout)
#         self.label = QLabel(self)
#         # self.label.width(300)
#         # self.label.height(300)
#         spinner = QMovie('./asset/loader.gif')
#         self.label.setMovie(spinner)
#         # self.setGeometry(50,50,100,100)
#         # self.setMaximumSize(300)
#         spinner.start()
#         # self.resize(400, 500)
#         # self.button = QPushButton('Hello World')
#         self.mainLayout.addWidget(self.label)
#         self.await_extraction()
    
#     def await_extraction(self):
#         global EXTRACTION
#         while type(EXTRACTION) != dict:
#             # print('waiting for extraction to finish')
#             # print(type(EXTRACTION))
#             pass
#         self.end_extraction()

#     def end_extraction(self):
#         global EXTRACTION
#         result = EXTRACTION
#         message = f"{result.get('success')} files where successfully extracted {result.get('error')} failed! Want to run another?"
#         alert = QMessageBox.question(self,'', message, QMessageBox.Yes | QMessageBox.No)
#         if alert == QMessageBox.Yes:
#             self.hide()
#             start().show()
#             # self.view.show()
#         else:
#             QCoreApplication.instance().quit()

def main():
    app = QApplication(sys.argv)
    view = start()
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()