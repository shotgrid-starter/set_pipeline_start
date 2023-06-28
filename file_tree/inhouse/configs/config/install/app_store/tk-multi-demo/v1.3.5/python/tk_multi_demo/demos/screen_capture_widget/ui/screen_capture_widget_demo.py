# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_capture_widget_demo.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_ScreenCaptureWidgetDemoUI(object):
    def setupUi(self, ScreenCaptureWidgetDemoUI):
        ScreenCaptureWidgetDemoUI.setObjectName("ScreenCaptureWidgetDemoUI")
        ScreenCaptureWidgetDemoUI.resize(608, 306)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScreenCaptureWidgetDemoUI.sizePolicy().hasHeightForWidth())
        ScreenCaptureWidgetDemoUI.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(ScreenCaptureWidgetDemoUI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_layout = QtGui.QFormLayout()
        self.top_layout.setSpacing(8)
        self.top_layout.setObjectName("top_layout")
        self.get_desktop_pixmap_btn = QtGui.QPushButton(ScreenCaptureWidgetDemoUI)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.get_desktop_pixmap_btn.setFont(font)
        self.get_desktop_pixmap_btn.setObjectName("get_desktop_pixmap_btn")
        self.top_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.get_desktop_pixmap_btn)
        self.get_desktop_pixmap_desc_layout = QtGui.QVBoxLayout()
        self.get_desktop_pixmap_desc_layout.setObjectName("get_desktop_pixmap_desc_layout")
        self.get_desktop_pixmap_desc = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.get_desktop_pixmap_desc.setWordWrap(False)
        self.get_desktop_pixmap_desc.setObjectName("get_desktop_pixmap_desc")
        self.get_desktop_pixmap_desc_layout.addWidget(self.get_desktop_pixmap_desc)
        self.get_desktop_pixmap_rect_layout = QtGui.QHBoxLayout()
        self.get_desktop_pixmap_rect_layout.setObjectName("get_desktop_pixmap_rect_layout")
        self.left_lbl = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.left_lbl.setObjectName("left_lbl")
        self.get_desktop_pixmap_rect_layout.addWidget(self.left_lbl)
        self.left_spin = QtGui.QSpinBox(ScreenCaptureWidgetDemoUI)
        self.left_spin.setMaximum(2048)
        self.left_spin.setObjectName("left_spin")
        self.get_desktop_pixmap_rect_layout.addWidget(self.left_spin)
        self.right_lbl = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.right_lbl.setObjectName("right_lbl")
        self.get_desktop_pixmap_rect_layout.addWidget(self.right_lbl)
        self.right_spin = QtGui.QSpinBox(ScreenCaptureWidgetDemoUI)
        self.right_spin.setMaximum(2048)
        self.right_spin.setProperty("value", 350)
        self.right_spin.setObjectName("right_spin")
        self.get_desktop_pixmap_rect_layout.addWidget(self.right_spin)
        self.top_lbl = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.top_lbl.setObjectName("top_lbl")
        self.get_desktop_pixmap_rect_layout.addWidget(self.top_lbl)
        self.top_spin = QtGui.QSpinBox(ScreenCaptureWidgetDemoUI)
        self.top_spin.setMaximum(2048)
        self.top_spin.setObjectName("top_spin")
        self.get_desktop_pixmap_rect_layout.addWidget(self.top_spin)
        self.bottom_lbl = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.bottom_lbl.setObjectName("bottom_lbl")
        self.get_desktop_pixmap_rect_layout.addWidget(self.bottom_lbl)
        self.bottom_spin = QtGui.QSpinBox(ScreenCaptureWidgetDemoUI)
        self.bottom_spin.setMaximum(2048)
        self.bottom_spin.setProperty("value", 350)
        self.bottom_spin.setObjectName("bottom_spin")
        self.get_desktop_pixmap_rect_layout.addWidget(self.bottom_spin)
        self.get_desktop_pixmap_rect_layout.setStretch(1, 1)
        self.get_desktop_pixmap_rect_layout.setStretch(3, 1)
        self.get_desktop_pixmap_rect_layout.setStretch(5, 1)
        self.get_desktop_pixmap_rect_layout.setStretch(7, 1)
        self.get_desktop_pixmap_desc_layout.addLayout(self.get_desktop_pixmap_rect_layout)
        self.get_desktop_pixmap_desc_layout.setStretch(0, 1)
        self.top_layout.setLayout(0, QtGui.QFormLayout.FieldRole, self.get_desktop_pixmap_desc_layout)
        self.screen_capture_btn = QtGui.QPushButton(ScreenCaptureWidgetDemoUI)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.screen_capture_btn.setFont(font)
        self.screen_capture_btn.setObjectName("screen_capture_btn")
        self.top_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.screen_capture_btn)
        self.screen_capture_desc = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.screen_capture_desc.setObjectName("screen_capture_desc")
        self.top_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.screen_capture_desc)
        self.screen_capture_file_btn = QtGui.QPushButton(ScreenCaptureWidgetDemoUI)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.screen_capture_file_btn.setFont(font)
        self.screen_capture_file_btn.setObjectName("screen_capture_file_btn")
        self.top_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.screen_capture_file_btn)
        self.screen_capture_file_lbl = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.screen_capture_file_lbl.setObjectName("screen_capture_file_lbl")
        self.top_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.screen_capture_file_lbl)
        self.verticalLayout.addLayout(self.top_layout)
        self.output_layout = QtGui.QHBoxLayout()
        self.output_layout.setObjectName("output_layout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.output_layout.addItem(spacerItem)
        self.output_file = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        font = QtGui.QFont()
        font.setItalic(True)
        self.output_file.setFont(font)
        self.output_file.setStyleSheet("QLabel {\n"
"    color: #888888;\n"
"}")
        self.output_file.setText("")
        self.output_file.setAlignment(QtCore.Qt.AlignCenter)
        self.output_file.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.output_file.setObjectName("output_file")
        self.output_layout.addWidget(self.output_file)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.output_layout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.output_layout)
        self.results_layout = QtGui.QHBoxLayout()
        self.results_layout.setObjectName("results_layout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.results_layout.addItem(spacerItem2)
        self.results_pixmap = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_pixmap.sizePolicy().hasHeightForWidth())
        self.results_pixmap.setSizePolicy(sizePolicy)
        self.results_pixmap.setMinimumSize(QtCore.QSize(192, 108))
        self.results_pixmap.setStyleSheet("QLabel {\n"
"    background-color: #000000;\n"
"    border: 1px solid #000000;\n"
"}")
        self.results_pixmap.setFrameShape(QtGui.QFrame.NoFrame)
        self.results_pixmap.setText("")
        self.results_pixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.results_pixmap.setObjectName("results_pixmap")
        self.results_layout.addWidget(self.results_pixmap)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.results_layout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.results_layout)
        self.dummy_label = QtGui.QLabel(ScreenCaptureWidgetDemoUI)
        self.dummy_label.setText("")
        self.dummy_label.setObjectName("dummy_label")
        self.verticalLayout.addWidget(self.dummy_label)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(ScreenCaptureWidgetDemoUI)
        QtCore.QMetaObject.connectSlotsByName(ScreenCaptureWidgetDemoUI)

    def retranslateUi(self, ScreenCaptureWidgetDemoUI):
        ScreenCaptureWidgetDemoUI.setWindowTitle(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.get_desktop_pixmap_btn.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "get_desktop_pixmap(rect)", None, QtGui.QApplication.UnicodeUTF8))
        self.get_desktop_pixmap_desc.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "Performs a screen capture on the specified rectangle:", None, QtGui.QApplication.UnicodeUTF8))
        self.left_lbl.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "L:", None, QtGui.QApplication.UnicodeUTF8))
        self.right_lbl.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "R:", None, QtGui.QApplication.UnicodeUTF8))
        self.top_lbl.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "T:", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_lbl.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "B:", None, QtGui.QApplication.UnicodeUTF8))
        self.screen_capture_btn.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "screen_capture()", None, QtGui.QApplication.UnicodeUTF8))
        self.screen_capture_desc.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "Modally displays the screen capture tool", None, QtGui.QApplication.UnicodeUTF8))
        self.screen_capture_file_btn.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "screen_capture_file()", None, QtGui.QApplication.UnicodeUTF8))
        self.screen_capture_file_lbl.setText(QtGui.QApplication.translate("ScreenCaptureWidgetDemoUI", "Modally display the screen capture tool, saving to a file", None, QtGui.QApplication.UnicodeUTF8))

