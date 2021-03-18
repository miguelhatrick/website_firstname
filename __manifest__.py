# Copyright 2021 Miguel Hatrick (Dacosys)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Website forms first name and last name",
    "summary": """
            Extends partner_firstname to the Address/Order/Login form and details form so you can enter first name and last name
    """,
    "version": "12.0.1.0.1",
    "author": "Miguel Hatrick",
    "license": "AGPL-3",
    "maintainer": "Dacosys",
    "category": "Extra Tools",
    "website": "https://www.dacosys.com",
    "depends": [
        "website_sale",
        "partner_firstname",
    ],
    "data": [
        'views/portal/auth_signup.xml',
        'views/portal/portal_details.xml',
        'views/portal/portal_address_details.xml'
    ],
    "installable": True,
}
