from odoo import models, fields

class TrepkaBooking(models.Model):
    _name = 'trepka.booking'
    _description = 'Rezervacija masaže'
    _order = 'booking_date, time_slot'

    name = fields.Char('Ime in priimek', required=True)
    email = fields.Char('E-mail', required=True)
    phone = fields.Char('Telefon')
    service = fields.Selection([
        ('relax_45', 'Relaxacijska masaža 45 min'),
        ('swedish_60', 'Švedska masaža 60 min'),
        ('sports_90', 'Športna masaža 90 min'),
    ], required=True, string='Storitev')
    booking_date = fields.Date('Datum', required=True)
    time_slot = fields.Char('Termin', required=True)
    notes = fields.Text('Opombe')
    state = fields.Selection([
        ('pending', 'Čaka potrditev'),
        ('confirmed', 'Potrjeno'),
        ('cancelled', 'Preklicano'),
    ], default='pending', string='Status')
