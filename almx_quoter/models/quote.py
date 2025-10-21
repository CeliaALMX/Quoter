from odoo import fields, models, api, _
from odoo.exceptions import UserError
import re

class MyAppItem(models.Model):
    _name = "app.quote"
    _description = "Cotizador de elevadores"

    name = fields.Char(string="Folio de Cotización", default="/", copy=False, readonly=True, tracking=True)
    date_order = fields.Datetime(string="Fecha de Cotización", default=fields.Datetime.now, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True, domain=[('customer_rank', '>', 0)])
    user_id = fields.Many2one("res.users", string="Vendedor", default=lambda s: s.env.user)
    company = fields.Many2one('res.company', string='Compañía', compute='_compute_company', store=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('sent', 'Enviada'),
        ('confirmed', 'Confirmada'),
        ('cancel', 'Cancelada'),
    ], default='draft', tracking=True, string="Estado")
    line_ids = fields.One2many('app.quote.line', 'quote_id', string="Líneas")
    amount_total = fields.Float(string="Total", compute='_compute_amount_total', store=True)

    # Configuración General del Elevador
    elevator_quant = fields.Integer(string="Cantidad de Elevadores", default=1, required=True)
    group_elevator = fields.Selection([
        ('simplex', 'Simplex'),
        ('normalx', 'Normalx'),
        ('grandex', 'Grandex'),
        ('extragx', 'Extragx')
    ], tracking=True, string="Grupo de Elevadores", required=True)
    capacity_elevator = fields.Char(required=True, string="Capacidad (kg)")
    entrance_type = fields.Selection([
        ('frontal', 'Frontal'),
        ('left', 'Izquierda'),
        ('right', 'Derecha')
    ], tracking=True, string="Tipo de Entrada", required=True)
    door_height = fields.Integer(string="Altura de Puerta (m)", required=True, help="Altura de puertas medida en milímetros", default=False)
    door_type = fields.Selection([
        ('o_right', 'Apertura derecha'),
        ('o_left', 'Apertura izquierda'),
        ('o_central', 'Apertura central')
    ], tracking=True, string="Tipo de Puerta", required=True)
    door_width = fields.Integer(string="Ancho de Puerta (m)", required=True, help="Ancho de puertas medida en milímetros", default=False)
    type_install = fields.Selection([
        ('residence', 'Residencial'),
        ('commercial', 'Comercial'),
        ('car_lift', 'Montacoches')
    ], tracking=True, string="Tipo de Instalación", required=True, default=False)
    car_door = fields.Selection([
        ('half_cabin', 'Media cabina'),
        ('manual', 'Manual abatible en inox con cristal templado')
    ], tracking=True, string="Puerta de Cabina", required=True)
    landing_door = fields.Selection([
        ('half_height', 'Media Altura'),
        ('manual_lading', 'Manual abatible en inox con cristal templado')
    ], tracking=True, string="Puerta de Desembarque", required=True)
    car_model = fields.Selection([
        ('medium_plataform', 'Mediana plataforma'),
        ('large_plataform', 'Gran Plataforma')
    ], tracking=True, string="Modelo de Cabina", required=True)
    car_floor = fields.Selection([
        ('pvc', 'PVC'),
        ('plastic', 'Plástico'),
        ('lamina', 'Lámina')
    ], tracking=True, string="Piso de Cabina", required=True)

    # Especificaciones Técnicas
    zona_sismica = fields.Char(required=True, string="Zona Sísmica", help="Zona sísmica", tracking=True)
    recorrido_de_planta_baja_a_planta_alta = fields.Char(required=True, string="Recorrido Planta Baja a Planta Alta (m)", help="Coloca la distancia que recorre desde la planta baja hasta la planta alta", tracking=True)
    fase = fields.Char(required=True, string="Fase Eléctrica", help="Coloca la fase que tendrá la cabina", tracking=True)
    profundidad = fields.Char(required=True, string="Profundidad del Cubo (m)", help="Profundidad del lugar donde se colocará el elevador", tracking=True)
    distancia_de_la_sala_de_maquinas_por_encima_del_piso_superior = fields.Char(required=True, string="Distancia Sala de Máquinas (m)", tracking=True)
    acabado_de_cabina = fields.Char(required=True, string="Acabado de Cabina", help="Acabado de cabina que tendrá el elevador", tracking=True)
    acabado_de_media_cabina = fields.Char(required=True, string="Acabado de media cabina", help="Coloca cuál va a ser el acabado de la media cabina que se colocará", tracking=True)
    acabado_de_abatibles = fields.Char(required=True, string="Acabado de Puertas Abatibles", help="Coloca el acabado que tendrá los abatibles", tracking=True)
    nomenclatura_del_piso = fields.Char(required=True, string="Nomenclatura de Piso", help="Coloca la nomenclatura que tendrá el piso de la cabina del elevador", tracking=True)
    tipo_de_cubo = fields.Char(required=True, string="Tipo de Cubo", help="Coloca el tipo de cubo que se hará para el cubo del elevador", tracking=True)
    puerta_resistente_al_fuego = fields.Selection([
        ('yes', 'Sí'),
        ('no', 'No'),
        ('null', 'Opción predeterminada')
    ], default="null", tracking=True, string="Puerta Resistente al Fuego", required=True)
    modelo_COP = fields.Char(required=True, string="Panel de Control (COP)", help="Coloca el modelo de COP", tracking=True)
    modelo_LOP = fields.Char(required=True, string="Panel de Piso (LOP)", help="Coloca el modelo de LOP", tracking=True)
    velocidad = fields.Char(required=True, string="Velocidad (m/s)", help="Coloca la velocidad del elevador", tracking=True)
    total_de_paradas = fields.Char(required=True, string="Total de Paradas", help="Coloca el total de paradas que tendrá el elevador", tracking=True)
    dimenciones_de_la_cabina = fields.Char(required=True, string="Dimensiones de Cabina (m)", help="Coloca las dimensiones que tendrá la cabina", tracking=True)
    ancho_de_la_puerta = fields.Char(required=True, string="Ancho de Puerta (m)", help="Coloca el ancho que tendrán las puertas", tracking=True)
    uso_del_elevador = fields.Char(required=True, string="Uso del Elevador", help="Coloca cuál será el uso que se le dará al elevador", tracking=True)
    regla_de_velocidad_CP = fields.Char(required=True, string="Regla de Velocidad CP", help="Coloca la regla de velocidad CP", tracking=True)
    modelo_del_elevador = fields.Char(required=True, string="Modelo del Elevador", help="Coloca el modelo del elevador que se colocará", tracking=True)
    tipo_de_maquina = fields.Char(required=True, string="Tipo de Máquina", help="Coloca el tipo de máquina", tracking=True)
    tipo_de_puerta_para_el_hueco = fields.Char(required=True, string="Tipo de Puerta del Hueco", help="Coloca el tipo de puerta que tendrá para el hueco", tracking=True)
    altura = fields.Char(required=True, string="Altura del Cubo (m)", help="Coloca la altura que tendrá el elevador", tracking=True)
    acabado = fields.Char(required=True, string="Acabado General", help="Coloca el acabado", tracking=True)
    tipo_de_entrada = fields.Char(required=True, string="Tipo de entrada", help="Coloca el tipo de entrada", tracking=True)
    traccion = fields.Selection([
        ('2 a 1', '2 a 1'),
        ('1 a 1', '1 a 1'),
        ('null', 'Opción predeterminada')
    ], default="null", tracking=True, string="Sistema de Tracción", required=True)
    ancho_de_cabina = fields.Char(required=True, string="Ancho de Cabina (m)", help="Coloca el ancho que tendrá la cabina", tracking=True)
    profundidad_de_cabina = fields.Char(required=True, string="Profundidad de Cabina (m)", help="Coloca la profundidad que tendrá la cabina", tracking=True)
    area_de_cabina = fields.Char(required=True, string="Área de Cabina (m²)", help="Coloca el área de la cabina", tracking=True)
    area_del_cubo = fields.Char(required=True, string="Área del Cubo (m²)", help="Coloca el área del cubo que tendrá el cubo para el elevador", tracking=True)
    ancho_del_cubo = fields.Char(required=True, string="Ancho del Cubo (m)", help="Coloca el ancho del cubo que tendrá el elevador", tracking=True)
    profundidad_del_cubo = fields.Char(required=True, string="Profundidad del Cubo (m)", help="Coloca la profundidad que tendrá el elevador", tracking=True)
    rieles_de_cabina = fields.Char(required=True, string="Rieles de Cabina", help="Coloca los tipos de rieles que tendrá el elevador", tracking=True)
    entrerieles_de_cabina = fields.Char(required=True, string="Distancia entre Rieles de Cabina (m)", help="Coloca los entrerieles que tendrá el elevador", tracking=True)
    rieles_de_contrapeso = fields.Char(required=True, string="Rieles de Contrapeso", help="Coloca los rieles del contrapeso que tendrá el elevador", tracking=True)
    entrerieles_de_contrapeso = fields.Char(required=True, string="Distancia entre Rieles de Contrapeso (m)", help="Coloca los entrerieles del contrapeso que tendrá el elevador", tracking=True)
    sobrepeso = fields.Char(required=True, string="Sobrepeso (kg)", help="Coloca el sobrepeso del elevador", tracking=True)
    fosa = fields.Char(required=True, string="Profundidad de Fosa (m)", help="Coloca la fosa del elevador", tracking=True)
    recorrido = fields.Char(required=True, string="Recorrido Total (m)", help="Coloca el recorrido del elevador", tracking=True)
    control = fields.Char(required=True, string="Sistema de Control", help="Coloca el control del elevador", tracking=True)
    version_del_plano = fields.Char(required=True, string="Versión del Plano", help="Coloca la versión del plano", tracking=True)

    @api.depends('user_id')
    def _compute_company(self):
        for record in self:
            if record.user_id and record.user_id.company_id:
                record.company = record.user_id.company_id
            else:
                record.company = False

    @api.depends('line_ids.price_total')
    def _compute_amount_total(self):
        for record in self:
            record.amount_total = sum(line.price_total for line in record.line_ids)

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
    name = fields.Char(string="Descripción")
    quantity = fields.Float(string="Cantidad", default=1.0)
    price_unit = fields.Float(string="Precio unitario", default=0.0)
    price_total = fields.Float(string="Total línea", compute='_compute_price_total', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_price_total(self):
        for line in self:
            line.price_total = line.quantity * line.price_unit
