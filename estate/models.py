from odoo import fields, models

class Estate(models.Model):
    _name = "estate"
    _description = "Estate"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Date.add(fields.Date.today(), days=90), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='G. Orientation',
        selection=[('north','North'),('south','South'),('East','East'),('west','West')],
        help="Choose the garden orientation"
    )
    
    active = fields.Boolean(default=False)
    state = fields.Selection(
        selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
        required=True,
        copy=False,
        default='new',
    )
    
    type_id = fields.Many2one("estate.type", string="Type")

    salesman_id = fields.Many2one('res.partner', string='Salesman')
    buyer_id = fields.Many2one('res.users', string='Buyer')

class Type(models.Model):
    _name = "estate.type"
    _description = "Estate type"
    
    name = fields.Char()
    