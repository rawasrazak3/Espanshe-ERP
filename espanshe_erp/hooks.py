app_name = "espanshe_erp"
app_title = "Espanshe ERP"
app_publisher = "Aysha kv"
app_description = "Espanshe ERP"
app_email = "ayshakv07@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/espanshe_erp/css/espanshe_erp.css"
# app_include_js = "/assets/espanshe_erp/js/espanshe_erp.js"

# include js, css files in header of web template
# web_include_css = "/assets/espanshe_erp/css/espanshe_erp.css"
# web_include_js = "/assets/espanshe_erp/js/espanshe_erp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "espanshe_erp/public/scss/website"

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "espanshe_erp.utils.jinja_methods",
# 	"filters": "espanshe_erp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "espanshe_erp.install.before_install"
# after_install = "espanshe_erp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "espanshe_erp.uninstall.before_uninstall"
# after_uninstall = "espanshe_erp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "espanshe_erp.utils.before_app_install"
# after_app_install = "espanshe_erp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "espanshe_erp.utils.before_app_uninstall"
# after_app_uninstall = "espanshe_erp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "espanshe_erp.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"espanshe_erp.tasks.all"
# 	],
# 	"daily": [
# 		"espanshe_erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"espanshe_erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"espanshe_erp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"espanshe_erp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "espanshe_erp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "espanshe_erp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "espanshe_erp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["espanshe_erp.utils.before_request"]
# after_request = ["espanshe_erp.utils.after_request"]

# Job Events
# ----------
# before_job = ["espanshe_erp.utils.before_job"]
# after_job = ["espanshe_erp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"espanshe_erp.auth.validate"
# ]





fixtures = [
    {
        "doctype": "Custom Field", 
        "filters": [
            [
                "name",
                "in",
                [
                    "Item-custom_company",
                    "Item-custom_col_brk",
                    "Item-custom_sec_brk",
                    "Item-custom_color",
                    "Item-custom_material_type",
                    "Item-custom_style",
                    "Item-custom_size",
                    "Item-custom_fit",
                    "Item-custom_type",
                    "Sales Invoice Item-custom_valuation_rate",
                    "Purchase Invoice Item-custom_create_batch",
                    "Purchase Order Item-custom_attach_image",
                    "Purchase Receipt Item-custom_attach_image",
                    "Purchase Invoice Item-custom_attach_image",
                    "Sales Invoice Item-custom_valuation_rate",
                    "Purchase Invoice Item-custom_create_batch",
                    "Supplier-custom_company",
                    "Item-custom_demo_field"
                    
                ]
            ]                         
        ]
    },
    {
    "doctype": "Property Setter",
    "filters":[
        [
            "name",
            "in",
            [
                "Purchase Receipt Item-description-in_list_view",
                "Purchase Receipt-item_name-in_list_view",
                "Purchase Order Item-description-in_list_view",
                "Purchase Order Item-item_name-in_list_view",
                "Purchase Invoice Item-item_name-in_list_view",
                "Purchase Invoice Item-item_name-in_list_view",
                "Sales Order Item-description-in_list_view",
                "Sales Order Item-item_name-in_list_view",
                "Delivery Note Item-item_name-in_list_view",
                "Delivery Note Item-description-in_list_view",
                "Sales Invoice Item-description-in_list_view",
                "Sales Invoice Item-item_name-in_list_view",
                

            ]
        ]
    ]
    },
    
]


doc_events = {
    "Item": {
        "before_insert": "espanshe_erp.espanshe_erp.custom_script.item.item_naming"
    },
     "Purchase Invoice": {
        "before_submit": "espanshe_erp.espanshe_erp.custom_script.purchase_invoice.create_batches_for_items",
    },

}



