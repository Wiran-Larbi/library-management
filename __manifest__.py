{
    'name': 'Library Book Category Management',
    'version': '1.0',
    'summary': 'Manage book categories in a library',
    'description': """
        This module allows you to manage book categories in a library.
        You can create, edit, and organize categories hierarchically.
    """,
    'category': 'Library/Management',
    'author': 'DotCipher',
    'depends': ['base'],
    'data': [
        'views/library_book_categ_view.xml',
        'views/library_book_rent_view.xml',
        'views/library_book_view.xml',
        'views/library_rent_stage_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}