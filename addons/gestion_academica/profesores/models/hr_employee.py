from odoo import fields, models


class HrEmployee(models.Model):
    """Model used to create the records of teacher."""
    _inherit = 'hr.employee'

    teacher = fields.Boolean(string='Is Teacher', help='Used to mark the '
                                                       'employee as a teacher.')
    
