# Copyright (c) 2022, D-codE and contributors
# For license information, please see license.txt

import frappe

# tesing api 
@frappe.whitelist(allow_guest=True)
def ping_pong(ping):
    if ping == 'ping':
        frappe.response["test"] = "pong"
    else:
        frappe.response["test"] = "please ping"
    