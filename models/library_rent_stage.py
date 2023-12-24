from odoo import models, fields, api

class LibraryRentStage(models.Model):
    _name = 'library.rent.stage'
    _order = 'sequence,name'
    
    name = fields.Char()
    fold = fields.Boolean()
    book_state = fields.Selection(
        [('available', 'Available'),
         ('borrowed', 'Borrowed'),
         ('lost', 'Lost')
         ],
        'State',
        default="available"
    )
    
    