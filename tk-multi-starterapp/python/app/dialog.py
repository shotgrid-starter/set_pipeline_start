# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.


import sgtk
import os
import sys
import threading
import subprocess

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.

from sgtk.platform.qt import QtCore, QtGui

from .api import ExcelCreate
# from .api import LoadConvertModel
from .ui.dialog import Ui_Dialog

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("IO Manager", app_instance, AppDialog)


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.main_stack.setCurrentIndex(0)

        self.api_1 = ExcelCreate()
        # self.api_2 = LoadConvertModel()

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()

        # logging happens via a standard toolkit logger
        logger.info("Launching Starter Application...")

        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An Sgtk API instance, via self._app.sgtk

        # excel_create
        self.ui.ui1_button_2.clicked.connect(self.create_excel)
        self.ui.btn_clear.clicked.connect(self.btn_clear_clicked)
        # self.ui.btn_create.clicked.connect(self.btn_create_clicked)
        # self.ui.btn_create.clicked.connect(self.save_folder_open)
        self.ui.btn_cancel.clicked.connect(self.btn_cancel_clicked)

        #test
        self.ui.btn_create.clicked.connect(self.btn_test)

        # convert
        self.ui.ui2_button_2.clicked.connect(self.convert)

        #
        # self.ui.combo_box.currentIndexChanged.connect(self.combo_box_changed)
        # self.ui.browse_button.clicked.connect(self.browse_clicked)
        # self.ui.ok_button.clicked.connect(self.ok_clicked)
        self.ui.cancel_button.clicked.connect(self.btn_cancel_clicked)


        # browse file action
        self._browse_file_action = QtGui.QAction(self)
        self._browse_file_action.setText("Select Excel File")
        self._browse_file_action.triggered.connect(
            lambda: self._on_browse(folders=False)
        )

        # browse folder action
        self._browse_folder_action = QtGui.QAction(self)
        self._browse_folder_action.setText("Select Directory")
        self._browse_folder_action.triggered.connect(
            lambda: self._on_browse(folders=True)
        )

        # drop area browse button. Note, not using the actions created above
        # because making the buttons look right when they're using he action's
        # text/icon proved difficult. Instead, the button text/icon are defined
        # in the designer file. So as a note, if you want to change the text or
        # icon, you'll need to do it above and in designer.

        self.ui.toolButton.clicked.connect(
            lambda: self._on_browse(folders=False)
        )
        self.ui.btn_browse.clicked.connect(
            lambda: self._on_browse(folders=True)
        )

    def _on_browse(self, folders=False):

        # options for either browse type
        options = [
            QtGui.QFileDialog.DontResolveSymlinks,
            QtGui.QFileDialog.DontUseNativeDialog,
        ]

        if folders:
            # browse folders specifics
            caption = "Select Directory"
            file_mode = QtGui.QFileDialog.Directory
            options.append(QtGui.QFileDialog.ShowDirsOnly)
        else:
            # browse files specifics
            caption = "Select Excel File"
            file_mode = QtGui.QFileDialog.ExistingFiles

        # create the dialog
        file_dialog = QtGui.QFileDialog(parent=self, caption=caption)
        file_dialog.setFileMode(file_mode)
        file_dialog.setDirectory('/TD/show')

        self.ui.line_dir_path.setText(file_dialog.getExistingDirectory())

        # set the appropriate options
        for option in options:
            file_dialog.setOption(option)

        # browse!
        if not file_dialog.exec_():
            return

    def create_excel(self):
        self.ui.main_stack.setCurrentIndex(2)

    def convert(self):
        self.ui.main_stack.setCurrentIndex(1)

    def btn_clear_clicked(self):
        self.ui.line_dir_path.clear()

    # def btn_create_clicked(self):
    #     self.api_1.excel_create()
    #     self.label_save_path.setText(self.api_1.excel_path)
    #     self.message_box()

    # def save_folder_open(self):
    #     if self.retval == QMessageBox.Open:
    #         subprocess.Popen(['gio', 'open', self.model.excel_path])

    def btn_cancel_clicked(self):
        self.ui.main_stack.setCurrentIndex(0)

    def btn_test(self):
        self.api_1.test()

    ## convert ##
    # def combo_box_changed(self):
    #     self.selected_project = self.view.combo_box.currentText()
    #     self.view.label.setText(f'Converting Project: {self.selected_project}')
    #     print(f'selected project: {self.selected_project}')
    #
    # def browse_clicked(self):
    #     dialog = BrowseDialog()
    #     self.selected_xlsx = dialog.file_name
    #     self.view.line_edit.setText(self.selected_xlsx)
    #     self.model.set_file_path(self.selected_xlsx)
    #     print(f'selected xlsx file: {self.selected_xlsx}')
    #
    # def ok_clicked(self):
    #     if not self.model.file_path:
    #         self.view.message_box('Choose the xlsx file')
    #         self.clean_up()
    #         return
    #     if not self.selected_project:
    #         self.view.message_box('Choose the project')
    #         self.clean_up()
    #         return
    #     if not self.model.file_path and self.selected_project:
    #         self.view.message_box('Choose the xlsx file and project')
    #         self.clean_up()
    #     else:
    #         self.model.set_file_path(self.model.file_path)
    #         self.model.data_info()
    #         self.model.get_project(self.selected_project)
    #         self.model.get_sequence_and_upload()
    #         self.model.get_shot_and_upload()
    #         self.model.video_uploader()
    #         self.view.message_box('Work is Done')
    #
    # def clean_up(self):
    #     self.view.line_edit.setText('')
    #     self.selected_xlsx = ''
    #     self.model.file_path = ''
    #
    # def cancel_clicked(self):
    #     self.view.close()

