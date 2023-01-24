import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def update_custom_fields():
    custom_fields = {
        "Item": [
            dict(fieldname='booking_item',
                 label='Booking Item',
                 fieldtype='Check',
                 insert_after='disabled',
                 print_hide=1),
            dict(fieldname='service_item',
                 label='Service Item',
                 fieldtype='Link',
                 insert_after='booking_item',
                 options='Item',
                 depends_on='eval:doc.booking_item',
                 read_only=0, print_hide=1),
            dict(fieldname='is_service_item',
                 label='Is Service Item',
                 fieldtype='Check',
                 insert_after='service_item',
                 options='Item',
                 depends_on='eval:!doc.booking_item',
                 read_only=0, print_hide=1)
        ],
        "Sales Order Item": [
            dict(fieldname='xyz',
                 fieldtype='Section Break',
                 insert_after='item_name',
                 print_hide=1),
            dict(fieldname='start_date',
                 label='Start Date',
                 fieldtype='Date',
                 insert_after='xyz',
                 read_only=0, print_hide=1),
            dict(fieldname='location',
                 label='Location',
                 fieldtype='Data',
                 insert_after='start_date',
                 read_only=0, print_hide=1),
            dict(fieldname='latitude_longitude',
                 label='Latitude-Longitude',
                 fieldtype='Data',
                 insert_after='location',
                 read_only=0, print_hide=1),
            dict(fieldname='holiday_list',
                 label='Link With Holiday List',
                 fieldtype='Link',
                 options='Holiday List',
                 insert_after='latitude_longitude',
                 read_only=0, print_hide=1),
            dict(fieldname='clm_brk',
                 fieldtype='Column Break',
                 insert_after='holiday_list',
                 print_hide=1, collapsible=1),
            dict(fieldname='end_date',
                 label='End Date',
                 fieldtype='Date',
                 insert_after='clm_brk',
                 read_only=0, print_hide=1),
            dict(fieldname='project_custom',
                 label='Project',
                 fieldtype='Data',
                 insert_after='end_date',
                 read_only=0, print_hide=1),
            dict(fieldname='google_link',
                 label='Google Map Link',
                 fieldtype='Data',
                 insert_after='project_custom',
                 read_only=0, print_hide=1),
             dict(fieldname='working_hours',
                 label='Working Hours',
                 fieldtype='Int',
                 insert_after='google_link',
                 read_only=0, print_hide=1),
        ],
        "Sales Invoice Item": [
            dict(fieldname='xyz',
                 fieldtype='Section Break',
                 insert_after='item_name',
                 print_hide=1),
            dict(fieldname='start_date',
                 label='Start Date',
                 fieldtype='Date',
                 insert_after='xyz',
                 read_only=0, print_hide=1),
            dict(fieldname='location',
                 label='Location',
                 fieldtype='Data',
                 insert_after='start_date',
                 read_only=0, print_hide=1),
            dict(fieldname='latitude_longitude',
                 label='Latitude-Longitude',
                 fieldtype='Data',
                 insert_after='location',
                 read_only=0, print_hide=1),
            dict(fieldname='holiday_list',
                 label='Link With Holiday List',
                 fieldtype='Link',
                 options='Holiday List',
                 insert_after='latitude_longitude',
                 read_only=0, print_hide=1),
            dict(fieldname='clm_brk',
                 fieldtype='Column Break',
                 insert_after='holiday_list',
                 print_hide=1, collapsible=1),
            dict(fieldname='end_date',
                 label='End Date',
                 fieldtype='Date',
                 insert_after='clm_brk',
                 read_only=0, print_hide=1),
            dict(fieldname='project_custom',
                 label='Project',
                 fieldtype='Data',
                 insert_after='end_date',
                 read_only=0, print_hide=1),
            dict(fieldname='google_link',
                 label='Google Map Link',
                 fieldtype='Data',
                 insert_after='project_custom',
                 read_only=0, print_hide=1),
             dict(fieldname='working_hours',
                 label='Working Hours',
                 fieldtype='Int',
                 insert_after='google_link',
                 read_only=0, print_hide=1),
        ],
        "UOM": [
            dict(fieldname='clm_brk',
                 fieldtype='Column Break',
                 insert_after='must_be_whole_number',
                 print_hide=1, collapsible=1),
            dict(fieldname='hours',
                 label='Hours',
                 fieldtype='Int',
                 insert_after='clm_brk',
                 print_hide=1),
        ]
    }

    create_custom_fields(custom_fields)
    frappe.msgprint("Custom Field Updated!")
