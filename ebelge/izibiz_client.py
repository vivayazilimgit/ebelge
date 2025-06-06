# ebelge/izibiz_client.py

import requests
import frappe
import time

class IzibizClient:
    TOKEN_EXPIRY_MARGIN = 60  # saniye, token süresinden önce yenile

    def __init__(self):
        settings = frappe.get_single("EBelge Ayarlari")
        self.is_test = settings.is_test_mode
        self.username = (settings.integrator_user or "").strip()
        self.password = (settings.integrator_pass or "").strip()
        self.company_name = getattr(settings, 'company', None)
        self.vkn = getattr(settings, 'vkn', None)

        # Eğer VKN formda yoksa şirket kartından çek
        if not self.vkn and self.company_name:
            self.vkn = frappe.db.get_value("Company", self.company_name, "tax_id")

        self.base_url = "https://apitest.izibiz.com.tr" if self.is_test else "https://api.izibiz.com.tr"
        self.token = None
        self.token_expiry = 0

    def authenticate(self):
        url = f"{self.base_url}/v1/auth/token"
        payload = {
            "username": self.username,
            "password": self.password
        }

        try:
            response = requests.post(url, json=payload, verify=False)
            response.raise_for_status()
            data = response.json()
            self.token = data.get("data", {}).get("accessToken")
            self.token_expiry = time.time() + 3600 - self.TOKEN_EXPIRY_MARGIN
            return True
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "İzibiz Token Alınamadı")
            return False

    def get_token(self):
        if self.token is None or time.time() >= self.token_expiry:
            if not self.authenticate():
                raise Exception("İZİBİZ API token alınamadı.")
        return self.token

    def request(self, method, endpoint, payload=None, params=None):
        token = self.get_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(method, url, json=payload, params=params, headers=headers, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            frappe.log_error(f"[HTTP ERROR] {response.text}", "İzibiz API")
            raise
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "İzibiz API Genel Hata")
            raise
