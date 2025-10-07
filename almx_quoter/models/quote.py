from odoo import fields, models, api, _
from odoo.exceptions import UserError

class MyAppItem(models.Model):
    _name = "app.quote"
    _description = "Cotizador de elevadores"

    name = fields.Char(string="Folio", default="/", copy=False, readonly=True, tracking=True)
    date_order = fields.Datetime(string="Fecha de la orden", default=fields.Datetime.now, tracking=True)
    partner_id = fields.Char(required=True, string='Cliente')
    user_id = fields.Many2one("res.users", string="Vendedor", default=lambda s: s.env.user)
    company = fields.Char(required=True, string='Compañía')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('sent', 'Enviada'),
        ('confirmed', 'Confirmada'),
        ('cancel', 'Cancelada'),
    ], default='draft', tracking=True, string="Estado")

    line_ids = fields.One2many('app.quote.line', 'quote_id', string="Líneas")
    amount_total = fields.Float("Total")  # de momento manual, luego lo calculas

class ElevatorQuoteLine(models.Model):
    _name = 'app.quote.line'
    _description = 'Línea de cotización'

    quote_id = fields.Many2one('app.quote', required=True, ondelete='cascade')
    sequence = fields.Integer(default=10)
    product_id = fields.Many2one('product.product', string="Producto")
    name = fields.Char("Descripción")
    quantity = fields.Float("Cantidad", default=1.0)
    price_unit = fields.Float("Precio unitario", default=0.0)
    price_total = fields.Float("Total línea")  # por ahora manual