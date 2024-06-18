from odoo import models, fields

class Gestion(models.Model):
    _name = 'academica.gestion'
    _description = 'Gestión de Año Académico'

    nombre = fields.Char(string='Nombre', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha de Fin', required=True)