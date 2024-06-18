from odoo import fields, models

class Curso(models.Model):
    _name = 'academica.curso'
    _description = 'Curso'
    
    cod = fields.Char(string='Código', required=True)
    
    descripcion = fields.Char(string='Descripción', required=True)
    
    nivel_id = fields.Many2one('academica.nivel', string='Nivel')
    
    nivel_nombre = fields.Char(related='nivel_id.nombre', string='Nombre del Nivel', store=True)
    
    paralelo_ids = fields.One2many('academica.paralelo', 'curso_id', string='Paralelos')

    
    