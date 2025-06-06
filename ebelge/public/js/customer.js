frappe.ui.form.on("Customer", {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button("Mükellefiyet Sorgula", function () {
                if (!frm.doc.tax_id) {
                    frappe.msgprint("Vergi numarası (VKN) girilmemiş.");
                    return;
                }

                frappe.call({
                    method: "ebelge.api.sorgula.mukellefiyet_sorgula",
                    args: {
                        vkn: frm.doc.tax_id,
                        doctype: frm.doctype,
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message === true) {
                            frappe.msgprint("Mükellefiyet bilgileri başarıyla alındı.");
                            frm.reload_doc();
                        } else {
                            frappe.msgprint("Mükellef bulunamadı.");
                        }
                    }
                });
            }, __("E-Belge İşlemleri"));
        }
    }
});
