
import frappe
from frappe.model.naming import make_autoname
from datetime import datetime

def create_batches_for_items(doc, method):
    if not doc.update_stock:
        frappe.throw("Cannot create batch unless 'Update Stock' is checked.")

    if isinstance(doc.posting_date, str):
        posting_date_obj = datetime.strptime(doc.posting_date, "%Y-%m-%d").date()
    else:
        posting_date_obj = doc.posting_date

    posting_date_str = posting_date_obj.strftime('%Y-%m-%d')

    supplier_code = doc.supplier or frappe.scrub(doc.supplier_name or "unknown")

    for item in doc.items:
        if item.custom_create_batch:
            item_doc = frappe.get_doc("Item", item.item_code)
            if item_doc.has_serial_no:
                frappe.throw(f"Item {item.item_code} requires serial numbers. Cannot auto-create batch.")

            series_base = f"{supplier_code}-{posting_date_str}-"
            raw_batch_id = make_autoname(series_base + ".####")

            batch_id = raw_batch_id.replace(".", "-")

            batch_doc = frappe.new_doc("Batch")
            batch_doc.batch_id = batch_id
            batch_doc.item = item.item_code
            batch_doc.reference_doctype = "Purchase Invoice"
            batch_doc.reference_name = doc.name
            batch_doc.save()

            item.batch_no = batch_id

            frappe.logger().info(f"Created batch {batch_id} for item {item.item_code}")
