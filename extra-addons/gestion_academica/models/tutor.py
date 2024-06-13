from odoo import models, fields

class Tutor(models.Model):
    _inherit = 'res.partner'

    # Campos específicos para los tutores
    es_tutor = fields.Boolean(string='Es tutor(padre de familia)', default=False)
    
    estudiantes_ids = fields.One2many('academica.estudiante', 'tutor_id', string='Estudiantes')
   
