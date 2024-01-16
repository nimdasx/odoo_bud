from odoo import models, fields


class SfDrugBud(models.Model):
    _name = 'sf_drug_bud'
    _description = 'Iki data beyond use date per obat'

    sf_drug_id = fields.Many2one("sf_drug", required=True, ondelete='cascade')
    sf_solvent_id = fields.Many2one("sf_solvent", required=True, ondelete='cascade', string="Solvent")
    concentration = fields.Char(string="Solvent Concentration")
    description = fields.Text(string="Description")
    storage_temperature_min = fields.Integer(string="Storage Temperature Minimal (C)")
    storage_temperature_max = fields.Integer(string="Storage Temperature Maximal (C)")
    expired_in = fields.Integer()
    expired_unit = fields.Selection(
        selection=[
            ('hour', 'Hour'),
            ('day', 'Day'),
            ('month', 'Month')
        ],
        default="hour")

    # tambahkan nama solvent disini agar bisa dipanggil oleh sf_drug
    solvent_name = fields.Char(related='sf_solvent_id.name', string="Solvent Name", store=True)
