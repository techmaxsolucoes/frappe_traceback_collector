# -*- coding: utf-8 -*-
# Copyright (c) 2015, Maxwell Morais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

class Traceback(Document):
	def validate(self):
		parent = frappe.get_list('Traceback', filters=[
			['Traceback', 'evalue', '=', self.evalue],
			['Traceback', 'parent_traceback', '=', None]], fields=["name", "relapses"])

		if parent:
			parent = parent[0]
			self.update({"parent_traceback": parent['name']})
			frappe.db.set_value('Traceback', parent['name'], 'relapses', parent["relapses"] + 1)
