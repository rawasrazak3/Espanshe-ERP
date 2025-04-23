
from frappe.model.naming import make_autoname
import frappe

def item_naming(doc, method):
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
