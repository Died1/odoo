from odoo import models, fields

class DetalleAsistencia(models.Model):
    _name = 'academica.detalle.asistencia'
    _description = 'Detalle de Asistencia'
    
    asistencia_id = fields.Many2one('academica.asistencia', string='Asistencia', required=True)
    estudiante_id = fields.Many2one('academica.estudiante', string='Estudiante', required=True)
    estado = fields.Selection([
        ('presente', 'Presente'),
        ('ausente', 'Ausente'),
        ('licencia', 'Licencia'),
        ('tarde', 'Tarde')
    ], string='Estado', required=True, default='presente')
    
    
    