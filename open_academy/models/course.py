from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'open academy Course'

    name = fields.Char(
        string='Course' ,
        required=True
    )

    title = fields.Char(
        string='Title'
    )

    description = fields.Text(
        string='Description'
    )

    usuario = fields.Many2one('open_academy.users', 'Responsable')

    field_one2many = fields.One2many('open_academy.sessions', 'field_many2one', 'campo One2many')
