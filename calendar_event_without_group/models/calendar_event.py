# -*- coding: utf-8 -*-
# (c) 2016 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, api, exceptions, _


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.multi
    def write(self, vals):
        if len(self.filtered(lambda x: x.create_uid.id != self.env.uid)) > 0:
            raise exceptions.Warning(
                _("You can not change this meeting, because you are not the "
                  "user who created it"))
        return super(CalendarEvent, self).write(vals)