from odoo import http
from odoo.http import request, Response
import json

class BudController(http.Controller):

    @http.route('/sf_drug/get_list', type='http', auth='public')
    def get_data(self):
        # Logic to retrieve data from Odoo
        # data = {
        #     'message': 'Hello from Odoo JSON API',
        #     'data': [1, 2, 3, 4, 5],
        # }
        xyz = request.env['sf_drug'].sudo().search([])
        data = [{
            'id':xy.id,
            'name':xy.name,
            'description':xy.description,
        } for xy in xyz]
        return Response(json.dumps(data), content_type='application/json')
