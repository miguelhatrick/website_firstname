# Copyright 2021 Miguel Hatrick (Dacosys)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import math
import re

from werkzeug import urls

from odoo import fields as odoo_fields, tools, _
from odoo.exceptions import ValidationError, AccessError, MissingError, UserError
from odoo.http import content_disposition, Controller, request, route
from odoo.tools import consteq
from odoo.addons.portal.controllers.portal import CustomerPortal


class FirstnamePortal(CustomerPortal):

    MANDATORY_BILLING_FIELDS = []

    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):

        self.MANDATORY_BILLING_FIELDS = super(FirstnamePortal, self).MANDATORY_BILLING_FIELDS

        # Remove name from the mandatory list
        if "name" in self.MANDATORY_BILLING_FIELDS:
            self.MANDATORY_BILLING_FIELDS.remove("name")

        # TODO: Fix this
        for mandatory in ["firstname", "lastname"]:
            if mandatory not in self.MANDATORY_BILLING_FIELDS:
                self.MANDATORY_BILLING_FIELDS.append(mandatory)

        return super(FirstnamePortal, self).account(redirect=None, **post)



