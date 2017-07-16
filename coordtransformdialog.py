"""
/***************************************************************************
 CoordtransformDialog
                                 A QGIS plugin
 transform input coordinate to whatever new refrence system using EPSG number
                             -------------------
        begin                : 2012-03-03
        copyright            : (C) 2012 by Giuseppe De Marco
        email                : info@pienocampo.it
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

from PyQt4 import QtCore, QtGui
from ui_coordtransform import Ui_Coordtransform
# create the dialog for zoom to point
class CoordtransformDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_Coordtransform()
        self.ui.setupUi(self)
