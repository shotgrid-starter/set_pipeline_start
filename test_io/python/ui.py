from excel_create_controller import CreateExcelController
from excel_load_convert_controller import LoadConvertController

from PySide2.QtWidgets import *


class IntegrationView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IO Manager')
        self.layout = QHBoxLayout()  # 수평 레이아웃으로 변경
        self.layout.setSpacing(20)  # 버튼 사이 간격 조정

        self.ui1_button = QPushButton('Create Excel File')
        self.ui2_button = QPushButton('Convert & Upload to Shotgrid')

        self.layout.addWidget(self.ui1_button)
        self.layout.addWidget(self.ui2_button)

        self.setLayout(self.layout)

        self.ui1_button.clicked.connect(self.connect_excel_create)
        self.ui2_button.clicked.connect(self.connect_excel_load_convert)

    def connect_excel_create(self):
        self.ce = CreateExcelController()
        self.ce.show()

    def connect_excel_load_convert(self):
        self.lc = LoadConvertController()  # Converter_controller 인스턴스 생성
        self.lc.view.show()


def main():
    app = QApplication([])
    integration_view = IntegrationView()
    integration_view.show()
    app.exec_()


if __name__ == '__main__':
    main()

