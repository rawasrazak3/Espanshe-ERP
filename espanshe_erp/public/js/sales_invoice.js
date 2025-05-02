frappe.ui.form.on('Sales Invoice Item', {
    batch_no: function(frm, cdt, cdn) {
        update_in_out_rate(frm, cdt, cdn);
    },
    item_code: function(frm, cdt, cdn) {
        update_in_out_rate(frm, cdt, cdn);
    }
});

function update_in_out_rate(frm, cdt, cdn) {
    let item = locals[cdt][cdn];

    if (!item.item_code) {
        return;
    }

    let filters = {
        item_code: item.item_code
    };

    if (item.batch_no) {
        filters.batch_no = item.batch_no;
    }

    frappe.db.get_list('Stock Ledger Entry', {
        filters: filters,
        fields: ['stock_value_difference', 'actual_qty', 'posting_date', 'posting_time'],
        order_by: 'posting_date desc, posting_time desc',
        limit: 1
    }).then(res => {
        if (res && res.length > 0) {
            let sle = res[0];
            let in_out_rate = 0;

            if (flt(sle.actual_qty) !== 0) {
                in_out_rate = flt(sle.stock_value_difference) / flt(sle.actual_qty);
            }

            frappe.model.set_value(cdt, cdn, 'custom_valuation_rate', in_out_rate);
        } else {
            frappe.model.set_value(cdt, cdn, 'custom_valuation_rate', 0);
        }
    });
}
