# -*- coding: utf-8 -*-
from odoo import models, fields, api


class district(models.Model):
    _description = 'District'
    _name = 'res.country.district'
    _order = 'code_district_id'

    district_id = fields.Char(string='District Name', help='Administrative divisions of a country, under level Fed. state is district', required=True)
    code_district_id = fields.Integer(string='District Code', required=True, default='01')
    state_ids = fields.Many2one('res.country.state', string="Fed. State", required=True)
    country_ids = fields.Many2one('res.country', string="Country", required=True)


class district_inherit(models.Model):
    _inherit = 'res.country'

    district_ids = fields.One2many('res.country.district', 'district_id', string='District')
    code_district_ids = fields.One2many('res.country.district', 'code_district_id', string='District')