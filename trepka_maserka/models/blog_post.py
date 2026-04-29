from odoo import models, fields

class TrepkaBlogPost(models.Model):
    _name = "trepka.blog.post"
    _description = "Blog objava"
    _order = "date_published desc"

    name = fields.Char("Naslov", required=True)
    slug = fields.Char("URL slug", required=True, help="Npr. moja-objava (brez presledkov)")
    subtitle = fields.Char("Podnaslov")
    body = fields.Text("Vsebina", required=True)
    image = fields.Image("Naslovna slika", max_width=1200, max_height=800)
    date_published = fields.Date("Datum objave", required=True)
    author = fields.Char("Avtor", default="Trepka Maserka")
    is_published = fields.Boolean("Objavljeno", default=False)
    category = fields.Char("Kategorija")
    meta_description = fields.Text("Meta opis (SEO)")
