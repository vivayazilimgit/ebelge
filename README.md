# ebelge

ERPNext için geliştirilen e-Belge modülüdür.  
Bu uygulama; e-Fatura, e-İrsaliye ve e-Arşiv belgeleri ile entegrasyon sağlamayı amaçlar.

## Özellikler

- İzibiz REST API ile doğrudan bağlantı
- Mükellef sorgulama ve PK alma
- XML üretimi ve gönderimi
- ERPNext `Sales Invoice`, `Delivery Note` gibi belgelerle tam uyum

## Geliştirici

Murathan KILIÇ  
[Viva Yazılım](https://www.vivayazilim.com)

## Kurulum

```bash
bench get-app ebelge
bench --site [site-name] install-app ebelge
