# -*- encoding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import Warning

class DoffPurchaseRequisition(models.Model):
	_name = "doff.purchase.requisition"
	_inherit = ['mail.thread']#historial de la bitacora que hace el usuario

	name = fields.Char("Numero de requisicion", required=True, default=lambda self: self.env['ir.sequence'].get('requisiciones'))
	description = fields.Text("Descripcion")

	fecha_requisicion = fields.Date("Fecha de Requisicion", required=True)
	fecha_aprobacion = fields.Date("Fecha de Aprobacion", readonly=True)
	fch_aprobacion_compra = fields.Date("Fecha Aprobacion de Compra", readonly=True)

	#tomar el empleado ya almacenado
	solicitud_empleado = fields.Many2one("hr.employee","Solicitante", required=True)

	#departamento
	departamento_id = fields.Many2one("hr.department","Departamento")

	#Tipo de procesos que se daran en las requission de materiales
	state = fields.Selection([('draft','Borrador'),('inprocess','En Proceso'),('qquotation','RFQ'),('approved','Aprobado'),('waitproduct','Esperando Productos'),
	('completed','Finalizado'),('noapproved','No Aprobada')], "Estado", default='draft')

	responsable_compra = fields.Many2one("res.users","Responsable de compras")
	responsable_compra_aprobacion = fields.Many2one("res.users","Responsable de aprobacion")

	productos_detalle_linea = fields.One2many("doff.product.line", "doff_objparent", "Requisiones Detalladas")

	compras_ids = fields.One2many("purchase.order", "rfq_id", "Cotizaciones")
	
	@api.onchange("solicitud_empleado")
	def onchage(self):
		if self.solicitud_empleado:
			self.departamento_id = self.solicitud_empleado.department_id

	@api.multi
	def inprocess_requisition(self):
		self.fecha_aprobacion =  datetime.now()
		self.write({'state' : 'inprocess'})

	@api.multi
	def quotation_requisition(self):
		self.write({'state' : 'qquotation'})

	@api.multi
	def noapproved_requisition(self):
		self.write({'state':'noapproved'})

	@api.multi
	def approved_requisition(self):
		self.write({'state':'waitproduct'})

	@api.multi
	def waitproduct_requisition(self):
		self.fch_aprobacion_compra =  datetime.now()
		self.write({'state' : 'approved'})	

	@api.multi
	def completed_requisition(self):
		self.write({'state' :'completed'})

#Agregar Productos
class doff_product_line(models.Model):
	_name = "doff.product.line"

	productos_id = fields.Many2one("product.product","Producto", required=True)
	doff_objparent = fields.Many2one("doff.purchase.requisition","Requisicion")
	producto_cantidad = fields.Float("Cantidad", required=True)
	#product_uom_id = fields.Many2one('product.uom', string='Product Unit of Measure')










	
