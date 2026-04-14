from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    x_line_number = fields.Integer(
        string="#",
        compute="_compute_line_number",
        store=False,
    )

    @api.depends("order_id.order_line")
    def _compute_line_number(self):
        for order in self.mapped("order_id"):
            lines = order.order_line.filtered(lambda l: not l.display_type)
            for idx, line in enumerate(lines, start=1):
                line.x_line_number = idx
        for line in self.filtered(lambda l: l.display_type):
            line.x_line_number = 0