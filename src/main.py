import sys
from PyQt5.QtWidgets import QApplication

from gui import MainWindow

def run_app():
    """Main function."""
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_app()