from odoo import models, fields, api


class Users(models.Model):
    _name = 'open_academy.users'
    _description = 'open academy Users'

    name = fields.Char(
        string='Name' ,
        required=True
    )