# -*- coding: utf-8 -*-

from odoo import models, fields, api

class comp(models.Model):
    _name='bm.bug'
    _description='bug'
    name = fields.Char('bug簡述', required=True)
    detail = fields.Text(size=150)
    is_closed = fields.Boolean('是否關閉')
    close_reason = fields.Selection([('changed', '已修改'), ('cannot', '無法修改'), ('delay', '延誤')], string='關閉理由')
    user_id = fields.Many2one('res.users', string='負責人')
    follower_id = fields.Many2many('res.partner', string='關注者')