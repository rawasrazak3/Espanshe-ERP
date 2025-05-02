
from erpnext.stock.doctype.batch.batch import Batch as ERPNextBatch
from frappe.model.naming import make_autoname
import frappe
from frappe.utils import formatdate

class CustomBatch(ERPNextBatch):
    def autoname(self):
        if self.batch_id:
            self.name = self.batch_id
            return

        supplier_code = "SUP"
        posting_date_str = "YYYYMMDD"

        if self.reference_doctype and self.reference_name:
            doc = frappe.get_doc(self.reference_doctype, self.reference_name)

            if self.reference_doctype == "Purchase Invoice" and getattr(doc, "supplier", None):
                supplier_code = doc.supplier

            elif self.reference_doctype == "Stock Entry" and getattr(doc, "custom_supplier", None):
                supplier_code = doc.custom_supplier


            if getattr(doc, "posting_date", None):
                posting_date_str = formatdate(doc.posting_date, "-yyyy-MM-dd-")

        prefix = f"{supplier_code}.{posting_date_str}."
        self.batch_id = make_autoname(prefix + "####")
        self.name = self.batch_id
