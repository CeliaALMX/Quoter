from odoo import fields, models, api, _
from odoo.exceptions import UserError
import re

class MyAppItem(models.Model):
    _name = "app.quote"
    _description = "Cotizador de elevadores"

    name = fields.Char(string="Folio", default="/", copy=False, readonly=True, tracking=True)
    date_order = fields.Datetime(string="Fecha de la orden", default=fields.Datetime.now, tracking=True)
    partner_id = fields.Many2one(
        'res.partner',
        string='Cliente',
        required=True,
        domain=[('customer_rank', '>', 0)]
    )
    user_id = fields.Many2one("res.users", string="Vendedor", default=lambda s: s.env.user)
    company = fields.Char(required=True, string='Compañía')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('sent', 'Enviada'),
        ('confirmed', 'Confirmada'),
        ('cancel', 'Cancelada'),
    ], default='draft', tracking=True, string="Estado")

    #no sé para q sean, saludos
    line_ids = fields.One2many('app.quote.line', 'quote_id', string="Líneas")
    amount_total = fields.Float("Total")  # de momento manual, luego lo calculas

    # Lista de requerimientos para los elevadores
    elevator_quant = fields.Integer(string="Cantidad de elevadores", default=1, requeried=True)
    group_elevator = fields.Selection([('simplex', 'Simplex'), ('normalx', 'Normalx'), ('grandex', 'Grandex'), ('extragx', 'Extragx'), ],
                     tracking=True, string="Tipo de grupo", requeried=True)
    capacity_elevator = fields.Char(requeried=True, string="Capacidad del elevador")
    entrance_type = fields.Selection([('frontal','Frontal'),('left','Izquierda'),('right','Derecha')], tracking=True, string="Tipo de entrada", requeried=True)
    door_height = fields.Integer(string="Altura de puertas", requeried=True, help="Altura de puertas medida en milimetros", default=False)
    door_type = fields.Selection([('o_right','Apertura derecha'),('o_left','Apertura izquierda'),('o_central','Apertura central')], tracking=True, string="Tipo de puerta", requeried=True)
    door_width = fields.Integer(string="Ancho de puertas", requeried=True, help="Ancho de puertas medida en milimetros", default=False)
    type_install = fields.Selection([('residence','Residencial'),('commercial','Comercial'),('car_lift','Montacoches')], tracking=True, string="Uso", requeried=True, default=False)
    car_door = fields.Selection([('half_cabin','Media cabina'),('manual','Manual abatible en inox con cristal templado')],tracking=True, string="Acabado de puertas de cabina", requeried=True)
    landing_door = fields.Selection([('half_height','Media Altura'),('manual_lading','Manual abatible en inox con cristal templado')],tracking=True, string="Acabado de puertas de piso", requeried=True)
    car_model = fields.Selection([('medium_plataform','Mediana plataforma'),('large_plataform','Gran Plataforma')], tracking=True, string="Modelo de cabina", requeried=True)
    car_floor = fields.Selection([('pvc','PVC'),('plastic','Plastico'),('lamina','Lamina')], tracking=True, string="Piso de cabina", requeried=True)



    #----Acciones de los botones:----
    def action_confirm(self):
        for rec in self:
            if rec.state in ('draft', 'sent'):
                rec.state = 'confirmed'
        return True

    def action_cancel(self):
        for rec in self:
            if rec.state in ('draft', 'sent', 'confirmed'):
                rec.state = 'cancel'
        return True

    def action_set_draft(self):
        for rec in self:
            if rec.state == 'cancel':
                rec.state = 'draft'
        return True

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
