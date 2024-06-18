from odoo import models, fields

class DetalleActividad(models.Model):
    _name = 'academica.detalle.actividad'
    _description = 'Detalle Actividad'

    actividad_id = fields.Many2one('academica.actividad', string='Actividad', required=True)
    estudiante_id = fields.Many2one('academica.estudiante', string='Estudiante', required=True)
    calificacion = fields.Float(string='Calificación', required=True)
    

