# -*- coding: utf-8 -*-
# Copyright (c) 2015, Maxwell Morais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe_traceback_collector.collector import collect

class Stack(Document):
	def onload(self):
		if not self.parent_stack:
			self.seen = True
			frappe.db.set_value("Stack", self.name, "seen", True)

			for relapsed in frappe.db.get_list("Stack", filters=[
				["Stack", "parent_stack", "=", self.name]]):
				frappe.db.set_value("Stack", relapsed["name"], "seen", True)

			frappe.db.commit()
	
	def ontrash(self):
		for relapsed in frappe.db.get_list("Stack", filters=[
				["Stack", "parent_stack", "=", self.name]]):
				frappe.delete_doc("Stack", relapsed["name"])
		frappe.db.commit()

	def validate(self):
		parent = frappe.get_list("Stack", filters=[
			["Stack", "stack_type", "=", self.stack_type],
			["Stack", "friendly_title", "=", self.friendly_title],
			["Stack", "parent_stack", "=", None]
		], fields=["name", "relapsed", "seen"])

		if parent:
			parent = parent[0]
			self.parent_stack = parent["name"]
			frappe.db.set_value("Stack", parent["name"], "relapsed", parent["relapsed"]+1)
			if parent["seen"]:
				frappe.db.set_value("Stack", parent["name"],"seen", False)