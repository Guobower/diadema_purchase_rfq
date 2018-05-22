# -*- coding: utf-8 -*-
# Copyright 2016 Business Analytics Consulting Group S.A. de C.V.
from odoo import models, fields, api

class DoffAccessUsers(models.Model):
    _inherit = "res.users"
    
    responsable_requisicion = fields.Boolean("Responsable de Requisicion")
    reponsable_aprobacion = fields.Boolean("Responsable de Aprobacion")