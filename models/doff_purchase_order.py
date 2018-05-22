# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    rfq_id = fields.Many2one("doff.purchase.requisition", "# Requisición")
    
    
    @api.onchange('rfq_id')
    def onchange_requisition_id(self):
    	#print "AQUI" * 200
    	for purchase in self:
	        if self.rfq_id:
	        	lineas = []
	        	obj_linea_compras = self.env["purchase.order.line"]
	        	for linea_requisition in self.rfq_id.productos_detalle_linea:
	        		lineas.append ((0, 0, {
	        		'name': linea_requisition.productos_id.name,
	        		'price_unit': linea_requisition.productos_id.standard_price,
	        		'product_id': linea_requisition.productos_id.id,
	        		'product_qty': linea_requisition.producto_cantidad,
	        		'product_uom': linea_requisition.productos_id.uom_po_id.id,
	        		'date_planned': linea_requisition.doff_objparent.fecha_requisicion,
	        		}))
	        		#id_purchase_line = obj_linea_compras.create(campos_compras)
	        	self.order_line = lineas
	
	
	#@api.onchange('partner_id')
	#def  onchange(self):
	#	if self.partner_id:
	#		print self.partner_id
	#		print "VENDOR" * 200	


  
    	

	 	


 



