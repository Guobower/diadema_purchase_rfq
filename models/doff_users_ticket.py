# -*- coding: utf-8 -*-
# Copyright 2016 Business Analytics Consulting Group S.A. de C.V.
from odoo import models, fields, api

class UsersTickets(models.Model):
	_inherit = "res.users"

	responsable_ticketict = fields.Boolean("Soporte ICT")
	reponsable_ticketmant = fields.Boolean("Soporte Mantenimiento")
	
    