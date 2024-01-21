from odoo import models, fields, api


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
    _sql_constraints = [
        ('name_check', 'unique(name)', 'Drug Name must unique!')
    ]
    drug_concentration = fields.Char()
    description = fields.Text()
    sf_catdrug_id = fields.Many2one("sf_catdrug",ondelete='cascade',string="Drug Category")

    # list drug_bud, sf_drug_id dari tabel sf_drug_bud.sf_drug_id
    # field ini gak ada di database
    sf_drug_bud_ids = fields.One2many("sf_drug_bud", "sf_drug_id", string="Beyond Use Date")

    # loop semua description yang ada di sf_drug_bud.description, ini untuk nampilin semua description
    # sf_drug_bud_descriptions = fields.Text(compute="_compute_sf_drug_bud_descriptions", string="BUD Descriptions")
    # @api.depends('sf_drug_bud_ids.description')
    # def _compute_sf_drug_bud_descriptions(self):
    #     for record in self:
    #         descriptions = record.sf_drug_bud_ids.mapped('description')
    #         record.sf_drug_bud_descriptions = ', '.join(descriptions)

    # loop semua solvent_name yang ada di sf_drug_bud.solvent_name, ini untuk nampilin semua solvent name
    sf_drug_bud_solvent_names = fields.Char(compute="_compute_sf_drug_bud_solvent_name", string="Solvents")

    @api.depends('sf_drug_bud_ids.solvent_name')
    def _compute_sf_drug_bud_solvent_name(self):
        for record in self:
            solvent_names = record.sf_drug_bud_ids.mapped('solvent_name')
            record.sf_drug_bud_solvent_names = ', '.join(solvent_names)
