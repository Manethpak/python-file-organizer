from PyQt5.QtWidgets import *

from organizer import organize

class MainWindow(QMainWindow):
    """Main GUI window"""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("File Sorter")
        self.setFixedSize(400, 100)
        
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._form()
        self._buttons()
    
    def _buttons(self):
        self.btn_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Organize", self)
        self.start_btn.clicked.connect(self._start_app)
        
        self.browse_btn = QPushButton("Browse Folder", self)
        self.browse_btn.clicked.connect(self._file_dialog)

        self.btn_layout.addWidget(self.browse_btn)
        self.btn_layout.addWidget(self.start_btn)
        
        self.generalLayout.addLayout(self.btn_layout)
        
    def _form(self):
        self.form_layout = QFormLayout()
        self.path = QLineEdit()
        self.form_layout.addRow("Path:", self.path)

        self.generalLayout.addLayout(self.form_layout)
        
    def _file_dialog(self):
        self.dialog = QFileDialog()
        self.dir = self.dialog.getExistingDirectory(self, 'Select a folder to be organized')
        self.path.setText(self.dir)
        
    def _get_path(self):
        return self.path.text()

    def _start_app(self):
        full_path = self._get_path()
        
        if full_path:
            try:
                organize(full_path)
                self._alert("Folder has been organized!")
            except:
                self._alert("Error occured!")
        else:
            self._alert("Enter a folder path or browse.") 
        
    def _alert(self, message):
        self.alert = QDialog(self)
        self.alert.setWindowTitle("Alert!")
        self.alert.setFixedSize(300, 50)
        
        self.alert_layout = QVBoxLayout()
        
        self.alert_label = QLabel(message)
        self.alert_layout.addWidget(self.alert_label)
        self.alert.setLayout(self.alert_layout)
        self.alert.exec()
