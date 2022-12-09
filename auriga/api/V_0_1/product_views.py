# Copyright (c) 2022, D-codE and contributors
# For license information, please see license.txt
# 418abbefb15d68e
# 37d29fd6c37279d


import frappe

from bezzie.api.V_0_1.product_query import get_product_filter_data
# from erpnext.e_commerce.api import get_product_filter_data
from erpnext.e_commerce.shopping_cart.product_info import get_product_info_for_website
from erpnext.e_commerce.doctype.item_review.item_review import add_item_review, get_item_reviews, get_customer
from erpnext.e_commerce.variant_selector.utils import get_attributes_and_values, get_next_attribute_and_values
# from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow

# tesing api 
@frappe.whitelist(allow_guest=True)
def ping_pong(ping):
    if ping == 'ping':
        frappe.response["test"] = "pong"
    else:
        frappe.response["test"] = "please ping"

# list product with group search and using other filterss
@frappe.whitelist(allow_guest=True)
def get_product_listing(search,field_filters,attribute_filters,item_group,start,from_filters,page_length):

	query_args={
		"search":search,
		"field_filters":field_filters ,
		"attribute_filters": attribute_filters,
		"item_group": item_group,
		"start": start,
		"from_filters": from_filters,
		"page_length":page_length
	     }
	result = get_product_filter_data(query_args)
	# return result
	frappe.response["items"] = result.get("items")
	frappe.response["sub_categories"] = result.get("sub_categories")
	frappe.response["start"] = start
	frappe.response["page_length"] = page_length
	frappe.response["items_count"] = result.get("items_count")

# Product listing based on filters
@frappe.whitelist(allow_guest=True)
def product_listing(**kwargs):

	kwargs = frappe._dict(kwargs)

	search = "",
	field_filters = {},
	attribute_filters = {},
	item_group = None,
	start = 0,
	from_filters = False,
	page_length = 1

	# if kwargs.search:
	# 	search = kwargs.search

	# if kwargs.field_filters:
	# 	field_filters = kwargs.field_filters

	# if kwargs.attribute_filters:
	# 	attribute_filters = kwargs.attribute_filters
		
	# if kwargs.item_group:
	# 	item_group = kwargs.item_group

	# if kwargs.start:
	# 	start = kwargs.start

	# if kwargs.from_filters:
	# 	from_filters = kwargs.from_filters

	# if kwargs.page_length:
	# 	page_length = kwargs.page_length

	return frappe._dict( {
		"search":search,
		"field_filters":field_filters ,
		"attribute_filters": attribute_filters,
		"item_group": item_group,
		"start": start,
		"from_filters": from_filters,
		"page_length":page_length
	})

	return get_product_filter_data(query_args)


# view product
@frappe.whitelist(allow_guest=True)
def get_product_info(item_code):
    return get_product_info_for_website(item_code)

@frappe.whitelist(allow_guest=True)
def get_product_review(web_item):
    return get_item_reviews(web_item) 


@frappe.whitelist()
def add_product_review(web_item,title,rating,comment):
    return add_item_review(web_item,title,rating,comment)

@frappe.whitelist(allow_guest=True)
def get_attributes_and_value(item_code):
    return get_attributes_and_values(item_code)


@frappe.whitelist(allow_guest=True)
def get_next_attribute_and_value(item_code,selected_attributes):
    return get_next_attribute_and_values(item_code,selected_attributes)



@frappe.whitelist(allow_guest=True)
def get_slideshow(slideshow):
	if not slideshow:
		return {}

	slideshow = frappe.get_doc("Website Slideshow", slideshow)
	slides = slideshow.get({"doctype": "Website Slideshow Item"})
	values={}
	for index, slide in enumerate(slides):
		values[f"slide_{index + 1}_image"] = slide.image
		values[f"slide_{index + 1}_title"] = slide.heading
	return {
		"slides":values,
		"slideshow_header": slideshow.header or "",
	}

@frappe.whitelist(allow_guest=True)
def get_item_code_from_web_item(web_item):
	if frappe.db.get_value("Website Item", web_item, "item_code"):
		return frappe.db.get_value("Website Item", web_item, "item_code")