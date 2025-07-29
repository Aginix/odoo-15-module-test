from odoo import models, fields


class HrEmployeeCode(models.Model):
    _inherit = "hr.employee"
    _description = "hr.employee"

    code = fields.Char("KMITL Code", copy=False, tracking=True)

    _sql_constraints = [
        (
            "code_unique",
            "unique(code)",
            "Can't be duplicate value for this field! -> 'KMITL Code'",
        )
    ]
