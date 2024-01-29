from odoo import http
from odoo.http import request, Response
import json


class BudController(http.Controller):

    @http.route('/sf_drug/get_list', type='http', auth='public')
    def sf_drug_get_list(self, **kw):
        # Logic to retrieve data from Odoo
        # data = {
        #     'message': 'Hello from Odoo JSON API',
        #     'data': [1, 2, 3, 4, 5],
        # }

        search_param = kw.get('search_param', '')

        if search_param:
            xyz = request.env['sf_drug'].sudo().search([('name', 'ilike', search_param)])
        else:
            xyz = request.env['sf_drug'].sudo().search([])

        data = [{
            'id': xy.id,
            'name': xy.name,
            'description': xy.description,
        } for xy in xyz]
        return Response(json.dumps(data), content_type='application/json')

    @http.route('/sf_drug/get/<int:record_id>', type='http', auth='public')
    def sf_drug_get(self, record_id):
        drug_record = request.env['sf_drug'].sudo().search([('id', '=', record_id)], limit=1)

        if drug_record:

            # Mengambil data dari field One2many sf_drug_bud_ids
            drug_bud_data = []
            for x in drug_record.sf_drug_bud_ids:

                # tambahkan s kalau lebih dari 1
                telo = ''
                if x.expired_in > 1:
                    telo = 's'

                bud_data = {
                    'id': x.id,
                    'sf_solvent_id': x.sf_solvent_id.id,
                    'concentration': x.concentration,
                    'storage_temperature': x.storage_temperature,
                    'expired_in': x.expired_in,
                    'expired_unit': x.expired_unit,
                    'sf_solvent_name': x.sf_solvent_id.name,
                    'sentence': ("Dissolved in " + x.sf_solvent_id.name +
                                 ", at temperature of " + x.storage_temperature +
                                 ", it expires within " + str(x.expired_in) + " " + x.expired_unit + telo)
                }
                drug_bud_data.append(bud_data)

            # ambil data sf_drug
            data = {
                'id': drug_record.id,
                'name': drug_record.name,
                'drug_concentration': drug_record.drug_concentration,
                'description': drug_record.description,
                'sf_catdrug_name': drug_record.sf_catdrug_id.name,
                'sf_drug_bud_list': drug_bud_data,
            }
            return Response(json.dumps(data), content_type='application/json')
        else:
            return Response(json.dumps({'error': 'Record not found'}), content_type='application/json')
