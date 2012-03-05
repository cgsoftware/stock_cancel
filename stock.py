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
# W gli spaghetti code!!!
##############################################################################


from osv import osv, fields
import netsvc
from tools.translate import _

class stock_picking(osv.osv):
	_inherit = 'stock.picking'

		
	def action_revert_done(self, cr, uid, ids, *args):
		if not len(ids):
			return False
		cr.execute('select id from stock_move where picking_id IN %s and state=%s', (tuple(ids), 'done'))
		line_ids = map(lambda x: x[0], cr.fetchall())
		self.write(cr, uid, ids, {'state': 'draft'})
		self.pool.get('stock.move').write(cr, uid, line_ids, { 'state': 'draft'})
		wf_service = netsvc.LocalService("workflow")
		for inv_id in ids:
			# Deleting the existing instance of workflow for SO
			wf_service.trg_delete(uid, 'stock.picking', inv_id, cr)
			wf_service.trg_create(uid, 'stock.picking', inv_id, cr)
		for (id,name) in self.name_get(cr, uid, ids):
			message = _("The stock picking '%s' has been set in draft state.") %(name,)
			self.log(cr, uid, id, message)
		return True

stock_picking()
