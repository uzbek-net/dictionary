# Lokalizatsiya lugʻati

Bu loyiha dasturiy taʼminotni ishlab chiqish sohasidagi eng koʻp qoʻllaniladigan texnik atamalarning inglizchadan oʻzbekchaga tarjimalarini jamlashga bagʻishlangan ochiq manbali resursdir.

Maqsadimiz — barcha oʻzbekcha IT-loyihalarida izchil va aniq atamalardan foydalanishni taʼminlash.

## Loyiha haqida

Bizning asosiy maʼlumotlar omborimiz — bu barcha tarjimalar, ularning maʼnolari va kontekstlarini oʻz ichiga olgan yagona TOML faylidir. Ushbu fayl oʻzbek tilidagi texnik hujjatlar, interfeyslar va taʼlim materiallarining sifatini oshirishga yordam beradi.

## Maʼlumotlar tuzilmasi (TOML)

Lugʻat TOML fayli ichida yoziladi va har bir tarjima oʻzining alohida jadvalini ([[translations]]) tashkil etadi. Har bir yozuv quyidagi majburiy maydonlarni oʻz ichiga oladi:

| Maydon | Turi | Tavsifi | Misol |
| --- | --- | --- | --- |
| `en` | String | Inglizcha atama (Kalit so'z) |`"concurrency"` |
| `uz` | String | Oʻzbekcha tarjimasi | `"parallel ishlash"` |
| `part_of_speech` | String | "Soʻz turkumi (noun, verb, adjective) | `"noun"` |
| `description` | String | Oʻzbek tilida qisqa taʼrif | `"Bir nechta vazifalarni bir vaqtda boshqarish."` |
| `pronunciation_uz` | String | Oʻzbekcha tarjimaning talaffuzi | `"pars"` |
| `similar` | Array[String] | Oʻxshash inglizcha atamalar roʻyxati | `["mutability"]` |
| `status` | String | Tarjimaning holati | `"Pending review"` |

**Yozuv misoli**

```toml
[[translations]]
en = "parse"
uz = "pars"
part_of_speech = "verb"
description = "Maʼlumotlar satrini strukturaviy elementlarga ajratish."
pronunciation_uz = "pars"
similar = ["tokenize"]
status = "Pending review"
```

## Hissa qo‘shish

Sizning yordamingiz biz uchun juda muhim! Hissa qoʻshishdan oldin quyidagi uchta maxsus Issue (Muammo) shablonidan birini tanlang. Bu, barcha oʻzgarishlar tartibli va toʻliq hujjatlashtirilishini taʼminlaydi.


**Hissa qoʻshish jarayoni**

1. Yangi Atama Taklifi
  
   - Agar lug'atda mavjud bo'lmagan yangi texnik atamani qo'shmoqchi bo'lsangiz **Yangi So'z Taklifi** shablonidan foydalaning.

2. Notoʻgʻri tarjimani haqida xabar qilish

    - Agar mavjud tarjima noto'g'ri, noaniq yoki yaxshilashni talab qilsa **Xato Tarjima Xisoboti** shablonidan foydalaning.

3. Tizim Xatolarini Yoki Yaxshilashni Taklif Qilish

    - Agar TOML faylining tuzilishida, loyiha jarayonida yoki vositalarida (tooling) xato (bug) boʻlsa yoki yaxshilashni taklif qilmoqchi boʻlsangiz **Yangi Funksiya Talabi** shablonidan foydalaning.


**Pull Request (PR) Yuborish**

Tasdiqlangan takliflar yoki tuzatishlarni amalga oshirgandan soʻng, oʻzgarishlaringizni birlashtirish (merge) uchun Pull Request (PR) yuboring.

- PR yuborishda ham shablon toʻldiriladi. Iltimos, barcha bandlarni diqqat bilan tekshiring va havolalarini bogʻlang.

Biz sizning hissangizni kutib qolamiz!

## Aloqa va muhokama

Tarjimalar va texnik atamalarni muhokama qilish koʻpincha tezkor yondashuvni talab qiladi. Shuning uchun, biz barcha qiziquvchilarni va hissa qoʻshuvchilarni rasmiy Oʻzbek Mahalliylashtirish Telegram hamjamiyatimizga taklif qilamiz.

Bu yerda siz:

- Tarjima variantlari bo'yicha tezkor fikr olishingiz.
- Yangi takliflar (proposals) yoki PRʼlar boʻyicha muhokama qilishingiz.
- Loyihaning jamoatchilikdagi eng soʻnggi yangiliklaridan xabardor boʻlishingiz mumkin.

**Guruh Chatiga Qo'shilish**

Oʻzbek Mahalliylashtirish Telegram hamjamiyatiga qoʻshish havolasi:

- https://t.me/uzbekl10n

**Eslatma:** Rasmiy oʻzgarishlar (yangi soʻz qoʻshish, xatolarni tuzatish) har doim GitHub Issues va Pull Requests orqali amalga oshirilishi shart. Chat faqat norasmiy aloqa uchundir.
