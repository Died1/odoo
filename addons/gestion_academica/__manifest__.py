{
    "name": "Gestion Academica",
    "version": "17.0",
    "category": "Education",
    "summary": "Administrar eficientemente profesores, estudiantes, clases y asistencia, "
    "tarifas y más con nuestro módulo de Gestión de Escuelas",
    "description": """Simplifique las operaciones académicas con este completo 
    Módulo Odoo. Administre profesores y estudiantes, realice un seguimiento de la asistencia, administre tarifas,
    y planificar eventos sin esfuerzo.""",
    "author": "Cybrosys Techno Solutions",
    "company": "Cybrosys Techno Solutions",
    "maintainer": "Cybrosys Techno Solutions",
    "website": "http://www.campozanodevlab.com",
    "depends": ["stock", "sale", "calendar", "event", "hr"],
    "data": [
        "security/music_school_institute_groups.xml",
        "security/ir.model.access.csv",
        "profesores/views/hr_employee_views.xml",
        'cursos/views/nivel_view.xml',
        'cursos/views/materia_views.xml',
        'cursos/views/curso_views.xml',
        'cursos/views/paralelo_views.xml',   
        'cursos/views/asignatura_views.xml',
        "cursos/views/horario_views.xml",
        'cursos/views/asistencia_views.xml',
                
        'estudiantes/views/estudiante_views.xml', 
        'estudiantes/views/inscripcion_views.xml',        
        'estudiantes/views/tutor_views.xml',        
        
        "views/menu_views.xml",

        'cursos/demo/materia_demo.xml'
    ],
    "license": "LGPL-3",
    "images": ["static/description/banner.jpg"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
