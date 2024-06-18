from odoo import models, fields, api
import requests
import json


class PushNotification(models.Model):
    _name = 'push.notification'
    _description = 'Push Notification'

    title = fields.Char(string='Title', required=True)
    message = fields.Text(string='Message', required=True)
    recipient_ids = fields.Many2many('res.partner', string='Recipients')
    sent_date = fields.Datetime(string='Sent Date')

    def send_notification(self):
        """
        Send the push notification to the recipients.
        """
        for record in self:
            for recipient in record.recipient_ids:
                # Call the method to send the push notification
                self._send_push_to_device(recipient.device_token, record.title, record.message)

            # Update the sent date
            record.sent_date = fields.Datetime.now()

    def _send_push_to_device(self, device_token, title, message):
        """
        Send the push notification to a single device using Firebase Cloud Messaging (FCM).
        """
        # FCM server key from your Firebase project settings
        server_key = 'YOUR_FCM_SERVER_KEY'
        url = 'https://fcm.googleapis.com/fcm/send'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + server_key,
        }

        payload = {
            'to': device_token,
            'notification': {
                'title': title,
                'body': message,
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            return True
        else:
            # Log an error or handle the failure case
            return False
