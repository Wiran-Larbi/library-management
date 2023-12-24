from odoo import api, models, fields
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta



class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _rec_name = 'short_name'
    
    short_name = fields.Char('Short Title', required=True)
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    date_updated = fields.Date('Last Updated')
    active = fields.Boolean(default=True)
    author_ids = fields.Many2many('res.partner', string='Authors')
    state = fields.Selection(
        [('available', 'Disponible'),
         ('borrowed', 'Emprinte'),
         ('lost', 'Perdu') 
        ],'State',default='Disponible'
    )
    cost_price = fields.Float('Book Cost')
    category_id = fields.Many2one('library.book.category')
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price')
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print ?')
    pages = fields.Integer('Number of Pages')
    nbr_jours = fields.Integer(compute='_compute_nbr_jours',string='Nombre de jours depuis la date de sortie',store=True)
    
    def make_available(self):
        self.ensure_one()
        self.state = 'available'
        
    def make_borrowed(self):
        self.ensure_one()
        self.state = 'borrowed'
        
    def make_lost(self):
        self.ensure_one()
        self.state = 'lost'
        
    @api.constrains('date_release', 'date_updated')
    def _compute_nbr_jours(self):
        for rec in self:
            if rec.date_updated:
                delta = rec.date_updated - rec.date_release
                rec.nbr_jours = delta.days
    