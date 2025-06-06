import frappe
from ebelge.izibiz_client import IzibizClient

@frappe.whitelist()
def sorgula_ebelge_mukellefi(docname):
    try:
        supplier = frappe.get_doc("Supplier", docname)
        vkn = supplier.tax_id

        if not vkn:
            return "Tedarikçi kartında Vergi Numarası (VKN) girilmemiş."

        client = IzibizClient()
        if not client.authenticate():
            return "İzibiz bağlantısı başarısız."

        response = client.request("GET", f"/v1/gib-user/vkn/{vkn}")
        data = response.get("data")

        if not data:
            return f"{vkn} için sonuç bulunamadı."

        # E-Fatura ve E-İrsaliye mükellefiyetlerini güncelle
        supplier.db_set("ebelge_efatura", 1 if data.get("eInvoiceUser") else 0)
        supplier.db_set("ebelge_eirsaliye", 1 if data.get("eDispatchUser") else 0)

        # PK URN listesini al
        urn_list = data.get("pkList", [])
        urn_values = [urn.get("pk") for urn in urn_list if urn.get("pk")]

        # Varsayılan PK: en güncel tarihli
        default_pk = None
        latest_date = None
        for urn in urn_list:
            if urn.get("pk") and urn.get("createDate"):
                date = frappe.utils.get_datetime(urn["createDate"])
                if not latest_date or date > latest_date:
                    latest_date = date
                    default_pk = urn["pk"]

        # Verileri güncelle
        supplier.db_set("ebelge_efatura_pk", default_pk or "")
        supplier.db_set("ebelge_efatura_pk_list", "\n".join(urn_values))

        return f"Mükellefiyet bilgileri güncellendi.\nE-Fatura: {'EVET' if data.get('eInvoiceUser') else 'HAYIR'}\nE-İrsaliye: {'EVET' if data.get('eDispatchUser') else 'HAYIR'}"
    
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Tedarikçi Mükellefiyet Sorgusu Hatası")
        return f"Hata oluştu: {str(e)}"
