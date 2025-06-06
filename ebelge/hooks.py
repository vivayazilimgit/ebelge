from __future__ import unicode_literals

app_name = "ebelge"
app_title = "E-Belge Yönetimi"
app_publisher = "Viva Yazılım"
app_description = "Elektronik belge yönetim sistemi"
app_icon = "octicon octicon-file-text"
app_color = "#2ecc71"
app_email = "murathan@vivayazilim.com"
app_license = "MIT"

# UI Gömülü CSS (eğer özel stiller varsa)
app_include_css = "/assets/ebelge/css/custom.css"

# Belge türlerine özel JS dosyaları
doctype_js = {
    "Customer": "public/js/customer.js",
    "Supplier": "public/js/supplier.js",
    "Ozel Entegrator Baglanti Ayarlari": "public/js/ozel_entegrator_baglanti_ayarlari.js"
}

# Sadece ebelge modülüyle ilgili olan fixture verilerini al
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["module", "=", "ebelge"]]
    },
    {
        "doctype": "Property Setter",
        "filters": [["module", "=", "ebelge"]]
    },
    {
        "doctype": "Client Script",
        "filters": [["module", "=", "ebelge"]]
    },
    {
        "doctype": "DocType",
        "filters": [["name", "in", ["Ozel Entegrator Baglanti Ayarlari"]]]
    },
    {
        "doctype": "Workspace",
        "filters": [["module", "=", "ebelge"]]
    }
]
