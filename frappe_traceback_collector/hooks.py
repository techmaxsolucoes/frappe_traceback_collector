# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "frappe_traceback_collector"
app_title = "Frappe Traceback Collector"
app_publisher = "Maxwell Morais"
app_description = "A Collector and Formatter for Tracebacks in Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "max.morais.dmm@gmail.com"
app_version = "0.0.1"



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_traceback_collector/css/frappe_traceback_collector.css"
app_include_js = "/assets/frappe_traceback_collector/js/frappe_traceback_collector.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_traceback_collector/css/frappe_traceback_collector.css"
# web_include_js = "/assets/frappe_traceback_collector/js/frappe_traceback_collector.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_traceback_collector.install.before_install"
# after_install = "frappe_traceback_collector.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

notification_config = "frappe_traceback_collector.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"frappe_traceback_collector.tasks.collect_tickets"
	]
}

# scheduler_events = {
# 	"all": [
# 		"frappe_traceback_collector.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_traceback_collector.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_traceback_collector.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_traceback_collector.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_traceback_collector.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_traceback_collector.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_traceback_collector.event.get_events"
# }

from .collector import install_collector
install_collector()