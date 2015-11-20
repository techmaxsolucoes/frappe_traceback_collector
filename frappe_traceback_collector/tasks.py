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

				doc = frappe.new_doc('Traceback')
				loc = data.pop('locals')
				exception = data.pop('exception')
				frames = data.pop('frames')

				doc.update(data)
				doc.update({
					'locals': json.dumps(loc),
					'exception': json.dumps(exception),
					'frames': json.dumps(frames)
				})
				doc.save()

			os.remove(fullpath)
	
	except Exception as e:
		collect(e)