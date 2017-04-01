# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Acespritech Solutions Pvt Ltd
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api, _
from datetime import datetime


class product_template(models.Model):
    _inherit = "product.template"

    @api.model
    def create(self, vals):
        res = super(product_template, self).create(vals)
        if res:
            if not vals.get('barcode') and self.env['sale.config.settings'].sudo().search([], limit=1, order="id desc").gen_ean13:
                barcode_str = self.env['barcode.nomenclature'].sanitize_ean("%s%s" % (res.id, datetime.now().strftime("%d%m%y%H%M")))
                res.write({'barcode' : barcode_str})
        return res


class product_product(models.Model):
    _inherit = "product.product"

    @api.model
    def create(self, vals):
        res = super(product_product, self).create(vals)
        if res:
            if not vals.get('barcode') and self.env['sale.config.settings'].sudo().search([], limit=1, order="id desc").gen_ean13:
                barcode_str = self.env['barcode.nomenclature'].sanitize_ean("%s%s" % (res.id, datetime.now().strftime("%d%m%y%H%M")))
                res.write({'barcode' : barcode_str})
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: