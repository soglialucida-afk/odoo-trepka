{
    'name': 'Trepka Maserka Theme',
    'version': '19.0.1.0.0',
    'category': 'Theme/Services',
    'summary': 'Elegantna tema za frizerski in kozmetični salon',
    'author': 'Soglia Lucida',
    'depends': ['website'],
    'data': [
        'views/templates.xml',
        'data/website_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'trepka_maserka/static/src/css/theme.css',
            'trepka_maserka/static/src/js/slider.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
