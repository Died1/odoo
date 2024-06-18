from odoo import fields, models

class Asistencia(models.Model):
    _name = 'academica.asistencia'
    _description = 'Asistencia'
    
    asignatura_id = fields.Many2one('academica.asignatura', string='Asignatura')
    fecha = fields.Date(string='Fecha', required=True, default=fields.Date.today)   
    detalle_ids = fields.One2many('academica.detalle.asistencia', 'asistencia_id', string='Detalle de Asistencia')
