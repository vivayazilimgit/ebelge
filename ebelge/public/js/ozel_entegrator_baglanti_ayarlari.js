frappe.ui.form.on('Ozel Entegrator Baglanti Ayarlari', {
    refresh: function(frm) {
        console.log(">> [DEBUG] Refresh eventi tetiklendi");
        
        frm.add_custom_button(__('Bağlantıyı Test Et'), function() {
            console.log(">> [DEBUG] Bağlantıyı Test Et butonuna tıklandı");
            frm.trigger("test_connection");
        });
    },

    test_connection: function(frm) {
        console.log(">> [DEBUG] test_connection fonksiyonu çağrıldı");

        frappe.call({
            method: "ebelge.api.test.test_custom_connection",
            args: {
                user_code: frm.doc.user_code,
                password: frm.doc.password,
                vkn: frm.doc.vkn,
                gb: frm.doc.gb,
                pk: frm.doc.pk,
                environment: frm.doc.environment,
                test_url: frm.doc.api_test_url || "",
                live_url: frm.doc.api_live_url || ""
            },
            callback: function(r) {
                console.log(">> [DEBUG] Sunucudan yanıt alındı:", r);

                if (!r.message) {
                    frappe.msgprint({
                        title: "Sunucu Hatası",
                        message: "Sunucudan yanıt alınamadı.",
                        indicator: "red"
                    });
                    return;
                }

                if (r.message.status === "success") {
                    frappe.msgprint({
                        title: "Bağlantı Başarılı",
                        message: r.message.message,
                        indicator: "green"
                    });
                } else {
                    frappe.msgprint({
                        title: "Bağlantı Başarısız",
                        message: r.message.message,
                        indicator: "red"
                    });
                }
            }
        });
    }
});
