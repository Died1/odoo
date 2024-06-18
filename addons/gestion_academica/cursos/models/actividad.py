from odoo import models, fields

class Actividad(models.Model):
    _name = 'academica.actividad'
    _description = 'Actividad'

    nombre = fields.Char(string='Nombre', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    asignatura_id = fields.Many2one('academica.asignatura', string='Asignatura', required=True)
    detalle_ids = fields.One2many('academica.detalle.actividad', 'actividad_id', string='Detalle de Actividad')