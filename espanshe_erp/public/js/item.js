frappe.ui.form.on('Item', {
    after_save: function(frm) {
        if (frm.doc.custom_company && frm.doc.custom_company !== "FAHI TRADING LLP") {
            frappe.call({
                method: "espanshe_erp.espanshe_erp.custom_script.item.set_barcode_based_on_series",
                args: {
                    item_name: frm.doc.name,
                    naming_series: frm.doc.naming_series
                },
                callback: function(r) {
                    if (!r.exc) {
                        frm.reload_doc();
                    }
                }
            });
        }
    }
});

