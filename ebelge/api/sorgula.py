import frappe
from ebelge.izibiz_client import IzibizClient

@frappe.whitelist()
def mukellefiyet_sorgula(vkn, doctype, docname):
    if not vkn:
        frappe.throw("Vergi Numarası (VKN) alanı boş olamaz.")

    client = IzibizClient()
    if not client.authenticate():
        frappe.throw("İzibiz bağlantısı başarısız.")

    result = client.query_mukellef(vkn)
    if not result:
        frappe.msgprint("Mükellef bulunamadı.")
        return False

    doc = frappe.get_doc(doctype, docname)
    doc.ebelge_efatura = "Evet" if result.get("efatura") else "Hayır"
    doc.ebelge_irsaliye = "Evet" if result.get("eirsaliye") else "Hayır"
    doc.ebelge_efatura_pk = result.get("default_pk") or ""
    doc.ebelge_irsaliye_pk = result.get("default_eirsaliye_pk") or ""
    doc.save()

    return True
