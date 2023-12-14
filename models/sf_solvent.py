from odoo import models, fields


class SfSolvent(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'sf_solvent'
    _description = 'Solvent'

    name = fields.Char(
        string="Solvent Name",
        required=True,
        tracking=True,
        help="Input solvent name here")
    description = fields.Text()

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Solvent Name must unique!')
    ]
