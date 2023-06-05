# import sys
# sys.path.append("/TD/dongjin/projects/configs/install/core/python")
#
# import sgtk
# sgtk
#
#
# # # Get the engine instance that is currently running.
# # current_engine = sgtk.platform.current_engine()
# #
# # # Grab the pre-created Sgtk instance from the current engine.
# # tk = current_engine.sgtk
# #
# # # Get a context object from a Task. This Task must belong to a Shot for the future steps to work.
# # context = tk.context_from_entity("Task", 13155)


import os
import logging

import shotgun_api3


url = "https://rndtest.shotgrid.autodesk.com/"
script_name = "dongjin"
api_key = "n2khFoc&jybfpufdwabdzgxyr"
sg = shotgun_api3.Shotgun(url, script_name, api_key)


def registerCallbacks(reg):
    eventFilter = {'Shotgun_Project_New': ['*']}
    reg.registerCallback('My script Name', 'My script key', CreateFolders, eventFilter, None)


def CreateFolders(sg, logger, event, args):
    project = event.get('project')
    path = 'My local storage'
    os.chdir(path)
    os.mkdir(project)
    os.chdir(path)
    os.mkdir(project)
    os.chdir(path + '/' + project)
    os.mkdir('For_CGI')
    os.mkdir('production_info')
    os.mkdir('work')


    registerCallbacks()
    CreateFolders()