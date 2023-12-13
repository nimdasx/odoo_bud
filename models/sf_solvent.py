from odoo import models, fields


class SfSolvent(models.Model):
    _name = 'sf_solvent'
    _description = 'Solvent'

    name = fields.Char(
        string="Solvent Name",
        required=True,
        tracking=True,
        help="Input solvent name here")
    description = fields.Text()

    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']
