import requests
import frappe

@frappe.whitelist()
def test_custom_connection(user_code, password, vkn, gb, pk, environment, test_url=None, live_url=None):
    try:
        base_url = test_url.strip() if environment == "Test" else live_url.strip()

        if not base_url:
            return {
                "status": "error",
                "message": "Seçilen ortama ait API URL girilmemiş."
            }

        # /v1/auth/token varsa birleştirme
        login_url = base_url if "/auth/token" in base_url else f"{base_url.rstrip('/')}/v1/auth/token"

        payload = {
            "username": user_code.strip(),
            "password": password.strip()
        }

        print(f"[DEBUG] API URL: {login_url}")
        print(f"[DEBUG] Payload: {payload}")

        response = requests.post(login_url, json=payload, verify=False)
        response.raise_for_status()
        data = response.json()

        token = data.get("data", {}).get("accessToken")

        if token:
            return {
                "status": "success",
                "message": "Bağlantı başarılı, token alındı.",
                "token": token
            }
        else:
            return {
                "status": "error",
                "message": "Token alınamadı. Yanıt geçersiz.",
                "raw": data
            }

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"Bağlantı hatası: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Genel hata: {str(e)}"
        }
