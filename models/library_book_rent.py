from odoo import models, fields, api


class LibraryBookRent(models.Model):
    _name = 'library.book.rent'
    
    @api.model
    def _default_rent_stage(self):
        Stage = self.env['library.rent.stage']
        return Stage.search([], limit=1)
    
    book_id = fields.Many2one('library.book', 'Book', required=True)
    borrowed_id = fields.Many2one('res.partner', 'Borrower', required=True)
    state = fields.Selection([('ongoing', 'En cours'), ('returned', 'Rendu')], 'State', default='ongoing', required=True)
    
    rent_date = fields.Date()
    stage_id = fields.Many2one('library.rent.stage',default=_default_rent_stage)
    
    @api.model
    def create(self, vals):
        book_rec = self.env('library.book').browse(vals['book_id'])
        book_rec.make_borrowed()
        return super(LibraryBookRent, self).create(vals)
    
    def book_return(self):
        self.ensure_one()
        self.book_id.make_available()
        self.write({
            'state':'returned',
            'return_date':fields.Date.today()
        })