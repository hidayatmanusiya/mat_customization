import frappe
import pandas as pd
import json

def make_booking_service_item(doc, method):
    if doc.booking_item == 1:
        create_service_item(doc)
        validate_service_item(doc)


def create_service_item(item):
    if not frappe.db.exists("Item", item.item_code + "_service"):
        book_service_setting = frappe.get_cached_doc("Booking Settings")
        service_item = frappe.new_doc("Item")
        service_item.update({
            "item_code": item.item_code + "_service",
            "item_name": item.item_name,
            "item_group": book_service_setting.service_item_group,
            "stock_uom": book_service_setting.uom,
            "is_stock_item": False,
            "is_service_item": True
        })
        service_item.save(ignore_permissions=True)
        item.service_item = service_item.name
    else:
        item.service_item = item.item_code + "_service"
        print("item_name",item.item_name + " (B) ")
        frappe.db.set_value("Item",item.service_item, "item_name",item.item_name + " (B) ")
        frappe.db.set_value("Item",item.service_item, "image",item.image)

def validate_service_item(doc):
    if doc.service_item:
        is_service_item = frappe.db.get_value("Item",doc.service_item,"is_service_item")
        if not is_service_item:
            frappe.throw("Service Item must be checked Is Service Item.")
        is_stock_item = frappe.db.get_value("Item",doc.service_item,"is_stock_item")
        if is_stock_item:
            frappe.throw("Stock Item can't be use as service item.")


def count_working_hours(doc, method):
    items = doc.items
    for item in items:
        if item.holiday_list and item.uom:
            days =  count_days(item)
            count_hours(item, days)



def count_days(item):
    hoiday_list_dates = []
    start_date = item.start_date
    end_date = item.end_date
    holiday_list = item.holiday_list
    holidays = frappe.get_doc("Holiday List", holiday_list)
    for row in holidays.holidays:
        hoiday_list_dates.append(row.holiday_date)
    

    a = pd.date_range(start=start_date, end=end_date)

    days = 0

    for date in a:
        if date in hoiday_list_dates:
            continue
        else :
            days += 1
    return days

def count_hours(item, days):
    hours = frappe.db.get_value("UOM", item.uom, "hours")
    working_hours = days * hours
    item.update({
            "working_hours": working_hours,
        })


@frappe.whitelist()
def calculate_working_hour(item):
    item = json.loads(item)
    days =  _count_days(item)
    return _count_hours(item, days)

def _count_days(item):
    hoiday_list_dates = []
    start_date = item['start_date']
    end_date = item['end_date']
    holiday_list = item['holiday_list']
    holidays = frappe.get_doc("Holiday List", holiday_list)
    for row in holidays.holidays:
        hoiday_list_dates.append(row.holiday_date)
    

    a = pd.date_range(start=start_date, end=end_date)

    days = 0

    for date in a:
        if date in hoiday_list_dates:
            continue
        else :
            days += 1
    return days

def _count_hours(item, days):
    hours = frappe.db.get_value("UOM", item['uom'], "hours")
    working_hours = days * hours
    return working_hours

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def custom_query(doctype, txt, searchfield, start, page_len, filters):
    if filters.get("party_name"):
        return frappe.db.sql("""
            select 
                contact.name
            from 
                `tabContact` as contact, 
                `tabDynamic Link` as contact_child_table
            where 
                contact.name = contact_child_table.parent
                and contact_child_table.link_doctype = 'Customer'
                and contact_child_table.link_name LIKE %(party_name)s
        """,{
                'party_name': filters.get('party_name'),
            }
        )
    else:
        return {}

@frappe.whitelist()
def make_item_price(doc, method):
    for row in doc.item_detail:
        flag = validate_item_price(row, doc.start_date, doc.end_date, doc.party_name)
        if flag == "create":
            create_item_price(row, doc.start_date, doc.end_date, doc.party_name)
        elif flag == "update":
            update_item_price(row, doc.start_date, doc.end_date, doc.party_name)
        else:
            continue
        


def create_item_price(item, start_date, end_date, customer):
    price_list = frappe.get_cached_doc("Selling Settings")
    item_price = frappe.new_doc("Item Price")
    item_price.update({
        "item_code": item.item,
        "item_name": item.item_name,
        "uom": item.uom,
        "price_list_rate": item.price,
        "valid_from": start_date,
        "valid_upto": end_date,
        "price_list": price_list.selling_price_list,
        "customer": customer
    })
    item_price.save(ignore_permissions=True)
        # print(item_price)
        # frappe.msgprint("Created")

def update_item_price(item, start_date, end_date, customer):
    price_list = frappe.get_cached_doc("Selling Settings")
    item_price = frappe.get_doc("Item Price", {
        "item_code": item.item, 
        "valid_from": start_date, 
        "valid_upto": end_date,
        "uom": item.uom,
        "customer": customer
        })
    item_price.update({
        "item_code": item.item,
        "item_name": item.item_name,
        "uom": item.uom,
        "price_list_rate": item.price,
        "valid_from": start_date,
        "valid_upto": end_date,
        "price_list": price_list.selling_price_list,
        "customer": customer
    })
    item_price.save(ignore_permissions=True)
    # print(item_price)
    # frappe.msgprint("Updated")

def validate_item_price(item, start_date, end_date, customer):
    create = False
    if not frappe.db.exists("Item Price", {
        "item_code": item.item, 
        "item_name": item.item_name, 
        "uom": item.uom, 
        "price_list_rate": item.price,
        "valid_from": start_date,
        "valid_upto": end_date,
        "customer": customer
        }):
        create = True
        if create and validate_existing_uom(item, start_date, end_date, customer):
            return "update"
        elif create and not validate_existing_item_price(item, start_date, end_date, customer) and not validate_existing_uom(item, start_date, end_date, customer):
            return "create"


def validate_existing_item_price(item, start_date, end_date, customer):
    update = False
    if frappe.db.exists("Item Price", {
    "item_code": item.item, 
    "item_name": item.item_name,
    "price_list_rate" : item.price,
    "valid_from": start_date, 
    "valid_upto": end_date,
    "customer": customer
    }):
        update = True
    return update

def validate_existing_uom(item, start_date, end_date, customer):
    update = False
    if frappe.db.exists("Item Price", {
    "item_code": item.item, 
    "item_name": item.item_name,
    "uom": item.uom,
    "valid_from": start_date, 
    "valid_upto": end_date,
    "customer": customer
    }):
        update = True
    return update

    
#     return update

# @frappe.whitelist()
# def get_item_name(contract, item):
#     items = {}
#     contract = frappe.get_doc("Contract", contract)
#     print(contract)
#     for row in contract.item_detail:
#         items[row.item] = row.item_name
    
#     if item in items.keys():
#         print(items[item])
#         return items[item]