from odoo import models, fields

class Inscripcion(models.Model):
    _name = 'academica.inscripcion'
    _description = 'Inscripción de Estudiantes'

    fecha_inscripcion = fields.Date(string='Fecha de Inscripción', default=fields.Date.today)
    gestion_id = fields.Many2one('academica.gestion', string='Año Académico', required=True)
    paralelo_id = fields.Many2one('academica.paralelo', string='Paralelo', required=True)
    estudiante_id = fields.Many2one('academica.estudiante', string='Estudiante', required=True)
