from odoo import models, fields, api


class Session(models.Model):
    _name = 'open_academy.sessions'
    _description = 'open academy Session'

    name = fields.Char(
        string='Session' ,
        required=True
    )

    fecha_inicio = fields.Char(
        string='fecha_inicio'
    )

    duracion = fields.Text(
        string='Duracion'
    )

    capacidad = fields.Text(
        string='Capacidad'
    )

    instructor = fields.Many2many('open_academy.partner', 'name',)

    field_many2one = fields.Many2one('open_academy.course', 'Campo Many2one')
