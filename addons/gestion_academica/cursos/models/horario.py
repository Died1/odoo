from odoo import fields, models

class Horario(models.Model):
    _name = 'academica.horario'
    _description = 'Horario'
    
    asignatura_id = fields.Many2one('academica.asignatura', string='Asignatura', required=True)
    
    
    dia_semana = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes')
    ], string='Día de la Semana', required=True)
    hora_inicio = fields.Float(string='Hora de Inicio', required=True)
    hora_fin = fields.Float(string='Hora de Fin', required=True)
