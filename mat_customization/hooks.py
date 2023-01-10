from . import __version__ as app_version

app_name = "mat_customization"
app_title = "Mat Customization"
app_publisher = "Jigar Tarpara"
app_description = "Mat Related Customization"
app_email = "jigartarpara@khatavahi.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mat_customization/css/mat_customization.css"
# app_include_js = "/assets/mat_customization/js/mat_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/mat_customization/css/mat_customization.css"
# web_include_js = "/assets/mat_customization/js/mat_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mat_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "mat_customization.utils.jinja_methods",
#	"filters": "mat_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mat_customization.install.before_install"
# after_install = "mat_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mat_customization.uninstall.before_uninstall"
# after_uninstall = "mat_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mat_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"on_update": "mat_customization.utils.make_booking_service_item"
	}
}

after_migrate = "mat_customization.custom_field.create_custom_fields"

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"mat_customization.tasks.all"
#	],
#	"daily": [
#		"mat_customization.tasks.daily"
#	],
#	"hourly": [
#		"mat_customization.tasks.hourly"
#	],
#	"weekly": [
#		"mat_customization.tasks.weekly"
#	],
#	"monthly": [
#		"mat_customization.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "mat_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "mat_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "mat_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"mat_customization.auth.validate"
# ]
