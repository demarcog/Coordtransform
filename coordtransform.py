"""
/***************************************************************************
 Coordtransform
                                 A QGIS plugin
 transform input coordinate to whatever new refrence system using EPSG number
                              -------------------
        begin                : 2012-03-03
        latest changes       : 2018-04-17
        copyright            : (C) 2012-2018 by Giuseppe De Marco
        email                : demarco.giuseppe@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import
from builtins import str
from builtins import object
# Import the PyQt and QGIS libraries
from qgis.core import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
# Initialize Qt resources from file resources.py
from . import resources
#import pdb
# Import the code for the dialog
from .coordtransformdialog import CoordtransformDialog

class Coordtransform(object):

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.dlg = CoordtransformDialog()
        x = None
        y = None
        input = None
        output = None
        chkout = 0
        chkin = 0
        
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/coordtransform/icon.png"), \
            "Coordtransform", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&d2gis", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&d2gis",self.action)
        self.iface.removeToolBarIcon(self.action)
        
#custom functions begin------------------------------------------------------------
    def check_x(self):
        x = self.dlg.ui.X.text()
        if  x =='':
            QMessageBox.critical(None,"!","Please provide X value")
            chkx = 0
            return chkx
        else:
            chkx = 1
            return chkx
    
    def check_y(self):
        y = self.dlg.ui.Y.text()
        if  y == '':
            QMessageBox.critical(None,"!","Please provide Y value")
            chky = 0
            return chky
        else:
            chky = 1
            return chky
    
    def check_input(self):
        input = self.dlg.ui.inputcrs.text()
        if  input == '':
            QMessageBox.critical(None,"!","Please provide input epsg code")
            chkin = 0
            return chkin
        else:
            chkin = 1
            return chkin
    
    def check_output(self):
        output = self.dlg.ui.outputcrs.text()
        if  output == '':
            QMessageBox.critical(None,"!","Please provide output epsg code")
            chkout = 0
            return chkout
        else:
            chkout = 1
            return chkout
            
    
    def clear(self):
        self.dlg.ui.results.clear()
        self.dlg.ui.X.clear()
        self.dlg.ui.Y.clear()
        self.dlg.ui.inputcrs.clear()
        self.dlg.ui.outputcrs.clear()
        self.dlg.ui.inputproj4.clear()
        self.dlg.ui.outputproj4.clear()
        self.dlg.ui.trfY.clear()
        self.dlg.ui.trfX.clear()
    
    def transform(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace() 
        #self.dlg.ui.results.setText("Transform pressed\n")
        chkx = 0
        chky = 0
        chkin = 0
        chkout = 0
        chkx = self.check_x()
        chky = self.check_y()
        chkin = self.check_input()
        chkout = self.check_output()
        if (chkin == 1) and (chkout == 1) and (chkx == 1) and (chky == 1):
            x = self.dlg.ui.X.text()
            y = self.dlg.ui.Y.text()
            input = "EPSG:"+ self.dlg.ui.inputcrs.text()
            output = "EPSG:"+self.dlg.ui.outputcrs.text()
            context = QgsProject.instance()
            crsSrc = QgsCoordinateReferenceSystem(input)
            crsDest = QgsCoordinateReferenceSystem(output)
            if crsSrc.authid() == '':
                source_crs = QgsCoordinateReferenceSystem()
                source_crs.createFromId(int(input), QgsCoordinateReferenceSystem.InternalCrsId)
                if source_crs.authid() == '':
                    QMessageBox.critical(None,"!","Please provide a valid input epsg/user code")
                    return
                else:
                    crsSrc=source_crs
            if crsDest.authid() == '':
                dest_crs = QgsCoordinateReferenceSystem()
                dest_crs.createFromId(int(output), QgsCoordinateReferenceSystem.InternalCrsId)
                if dest_crs.authid() == '':
                    QMessageBox.critical(None,"!","Please provide a valid output epsg/user code")
                    return
                else:
                    crsDest=dest_crs
            self.dlg.ui.results.setText("input CRS "+crsSrc.authid()+"\n"+"output CRS "+crsDest.authid())
            self.dlg.ui.inputproj4.setText(str(crsSrc.toProj4()))
            self.dlg.ui.outputproj4.setText(str(crsDest.toProj4()))
            xform = QgsCoordinateTransform(crsSrc, crsDest, context)
            transfpoint=xform.transform(QgsPointXY(float(x),float(y)))
            self.dlg.ui.results.append("New coordinates:")
            self.dlg.ui.results.append(transfpoint.toString())
            self.dlg.ui.trfX.setText(str(transfpoint.x()))
            self.dlg.ui.trfY.setText(str(transfpoint.y()))
        else:
            return

    # run method that performs all the real work
    def run(self):
        #Buttons events
        self.dlg.ui.clear.clicked.connect(self.clear)
        self.dlg.ui.transform.clicked.connect(self.transform)
        
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass
