# ebelge/ebelge/patches/add_ebelge_fields.py

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Customer": [
            {
                "fieldname": "ebelge_section_break",
                "label": "E-Belge Bilgileri",
                "fieldtype": "Section Break",
                "insert_after": "tax_id"
            },
            {
                "fieldname": "ebelge_efatura_mukellefi",
                "label": "E-Fatura",
                "fieldtype": "Select",
                "options": "Evet\nHayır",
                "insert_after": "ebelge_section_break"
            },
            {
                "fieldname": "ebelge_efatura_pk",
                "label": "E-Fatura PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_efatura_mukellefi"
            },
            {
                "fieldname": "ebelge_efatura_pk_default",
                "label": "Varsayılan E-Fatura PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_efatura_pk"
            },
            {
                "fieldname": "ebelge_eirsaliye_mukellefi",
                "label": "E-İrsaliye",
                "fieldtype": "Select",
                "options": "Evet\nHayır",
                "insert_after": "ebelge_efatura_pk_default"
            },
            {
                "fieldname": "ebelge_eirsaliye_pk",
                "label": "E-İrsaliye PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_eirsaliye_mukellefi"
            },
            {
                "fieldname": "ebelge_eirsaliye_pk_default",
                "label": "Varsayılan E-İrsaliye PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_eirsaliye_pk"
            },
            {
                "fieldname": "ebelge_vergi_dairesi",
                "label": "Vergi Dairesi",
                "fieldtype": "Data",
                "insert_after": "ebelge_eirsaliye_pk_default"
            }
        ],
        "Supplier": [
            {
                "fieldname": "ebelge_section_break",
                "label": "E-Belge Bilgileri",
                "fieldtype": "Section Break",
                "insert_after": "tax_id"
            },
            {
                "fieldname": "ebelge_efatura_mukellefi",
                "label": "E-Fatura",
                "fieldtype": "Select",
                "options": "Evet\nHayır",
                "insert_after": "ebelge_section_break"
            },
            {
                "fieldname": "ebelge_efatura_pk",
                "label": "E-Fatura PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_efatura_mukellefi"
            },
            {
                "fieldname": "ebelge_efatura_pk_default",
                "label": "Varsayılan E-Fatura PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_efatura_pk"
            },
            {
                "fieldname": "ebelge_eirsaliye_mukellefi",
                "label": "E-İrsaliye",
                "fieldtype": "Select",
                "options": "Evet\nHayır",
                "insert_after": "ebelge_efatura_pk_default"
            },
            {
                "fieldname": "ebelge_eirsaliye_pk",
                "label": "E-İrsaliye PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_eirsaliye_mukellefi"
            },
            {
                "fieldname": "ebelge_eirsaliye_pk_default",
                "label": "Varsayılan E-İrsaliye PK",
                "fieldtype": "Data",
                "insert_after": "ebelge_eirsaliye_pk"
            },
            {
                "fieldname": "ebelge_vergi_dairesi",
                "label": "Vergi Dairesi",
                "fieldtype": "Data",
                "insert_after": "ebelge_eirsaliye_pk_default"
            }
        ]
    }

    create_custom_fields(custom_fields)
