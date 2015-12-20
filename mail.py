# -*- coding: utf-8 -*-
#/#############################################################################
#
#    BizzAppDev
#    Copyright (C) 2004-TODAY bizzappdev(<http://www.bizzappdev.com>).
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
#/#############################################################################

from openerp.osv import osv
import logging
from openerp.tools.config import config
config['publisher_warranty_url'] = ''
_logger = logging.getLogger(__name__)
from openerp.models import AbstractModel


from openerp.tools import config

config['publisher_warranty_url'] = ''

class publisher_warranty_contract(AbstractModel):
    _inherit = "publisher_warranty.contract"

    def _get_message(self, cr, uid):
        return {}
    
    
class publisher_warranty_contract(osv.osv):
    _inherit = 'publisher_warranty.contract'

    def _get_sys_logs(self, cr, uid):
        return 
    def update_notification(self, cr, uid, ids, cron_mode=True,
                            context=None):

        _logger.info("NO More Spying Stuff")

        return True


publisher_warranty_contract()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

