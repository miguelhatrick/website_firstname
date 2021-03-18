# Copyright 2021 Miguel Hatrick (Dacosys)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request, route


class FirstnameSignup(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        request.params['name'] = '%s, %s' % (request.params['lastname'] if 'lastname' in request.params else '',
                                             request.params['firstname'] if 'firstname' in request.params else '')

        return super(FirstnameSignup, self).get_auth_signup_qcontext()
