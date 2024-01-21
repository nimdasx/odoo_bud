from odoo import models, fields


class SfCatdrug(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'sf_catdrug'
    _description = 'Drug Category'

    name = fields.Char(
        string="Drug Category Name",
        required=True,
        tracking=True,
        help="Input drug category name here")
    description = fields.Text()

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Drug Category Name must unique!')
    ]
