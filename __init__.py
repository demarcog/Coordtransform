"""
/***************************************************************************
 Coordtransform
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Coordtransform"
def description():
    return "This plugin let the user transform x,y input coordinate to whatever new reference system using EPSG code number and even USER DEFINED crs"
def version():
    return "Version 1.0"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    # load Coordtransform class from file Coordtransform
    from coordtransform import Coordtransform
    return Coordtransform(iface)
