{
    'name': 'Drug BUD',
    'author': "Sofyan Sofi",
    'website': "https://sofy.web.id",
    'summary': 'Drug Beyond Use Date',
    'version': '1.0',
    'application': True,
    'category': 'Productivity',
    'license': 'Other proprietary',
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/sfx_jenis_obat.csv',
        'views/sf_catdrug_views.xml',
        'views/sf_solvent_views.xml',
        'views/sf_drug_views.xml',
        'views/sf_drug_bud_views.xml',
        'views/bud_menus.xml',
    ],

}
