# venv, virtualenv va Poetry — solishtiruv jadvali

| Xususiyat | venv | virtualenv | Poetry |
|---|---|---|---|
| O'rnatish | Python bilan birga keladi (standart kutubxona) | Alohida o'rnatiladi (`pip install virtualenv`) | Alohida o'rnatiladi |
| Tezlik | O'rtacha | venv'dan tezroq | O'rtacha |
| Dependency boshqaruvi | Yo'q, faqat pip bilan qo'lda | Yo'q, faqat pip bilan qo'lda | Ha, avtomatik (pyproject.toml orqali) |
| Lock fayl | Yo'q | Yo'q | Ha (poetry.lock) — versiyalar aniq qotiriladi |
| Eski Python versiyalarini qo'llab-quvvatlash | Faqat Python 3.3+ | Python 2 va 3 | Python 3 |
| Paket nashr qilish (publish) | Yo'q | Yo'q | Ha, o'rnatilgan (`poetry publish`) |
| Ishlatish qulayligi | Oddiy, minimal | Oddiy, venv'ga o'xshash | Boshida murakkabroq, lekin katta loyihalarda qulay |

## Xulosa
Kichik skriptlar uchun `venv` yetarli. Eski Python versiyalar bilan ishlash kerak bo'lsa `virtualenv`. Katta, jamoaviy loyihalarda aniq dependency boshqaruvi va lock fayl kerak bo'lsa — `Poetry` eng yaxshi tanlov.
