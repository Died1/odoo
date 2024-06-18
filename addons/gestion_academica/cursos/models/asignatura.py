from odoo import fields, models

class Asignatura(models.Model):
    _name = 'academica.asignatura'
    _description = 'Asignatura'
    
    paralelo_id = fields.Many2one('academica.paralelo', string='Paralelo', required=True)
    materia_id = fields.Many2one('academica.materia', string='Materia', required=True)
    descripcion_materia = fields.Char(related='materia_id.descripcion', string='Descripción de la Materia', store=True, readonly=True)
    teacher_id = fields.Many2one('hr.employee', string='Profesor', domain="[('teacher', '=', True)]")
    asistencia_ids = fields.One2many('academica.asistencia', 'asignatura_id', string='Asistencias')
    actividad_ids = fields.One2many('academica.actividad', 'asignatura_id', string='Actividades')
    # Método para cambiar la visualización de materia_id en las relaciones
    horario_ids = fields.One2many('academica.horario', 'asignatura_id', string='Horario')