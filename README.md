## Frappe Traceback Collector

A Collector and Formatter for Tracebacks in Frappe

## Motivation

Get detailed tracebacks is much more important than get a simple traceback, while you are trying to debug a async routine, while the traceback collector, you can inspect much more info and inspect the variables values in a context

![alt Traceback](https://raw.githubusercontent.com/mxmo-co/frappe_traceback_collector/master/docs/images/traceback_report.png)

## How to use?

Usually `frappe_traceback_collector` will collect all tracebacks raised in the web context, whithout touch the error handling, thanks to `sys.excepthook`

Async tasks run in a different context, so for collect tracebacks in async context you need import the collector, and run your function inside a `try` statement, see the example 

```python
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
		
```

This code is present [here](https://github.com/mxmo-co/frappe_traceback_collector/blob/master/frappe_traceback_collector/tasks.py), and is used by this app to move the file from the disk to the db.


#### License

MIT
