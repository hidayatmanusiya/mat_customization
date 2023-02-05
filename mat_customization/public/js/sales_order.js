frappe.ui.form.on('Sales Order',{
	customer: function(frm){
		set_filter(frm)
	},
	// change_item_name: function(frm, cdt, cdn){
	// 	set_item_name(frm, cdt, cdn)
	// }
})
frappe.ui.form.on('Sales Order Item', {
	start_date(frm, cdt, cdn) {
		calculate_working_hour(frm, cdt, cdn)
	},
	end_date(frm, cdt, cdn) {
		calculate_working_hour(frm, cdt, cdn)
	},
	holiday_list(frm, cdt, cdn) {
		calculate_working_hour(frm, cdt, cdn)
	},
	uom(frm, cdt, cdn) {
		calculate_working_hour(frm, cdt, cdn)
	},
})

var set_filter = function(frm){
	frm.set_query("contract", function() {
        return {
            "filters": {
                "party_name": frm.doc.customer
            }
        };
    });
}

var calculate_working_hour = function (frm, cdt, cdn) {
	var row = locals[cdt][cdn];
	if (row.start_date && row.end_date && row.holiday_list && row.uom){
		frappe.call({
			method: 'mat_customization.utils.calculate_working_hour',
			type: 'POST',
			args: {
				"item": row
			},
			callback: function (r) {
				if (!r.exc) {
					frappe.model.set_value(cdt, cdn, "working_hours", r.message)
				}
			}
		});
	}
}

// var set_item_name = function(frm){
// 	var row = locals[cdt][cdn];
// 	if (row.item_code){
// 		frappe.call({
// 			method: 'mat_customization.utils.get_item_name',
// 			type: 'GET',
// 			args: {
// 				"item": row.item_code,
// 				"contract": frm.doc.contract
// 			},
// 			callback: function (r) {
// 				if (!r.exc) {
// 					frappe.model.set_value(cdt, cdn, "item_name", r.message)
// 				}
// 			}
// 		});
// 	}
// }