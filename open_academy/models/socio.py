from odoo import models, fields, api


class Partner(models.Model):
    _name = 'open_academy.partner'
    _description = 'open academy Partner'

    name = fields.Char(
        string='Name' ,
        required=True
    )

    instructor = fields.Char(
        string='Instructor',
        required=True
    )

    sessions = fields.Many2many('open_academy.sessions', 'name')