

from frappe.model.naming import make_autoname
from erpnext.stock.doctype.item.item import Item
import frappe

def item_naming(doc, method):
    if doc.custom_company != "FAHI TRADING LLP":
        item_group = doc.item_group or "ITEM_GROUP"
        style = doc.custom_style or "STYLE"
        name = doc.item_name or "ITEM"
        material = doc.custom_material_type or "MAT"
        custom_type = doc.custom_type or "TYPE"
        size = doc.custom_size or "SIZE"
        fit = doc.custom_fit or "FIT"
        color = doc.custom_color or "COLOR"

        prefix = f"{item_group}-{style}-{name}-{material}-{custom_type}-{size}-{fit}-{color}-"
        series_number = make_autoname(prefix + ".####")

        doc.name = series_number
        doc.item_name = series_number
    else:
        doc.item_code = doc.item_name

class CustomItem(Item):
    def autoname(self):
        if self.custom_company == "FAHI TRADING LLP":
            self.name = self.item_name
            self.item_code = self.item_name
        else:
            super().autoname()

@frappe.whitelist()
def set_barcode_based_on_series(item_name):
    item = frappe.get_doc("Item", item_name)
    if item.get("custom_company") != "FAHI TRADING LLP":
        barcode_value = item.name

        item.set("barcodes", [])

        item.append("barcodes", {
            "barcode": barcode_value,
        })

        item.save(ignore_permissions=True)
        frappe.db.commit()
