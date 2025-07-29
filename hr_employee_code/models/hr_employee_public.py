from odoo import models, fields


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    code = fields.Char(
        related="employee_id.code",
        readonly=True,
    )
