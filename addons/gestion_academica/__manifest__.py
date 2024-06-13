{
    "name": "Gestion Academica",
    "version": "17.0.1.0.0",
    "category": "Industries",
    "summary": "Efficiently manage teachers, students, classes, attendance, "
    "fees, and more with our Music School Management module. ",
    "description": """Simplify music school operations with this comprehensive 
    Odoo module. Manage teachers and students, track attendance, handle fees,
    and plan events effortlessly. Stay organized and focus on nurturing 
    musical talent.""",
    "author": "Cybrosys Techno Solutions",
    "company": "Cybrosys Techno Solutions",
    "maintainer": "Cybrosys Techno Solutions",
    "website": "https://www.cybrosys.com",
    "depends": ["stock", "sale", "calendar", "event", "hr"],
    "data": [
        "security/music_school_institute_groups.xml",
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
        'views/curso_views.xml',
        'views/estudiante_views.xml',        
        'views/materia_views.xml',
        'views/paralelo_views.xml',        
        'views/tutor_views.xml',        
        "views/menu_views.xml",
    
    ],
    "license": "LGPL-3",
    "images": ["static/description/banner.jpg"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
