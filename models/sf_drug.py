from odoo import models, fields


class SfDrug(models.Model):
    _name = 'sf_drug'
    _description = 'Drug'

    name = fields.Char(
        string="Drug Name",
        required=True,
        tracking=True,
        help="Input drug name here")
    description = fields.Text()

    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']
