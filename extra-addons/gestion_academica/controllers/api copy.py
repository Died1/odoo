from odoo import http
from odoo.http import request
import json



class Api(http.Controller):


    @http.route(['/api/comunicados'], auth='none', methods=['GET'], type='http', csrf=False)
    def get_comunicados(self):
        # Supongamos que tienes una lista de datos para retornar
        data = [
            {
                "comunicado": {
                    "id": "12345",
                    "titulo": "Reunión Anual",
                    "descripcion": "La reunión anual de la empresa se llevará a cabo el próximo viernes.",
                    "imagen": "https://example.com/imagen.jpg",
                    "fecha": "2024-05-21",
                    "hora": "15:30",
                    "ubicacion": "Sala de Conferencias A",
                    "tipo": "Reunión",
                    "prioridad": "Alta",
                    "enlace": "https://example.com/reunion",
                    "adjuntos": [
                        {
                            "nombre": "Agenda.pdf",
                            "url": "https://example.com/agenda.pdf"
                        }
                    ],
                    "autor": {
                        "nombre": "Juan Pérez",
                        "email": "juan.perez@example.com"
                    },
                    "estado": "Pendiente"
                }
            },
            {
                "comunicado": {
                    "id": "123456",
                    "titulo": "Dia de la madre",
                    "descripcion": "La reunión se acordara los agasajos y cuanto sera el aporte. se llevará a cabo el próximo jueves.",
                    "imagen": "https://example.com/imagen.jpg",
                    "fecha": "2024-05-21",
                    "hora": "15:30",
                    "ubicacion": "Sala de Conferencias A",
                    "tipo": "Reunión",
                    "prioridad": "Alta",
                    "enlace": "https://example.com/reunion",
                    "adjuntos": [
                        {
                            "nombre": "Agenda.pdf",
                            "url": "https://example.com/agenda.pdf"
                        }
                    ],
                    "autor": {
                        "nombre": "Juan Pérez",
                        "email": "juan.perez@example.com"
                    },
                    "estado": "Pendiente"
                }
            }
        ]
        # Serializa los datos a JSON
        json_data = json.dumps(data)
        # Retorna la respuesta con los datos serializados en JSON
        return http.Response(json_data, status=200, mimetype='application/json')



    @http.route(['/api/comunicados/<int:comunicado_id>'], auth='none', methods=['GET'], type='http', csrf=False)
    def get_comunicado_by_id(self, comunicado_id=0):
        data = {
            "id": comunicado_id,
            "titulo": "Dia de la madre",
            "descripcion": "La reunión se acordara los agasajos y cuanto sera el aporte. se llevará a cabo el próximo jueves.",
            "imagen": "https://example.com/imagen.jpg",
            "fecha": "2024-05-21",
            "hora": "15:30",
            "ubicacion": "Sala de Conferencias A",
            "tipo": "Reunión",
            "prioridad": "Alta",
            "enlace": "https://example.com/reunion",
            "adjuntos": [
                {
                    "nombre": "Agenda.pdf",
                    "url": "https://example.com/agenda.pdf"
                }
            ],
            "autor": {
                "nombre": "Juan Pérez",
                "email": "juan.perez@example.com"
            },
            "estado": "Pendiente"
        }
        json_data = json.dumps(data)
        return http.Response(json_data, status=200, mimetype='application/json')



    @http.route(['/api/asistencias/<int:asistencia_id>'], auth='none', methods=['GET'], type='http', csrf=False)
    def get_asistencia_by_id(self, asistencia_id=0):
        data = {
            'type': 'asistencia',
            'details': {
                'student_id': 123,
                'class_id': 123,
                'timestamp': '12-12-2012',
            }
        }
        json_data = json.dumps(data)
        return http.Response(json_data, status=200, mimetype='application/json')



    @http.route(['/api/salidas/<int:salida_id>'], auth='none', methods=['GET'], type='http', csrf=False)
    def get_salida_by_id(self, salida_id=0):
        data = {
            'type': 'salida',
            'details': {
                'student_id': 123,
                'class_id': 123,
                'timestamp': '12-12-2012',
            }
        }
        json_data = json.dumps(data)
        return http.Response(json_data, status=200, mimetype='application/json')

    @http.route(['/api/employes'], auth='none', methods=['GET'], type='http', csrf=False)
    def get_employes(self):
        employees = request.env['hr.employee'].sudo().search([])
        employee_data = []

        for employee in employees:
            employee_data.append({
                'id': employee.id,
                'name': employee.name,
                'work_email': employee.work_email,
                'job_title': employee.job_id.name if employee.job_id else '',
                'department': employee.department_id.name if employee.department_id else ''
            })

        return request.make_response(json.dumps(employee_data), headers={'Content-Type': 'application/json'})

        for employee in employees:
            employee_data.append({
                'id': employee.id,
                'name': employee.name,
                'work_email': employee.work_email,
                'job_title': employee.job_id.name if employee.job_id else '',
                'department': employee.department_id.name if employee.department_id else ''
            })

        return request.make_response(json.dumps(employee_data), headers={'Content-Type': 'application/json'})

