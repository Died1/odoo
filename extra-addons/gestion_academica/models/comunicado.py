from odoo import models, fields, api

class Comunicado(models.Model):
    _name = 'comunicado'
    _description = 'Comunicado'

    title = fields.Char(string='Title', required=True)
    content = fields.Text(string='Content', required=True)
    recipient_ids = fields.Many2many('res.partner', string='Recipients')

    @api.model
    def create(self, vals):
        record = super(Comunicado, self).create(vals)
        record.send_push_notification()
        return record

    def send_push_notification(self):
        for record in self:
            notification = self.env['push.notification'].create({
                'title': record.title,
                'message': record.content,
                'recipient_ids': [(6, 0, record.recipient_ids.ids)]
            })
            notification.send_notification()
