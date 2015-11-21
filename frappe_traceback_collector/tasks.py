from __future__ import unicode_literals

import os
import frappe
import json
from frappe.celery_app import celery_task
from .collector import collect

@celery_task()
def collect_tickets():
	try:
		path = frappe.get_site_path('tickets')
		if not os.path.exists(path):
			return

		for fname in os.listdir(path):
			fullpath = os.path.join(path, fname)

			with open(fullpath, 'rb') as fcontent:
				data = json.load(fcontent)

			for field in ['locals', 'exception', 'frames']:
				data[field] = json.dumps(data[field])

			doc = frappe.new_doc('Traceback')
			
			doc.update(data)
			doc.save()

			os.remove(fullpath)
	
	except Exception as e:
		collect(e)