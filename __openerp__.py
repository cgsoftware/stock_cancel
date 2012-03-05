# -*- encoding: utf-8 -*-
##############################################################################
#
#    Personalizzazione realizzata da Andrea Cometa
#    Compatible with OpenERP release 6.0.0
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##############################################################################
{
	'name': 'Stock Cancel',
	'version': '1.0',
	'category': 'Stock',
	'description': """Questo modulo consente di reimpostare uno stock.picking allo stato di assigned
This module allows you to revert the stock.picking state to assigned
""",
	'author': 'Andrea Cometa',
	'website': 'http://www.andreacometa.it',
	'depends': ['stock'],
	'update_xml': [
		'stock_view.xml',
		],
	'installable': True,
	'active': False,
}

