from odoo import fields, models, api
from odoo.exceptions import UserError
import base64

class MyAppItem(models.Model):
    _name = "app.quote"
    _description = "Cotizador de elevadores"

    date_order = fields.Datetime(string="Fecha de Cotización", default=fields.Datetime.now, required=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True, domain=[('customer_rank', '>', 0)])
    user_id = fields.Many2one("res.users", string="Vendedor", default=lambda s: s.env.user, required=True)
    user_email = fields.Char(string='Correo del Contacto', related='user_id.email', store=True, readonly=True)
    user_phone = fields.Char(string='Teléfono del Usuario', related='user_id.partner_id.phone', store=True, readonly=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('sent', 'Enviada'),
        ('confirmed', 'Confirmada'),
        ('cancel', 'Cancelada')],
        default='draft', required=True)

    nombre_del_comprador = fields.Many2one(
        comodel_name='res.partner',
        string="Nombre del Comprador",
        required=True,
        domain=["|", ('customer_rank', '>', 0), ('user_ids', '!=', False)],
        help="Selecciona el comprador o usuario registrado."
    )
    compania_del_comprador = fields.Char(string="Compañía del Comprador", readonly=True)
    ubicacion_de_la_empresa = fields.Char(string="Ubicación de la Empresa", readonly=True)
    correo_electronico = fields.Char(string="Correo Electrónico", readonly=True)
    codigo_postal = fields.Char(string="Código Postal", readonly=True)
    ciudad = fields.Char(string="Ciudad", readonly=True)

    @api.onchange('nombre_del_comprador')
    def _onchange_nombre_del_comprador(self):
        if self.nombre_del_comprador:
            self.compania_del_comprador = self.nombre_del_comprador.parent_id.name or self.nombre_del_comprador.name
            self.ubicacion_de_la_empresa = self.nombre_del_comprador.street or ''
            self.correo_electronico = self.nombre_del_comprador.email or ''
            self.codigo_postal = self.nombre_del_comprador.zip or ''
            self.ciudad = self.nombre_del_comprador.city or ''
        else:
            self.compania_del_comprador = False
            self.ubicacion_de_la_empresa = False
            self.correo_electronico = False
            self.codigo_postal = False
            self.ciudad = False

    folio = fields.Char(string="Folio", readonly=True, copy=False, default="/")
    line_ids = fields.One2many('app.quote.line', 'quote_id', string="Líneas", required=True)
    amount_total = fields.Float(string="Total", compute='_compute_amount_total', store=True, required=True)
    elevator_quant = fields.Integer(string="Cantidad de Elevadores", default=1, required=True)
    group_elevator = fields.Selection([
        ('simplex', 'Simple'),
        ('normalx', 'Normal'),
        ('grandex', 'Grande'),
        ('extragx', 'Extragrande')], string="Grupo de Elevadores", required=True)
    capacity_elevator = fields.Char(required=True, string="Capacidad (kg)")
    entrance_type = fields.Selection([
        ('frontal', 'Frontal'),
        ('left', 'Izquierda'),
        ('right', 'Derecha')], string="Tipo de Entrada", required=True)
    door_height = fields.Integer(string="Altura de Puerta (m)", required=True)
    door_type = fields.Selection([
        ('o_right', 'Apertura derecha'),
        ('o_left', 'Apertura izquierda'),
        ('o_central', 'Apertura central')], string="Tipo de Puerta", required=True)
    door_width = fields.Float(string="Ancho de Puerta de Cabina (m)", required=True)
    type_install = fields.Selection([
        ('residence', 'Residencial'),
        ('commercial', 'Comercial'),
        ('car_lift', 'Montacoches')], string="Tipo de Instalación", required=True)
    car_door = fields.Selection([
        ('half_cabin', 'Media cabina'),
        ('manual', 'Manual abatible en inox con cristal templado')], string="Puerta de Cabina", required=True)
    landing_door = fields.Selection([
        ('half_height', 'Media Altura'),
        ('manual_lading', 'Manual abatible en inox con cristal templado')], string="Puerta de Desembarque", required=True)
    car_model = fields.Selection([
        ('medium_plataform', 'Mediana plataforma'),
        ('large_plataform', 'Gran Plataforma')], string="Modelo de Cabina", required=True)
    car_floor = fields.Selection([
        ('pvc', 'PVC'),
        ('plastic', 'Plástico'),
        ('lamina', 'Lámina')], string="Piso de Cabina", required=True)
    zona_sismica = fields.Char(required=True, string="Zona Sísmica")
    recorrido_de_planta_baja_a_planta_alta = fields.Char(required=True, string="Recorrido Planta Baja a Planta Alta (m)")
    fase = fields.Char(required=True, string="Fase Eléctrica")
    profundidad = fields.Char(required=True, string="Profundidad General (m)")
    distancia_de_la_sala_de_maquinas_por_encima_del_piso_superior = fields.Char(required=True, string="Distancia Sala de Máquinas (m)")
    acabado_de_cabina = fields.Char(required=True, string="Acabado de Cabina")
    acabado_de_media_cabina = fields.Char(required=True, string="Acabado de media cabina")
    acabado_de_abatibles = fields.Char(required=True, string="Acabado de Puertas Abatibles")
    nomenclatura_del_piso = fields.Char(required=True, string="Nomenclatura de Piso")
    tipo_de_cubo = fields.Char(required=True, string="Tipo de Cubo")
    puerta_resistente_al_fuego = fields.Selection([
        ('yes', 'Sí'),
        ('no', 'No'),
        ('null', 'Opción predeterminada')], default="null", string="Puerta Resistente al Fuego", required=True)
    modelo_COP = fields.Char(required=True, string="Panel de Control (COP)")
    modelo_LOP = fields.Char(required=True, string="Panel de Piso (LOP)")
    velocidad = fields.Char(required=True, string="Velocidad (m/s)")
    total_de_paradas = fields.Char(required=True, string="Total de Paradas")
    dimenciones_de_la_cabina = fields.Char(required=True, string="Dimensiones de Cabina (m)")
    ancho_de_la_puerta = fields.Float(required=True, string="Ancho de Puerta del Hueco (m)")
    uso_del_elevador = fields.Char(required=True, string="Uso del Elevador")
    regla_de_velocidad_CP = fields.Char(required=True, string="Regla de Velocidad CP")
    modelo_del_elevador = fields.Char(required=True, string="Modelo del Elevador")
    tipo_de_maquina = fields.Char(required=True, string="Tipo de Máquina")
    tipo_de_puerta_para_el_hueco = fields.Char(required=True, string="Tipo de Puerta del Hueco")
    altura = fields.Integer(required=True, string="Altura del Cubo (m)")
    acabado = fields.Char(required=True, string="Acabado General")
    tipo_de_entrada = fields.Char(required=True, string="Tipo de entrada")
    traccion = fields.Selection([
        ('2 a 1', '2 a 1'),
        ('1 a 1', '1 a 1'),
        ('null', 'Opción predeterminada')], default="null", string="Sistema de Tracción", required=True)
    ancho_de_cabina = fields.Char(required=True, string="Ancho de Cabina (m)")
    profundidad_de_cabina = fields.Char(required=True, string="Profundidad de Cabina (m)")
    area_de_cabina = fields.Char(required=True, string="Área de Cabina (m²)")
    area_del_cubo = fields.Char(required=True, string="Área del Cubo (m²)")
    tipo_de_cabina = fields.Selection([
        ('null', 'Opción predeterminada'),
        ('cabina_1', 'MR'),
        ('cabina_2', 'MRL'),
        ('cabina_3', 'MRLE')],
        default='null',
        string='Tipo de cabina',
        required=True
    )
    ancho_del_cubo = fields.Char(required=True, string="Ancho del Cubo (m)")
    profundidad_del_cubo = fields.Char(required=True, string="Profundidad del Cubo (m)")
    rieles_de_cabina = fields.Char(required=True, string="Rieles de Cabina")
    entrerieles_de_cabina = fields.Char(required=True, string="Distancia entre Rieles de Cabina (m)")
    rieles_de_contrapeso = fields.Char(required=True, string="Rieles de Contrapeso")
    entrerieles_de_contrapeso = fields.Char(required=True, string="Distancia entre Rieles de Contrapeso (m)")
    sobrepeso = fields.Char(required=True, string="Sobrepeso (kg)")
    fosa = fields.Char(required=True, string="Profundidad de Fosa (m)")
    recorrido = fields.Char(required=True, string="Recorrido Total (m)")
    control = fields.Char(required=True, string="Sistema de Control")
    version_del_plano = fields.Char(required=True, string="Versión del Plano")

    @api.depends('line_ids.price_total')
    def _compute_amount_total(self):
        for record in self:
            record.amount_total = sum(line.price_total for line in record.line_ids)

    def write(self, vals):
        for rec in self:
            if rec.state == 'confirmed':
                raise UserError("No se puede modificar una cotización que ya está confirmada.")
        return super(MyAppItem, self).write(vals)

    def action_confirm(self):
        for rec in self:
            if rec.state in ('draft', 'sent'):
                if not rec.folio or rec.folio in ("/", ""):
                    all_folios = self.env['app.quote'].search([('folio', '!=', False)])
                    numeric_folios = []
                    for f in all_folios:
                        if f.folio and "COT/ALAM/" in f.folio:
                            try:
                                num = int(f.folio.split("COT/ALAM/")[1])
                                numeric_folios.append(num)
                            except Exception:
                                continue
                        elif str(f.folio).isdigit():
                            numeric_folios.append(int(f.folio))
                    next_folio = max(numeric_folios) + 1 if numeric_folios else 1
                    rec.folio = f"COT/ALAM/{next_folio:06d}"
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

    def action_generate_blank_pdf(self):
        pdf_content = b"%PDF-1.4\n1 0 obj<<>>endobj\ntrailer<<>>\n%%EOF\n"
        pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')
        url = f"data:application/pdf;base64,{pdf_base64}"
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }

class ElevatorQuoteLine(models.Model):
    _name = 'app.quote.line'
    _description = 'Línea de cotización'

    quote_id = fields.Many2one('app.quote', required=True, ondelete='cascade')
    sequence = fields.Integer(default=10, required=True)
    product_id = fields.Many2one('product.product', string="Producto", required=True)
    name = fields.Char(string="Descripción", required=True)
    quantity = fields.Float(string="Cantidad", default=1.0, required=True)
    price_unit = fields.Float(string="Precio unitario", default=0.0, required=True)
    price_total = fields.Float(string="Total línea", compute='_compute_price_total', required=True, store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_price_total(self):
        for line in self:
            line.price_total = line.quantity * line.price_unit
