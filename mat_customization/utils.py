import frappe
import pandas as pd


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
            days =  count_days(doc, item)
            count_hours(item, days)

def count_days(doc, item):
    start_date = item.start_date
    end_date = item.end_date
    holiday_list = item.holiday_list
    hoiday_list_dates = frappe.db.get_all("Holiday", fields=["holiday_date"], pluck= 'holiday_date')

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