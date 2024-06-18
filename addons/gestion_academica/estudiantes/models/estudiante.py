from odoo import fields, models

class Estudiante(models.Model):
    _name = 'academica.estudiante'
    _description = 'Estudiante'
    
    ci_estudiante = fields.Integer(string='CI Estudiante', required=True)
    rude = fields.Integer(string='RUDE', required=True)
    ap_paterno = fields.Char(string='Apellido Paterno', required=True)
    ap_materno = fields.Char(string='Apellido Materno', required=True)
    nombres = fields.Char(string='Nombres', required=True)
    sexo = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ], string='Sexo', required=True)
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], string='Estado', required=True)
    
    tutor_id = fields.Many2one('res.partner', string='Tutor', domain="[('es_tutor', '=', True)]")    
