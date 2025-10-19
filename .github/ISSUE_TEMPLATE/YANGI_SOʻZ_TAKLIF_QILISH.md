---
name: ✨ Yangi So'z Taklifi
about: Lugʻatga yangi inglizcha texnik atama va uning rasmiy oʻzbekcha tarjimasini taklif qiling.
title: "[Yangi Atama]: <Inglizcha Atama>"
labels: enhancement, new-term, needs-translation
assignees: ''

---

### Inglizcha atama maʼlumotlari

* **Inglizcha atama:** (Masalan, `idempotence`, `marshalling`)
* **Soʻz turkumi (`part_of_speech`):** (Masalan, `noun`, `verb`, `adjective`)
* **Kontekst:** (Bu atama odatda qayerda qoʻllaniladi? Masalan, "API dizayni," "Maʼlumotlarni seriyalashtirish," "Maʼlumotlar bazasi tranzaktsiyalari.")

---

### Taklif etilayotgan oʻzbekcha tarjima va ta'rif

Taklif etilayotgan tarjima va toʻliq yozuv maʼlumotlarini TOML formatida taqdim eting.

* **Taklif etilayotgan oʻzbekcha tarjima (`uz`):** (Masalan, `oʻzgarmaslik`, `marshalizatsiya`)
* **Taklif etilayotgan taʼrif (`description` - oʻzbekcha):** Atama nimani anglatishining qisqacha oʻzbekcha tushuntirishi.
* **Taklif etilayotgan talaffuz (`pronunciation_uz`):** (Oʻzbekcha atama qanday talaffuz qilinishi kerak? Masalan, `mar-sha-li-za-tsi-ya`)
* **Oʻxshash atamalar (`similar`):** (Bunga oʻxshash yoki bogʻliq inglizcha atamalarni sanab oʻting, masalan, `["concurrency", "mutability"]`)

### Taklif etilayotgan TOML yozuvi

Iltimos, dastlabki yozuvni yaratish uchun quyidagi maydonlarni toʻldiring:

```toml
[[translations]]
en = "<Inglizcha atama>"
uz = "<Taklif etilayotgan oʻzbekcha tarjima>"
part_of_speech = "<So'z turkumi>"
description = "<Taklif etilayotgan taʼrif>"
pronunciation_uz = "<Taklif etilayotgan talaffuz>"
similar = ["<Oʻxshash atama 1>", ""] # Oʻxshash atamalarni qoʻshing
status = "Pending review" # Har doim 'Pending review' (Koʻrib chiqish kutilmoqda) sifatida boshlang