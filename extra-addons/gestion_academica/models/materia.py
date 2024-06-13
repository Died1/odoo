from odoo import fields, models

class Materia(models.Model):
    _name = 'academica.materia'
    _description = 'Materia'
    
    cod = fields.Char(string='Código', required=True)
    
    descripcion = fields.Char(string='Descripción', required=True)
    
