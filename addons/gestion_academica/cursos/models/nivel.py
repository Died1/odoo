from odoo import models, fields

class Nivel(models.Model):
    _name = 'academica.nivel'
    _description = 'Nivel Holistico'

    nombre = fields.Char(string='Nombre', required=True)
    
    descripcion = fields.Text(string='Descripción')
    
    materia_ids = fields.Many2many('academica.materia', string='Materias')
    