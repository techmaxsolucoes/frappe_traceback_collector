 
from __future__ import unicode_literals

import frappe

def get_notification_config():
	return {
		"for_doctype": {
			"Traceback": {"seen": 0, "parent_traceback": None},
			"Stack": {"seen": 0, "parent_stack": 0}
		}
	}