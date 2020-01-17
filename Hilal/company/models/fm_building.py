from odoo import api, models, fields
import math


class FmBuilding(models.Model):
    _name = 'fm.building'
    _description = 'Buildings'
    _rec_name = 'building_name'
    building_id = fields.One2many('employee.building.assignment', 'building_id', string='Building')

    building_name = fields.Char(string="Building Name", required=True)
    building_no = fields.Char(string="Building No", required=True)
    building_dimension = fields.Char(string="Building Dimension")
    construction_year = fields.Integer(string="Construction Year")
    structural_system = fields.Char(string="Structural System")
    office_area_as_mt_square = fields.Float()
    under_root_area_as_meter = fields.Float(string='Meter: ')
    under_root_area_as_feet = fields.Float(string='Feet: ', compute='_mt_to_feet')

    active = fields.Boolean()
    building_ids = fields.One2many('employee.building.assignment', 'building_id', string='Building')

    @api.depends('office_area_as_mt_square')
    @api.one
    def _mt_sqr_to_mt(self):
        self.under_root_area_as_meter = math.sqrt(self.office_area_as_mt_square)

    @api.depends('under_root_area_as_meter')
    def _mt_to_feet(self):
        for record in self:
            record.under_root_area_as_feet = record.under_root_area_as_meter * 3.2808
