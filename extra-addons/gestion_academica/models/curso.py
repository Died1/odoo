from odoo import fields, models

class Curso(models.Model):
    _name = 'academica.curso'
    _description = 'Curso'
    
    cod = fields.Char(string='Código', required=True)
    descripcion = fields.Char(string='Descripción', required=True)
    
    paralelo_ids = fields.One2many('academica.paralelo', 'curso_id', string='Paralelos')

    materia_ids = fields.Many2many('academica.materia', string='Materias')