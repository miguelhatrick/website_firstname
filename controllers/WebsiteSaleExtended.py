# Copyright 2021 Miguel Hatrick (Dacosys)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleExtended(WebsiteSale):

    _mandatory = ["firstname", "lastname"]
    _mandatoryRemove = ["name"]

    def _get_mandatory_billing_fields(self):
        _fieldArray = super(WebsiteSaleExtended, self)._get_mandatory_billing_fields();
        return self._process_array(_fieldArray)

    def _get_mandatory_shipping_fields(self):
        _fieldArray = super(WebsiteSaleExtended, self)._get_mandatory_shipping_fields();
        return self._process_array(_fieldArray)

    def _process_array(self, _fieldArray):

        # Remove name from the mandatory list
        for _remove in self._mandatoryRemove:
            if _remove in _fieldArray:
                _fieldArray.remove(_remove)

        # Append missing
        for mandatory in self._mandatory:
            if mandatory not in _fieldArray:
                _fieldArray.append(mandatory)

        return _fieldArray
