from odoo import fields, models

class Paralelo(models.Model):
    _name = 'academica.paralelo'
    _description = 'Paralelo'
    
    cod = fields.Char(string='Código', required=True)
    descripcion = fields.Char(string='Descripción', required=True)
    aula = fields.Char(string='Aula', required=True)
    cupo = fields.Integer(string='Cupo', required=True)
    
    curso_id = fields.Many2one('academica.curso', string='Curso', required=True)
    curso_descripcion = fields.Char(related='curso_id.descripcion', string='Descripción del Curso', store=True, readonly=True)
                
    asignatura_ids = fields.One2many('academica.asignatura', 'paralelo_id', string='Asignaturas')

    #Método para cambiar la visualización de curso_id en las relaciones
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.descripcion} - {record.curso_id.descripcion}"  # Muestra la descripción del paralelo y del curso
            result.append((record.id, name))
        return result