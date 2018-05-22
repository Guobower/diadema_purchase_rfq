# -*- coding: utf-8 -*-
{
    "name": "Requision de Materiales",
    "version": "1",
    "category": "Inventario",
    "description": """
	  Caracteristicas:
    - Empleados
    - Productos
    - Inventario
    - Compras
   
""",
    "author": "Marlon J Zelaya",
    "depends": [
        "product",
        "purchase",
        "stock",
        "hr"
        ],
    "data": [
    "views/doff_stock_requisition_view.xml", 
    "views/doff_sequence_view.xml", 
    "views/doff_users_responsible.xml",
    "views/doff_users_ticket.xml"        
    ],
   
   "installable": True,
}
