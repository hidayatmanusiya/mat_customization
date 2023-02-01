frappe.ui.form.on('Sales Invoice', "onload", function(frm){
	frm.set_query("contract", function() {
        return {
            "filters": {
                "party_name": frm.doc.customer
            }
        };
    });
})