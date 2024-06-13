from odoo import fields, models

class Paralelo(models.Model):
    _name = 'academica.paralelo'
    _description = 'Paralelo'
    
    cod = fields.Char(string='Código', required=True)
    descripcion = fields.Char(string='Descripción', required=True)
    aula = fields.Char(string='Aula', required=True)
    cupo = fields.Integer(string='Cupo', required=True)
    
    curso_id = fields.Many2one('academica.curso', string='Curso', required=True)
    
    estudiante_ids = fields.One2many('academica.estudiante', 'paralelo_id', string='Estudiantes')

