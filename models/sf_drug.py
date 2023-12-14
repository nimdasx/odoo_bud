from odoo import models, fields


class SfDrug(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'sf_drug'
    _description = 'Drug'

    name = fields.Char(
        string="Drug Name",
        required=True,
        tracking=True,
        help="Input drug name here")
    description = fields.Text()

    # list drug_bud, sf_drug_id dari tabel sf_drug_bud.sf_drug_id
    sf_drug_bud_ids = fields.One2many("sf_drug_bud", "sf_drug_id", string="Beyond Use Date")
