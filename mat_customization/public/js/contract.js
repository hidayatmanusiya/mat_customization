frappe.ui.form.on('Contract', "onload", function(frm){
	frm.set_query("contact", "contact_table", function() {
        return {
            query: "mat_customization.utils.custom_query",
            filters: {
                "party_name" : frm.doc.party_name
            }
        };
    });
})
