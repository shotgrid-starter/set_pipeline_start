from io_manager import ExcelCreate
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton


class IntegrationView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Integration UI')
        self.layout = QHBoxLayout()  # 수평 레이아웃으로 변경
        self.layout.setSpacing(20)  # 버튼 사이 간격 조정

        self.ui1_button = QPushButton('Open Excel File')
        self.ui2_button = QPushButton('Upload to Shotgrid')
        self.ui3_button = QPushButton('Convert to .jpg / .mp4')

        self.layout.addWidget(self.ui1_button)
        self.layout.addWidget(self.ui2_button)
        self.layout.addWidget(self.ui3_button)

        self.setLayout(self.layout)

        # self.ui1_button.clicked.connect(self.open_my_ui)
        self.ui2_button.clicked.connect(self.open_ui2)

    # def open_my_ui(self):


    def open_ui2(self):
        self.controller = CreateExcelController()  # CreateExcelController 인스턴스 생성
        self.controller.show()


def main():
    app = QApplication([])
    integration_view = IntegrationView()
    integration_view.show()
    app.exec_()


if __name__ == '__main__':
    main()
