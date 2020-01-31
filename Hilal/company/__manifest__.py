{'name': 'Company Application',
 'description': 'Company',
 'author': 'Hilal Kaya',
 'depends': ['base', 'hr'],
 'data': [

     'security/security.xml',
     'security/ir.model.access.csv',
     'views/company.xml',
     'views/company_view.xml',

 ],
 'application': True,
 'installable': True,
 }