## Izohlar

Barcha dasturchilar oʻz kodlarini tushunishni osonlashtirishga harakat qilishadi, lekin baʼzida qoʻshimcha tushuntirish kerak. Bunday hollarda dasturchilar oʻzlarining manba kodlarida *izohlar* qoldiradilar, ularni kompilyator eʼtiborsiz qoldiradi, ammo manba kodini oʻqiyotgan odamlar uchun foydali boʻlishi mumkin.

Mana oddiy izoh:

```rust
// hello, world
```

Rustda idiomatik izoh uslubi izohni ikki qiyshiq chiziq bilan boshlaydi va izoh satr oxirigacha davom etadi. Bitta satrdan tashqariga chiqadigan izohlar uchun har bir satrga `//` qoʻshishingiz kerak boʻladi, masalan:

```rust
// Shunday qilib, biz bu erda murakkab ish qilyapmiz,
// bizga bir nechta izohlar kerak boʻladi! Vou! Umid qilamanki,
// bu izoh nima boʻlayotganini tushuntiradi.
```

Izohlar, shuningdek, kodni oʻz ichiga olgan qatorlar oxirida joylashtirilishi mumkin:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-24-comments-end-of-line/src/main.rs}}
```

Ammo siz ularni ushbu formatda koʻproq koʻrasiz, izohli kod ustidagi alohida satrda izoh bilan:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-25-comments-above-line/src/main.rs}}
```
Rustda yana bir turdagi izohlar, hujjatlar izohlari mavjud, biz ularni 14-bobning [“Crates.io-ga crateni nashr qilish“][publishing]<!-- ignore --> boʻlimida muhokama qilamiz.

[publishing]: ch14-02-publishing-to-crates-io.html
