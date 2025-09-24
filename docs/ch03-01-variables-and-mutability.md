## Oʻzgaruvchilar va oʻzgaruvchanlik

[”Oʻzgaruvchilar bilan qiymatlarni saqlash”][storing-values-with-variables]<!-- ignore --> boʻlimida aytib oʻtilganidek, standart boʻyicha oʻzgaruvchilar oʻzgarmasdir.Rust sizga oʻz kodingizni Rust taqdim etgan xavfsizlik va qulay parallellikdan foydalanadigan tarzda yozish uchun beradigan koʻplab qulayliklardan biridir. Biroq, siz hali ham oʻzgaruvchilaringizni oʻzgaruvchan qilish imkoniyatiga egasiz.
Keling, Rust sizni qanday qilib va nima uchun oʻzgarmaslikni afzal koʻrishga undashini va nega baʼzan siz undan voz kechishingiz mumkinligini bilib olaylik.

Agar oʻzgaruvchi oʻzgarmas boʻlsa, qiymat nomga bogʻlangandan keyin siz bu qiymatni oʻzgartira olmaysiz. Buni koʻrsatish uchun `cargo new variables` yordamida *projects* jildingizda *variables* nomli yangi loyihani yarating.

Keyin, yangi *variables* jildida *src/main.rs* ni oching va uning kodini quyidagi kod bilan almashtiring. Bu kod hozircha kompilyatsiya qilinmaydi, biz avval oʻzgarmaslik xatosini koʻrib chiqamiz.

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-01-variables-are-immutable/src/main.rs}}
```

Kodni saqlang va dasturni `cargo run` yordamida ishga tushiring. Ushbu chiqishda koʻrsatilganidek, oʻzgarmaslik xatosi haqida xato xabarini olishingiz kerak:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-01-variables-are-immutable/output.txt}}
```

Ushbu misol kompilyator sizning dasturlaringizdagi xatolarni topishga qanday yordam berishini koʻrsatadi.
Kompilyatordagi xatolar sizni asabiylashtirishi mumkin, lekin aslida ular sizning dasturingiz hali siz xohlagan narsani xavfsiz bajarmayotganligini anglatadi; ular sizning yaxshi dasturchi emasligingizni bildirmaydi! Tajribali Rustaceanlar hali ham kompilyator xatolariga duch kelishadi.

Siz oʻzgarmas `x` oʻzgaruvchisiga ikkinchi qiymatni belgilashga harakat qilganingiz uchun ````x` oʻzgaruvchisiga ikki marta tayinlab boʻlmaydi``` xato xabarini oldingiz.

Oʻzgarmas deb belgilangan qiymatni oʻzgartirishga urinayotganda kompilyatsiya vaqtida xatolarga duch kelishimiz muhim, chunki bu holat xatolarga olib kelishi mumkin.Agar bizning kodimizning bir qismi qiymat hech qachon oʻzgarmasligi haqidagi faraz asosida ishlayotgan boʻlsa va kodimizning boshqa qismi bu qiymatni oʻzgartirsa, kodning birinchi qismi uni bajarish uchun moʻljallangan narsani qilmasligi mumkin. Bunday xatoning sababini aniqlash qiyin boʻlishi mumkin, ayniqsa kodning ikkinchi qismi faqat *baʼzan* qiymatini oʻzgartirganda. Rust kompilyatori qiymat oʻzgarmasligini bildirganingizda, u haqiqatan ham oʻzgarmasligini kafolatlaydi, shuning uchun uni oʻzingiz kuzatib borishingiz shart emas. Shunday qilib, kodingizni tushunish osonroq.

Ammo oʻzgaruvchanlik juda foydali boʻlishi mumkin va kodni yozishni qulayroq qilishi mumkin.
Garchi oʻzgaruvchilar standart boʻyicha oʻzgarmas boʻlsa-da, [2-bobda][storing-values-with-variables]<!-- ignore --> boʻlgani kabi oʻzgaruvchi nomi oldiga `mut` qoʻshish orqali ularni oʻzgaruvchan qilish mumkin. `mut` qoʻshilishi, shuningdek, kodning boshqa qismlari ushbu oʻzgaruvchining qiymatini oʻzgartirishini koʻrsatib, kelajakdagi kod oʻquvchilariga niyatni bildiradi.

Masalan, *src/main.rs* ni quyidagiga oʻzgartiramiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-02-adding-mut/src/main.rs}}
```

Dasturni hozir ishga tushirganimizda, biz quyidagilarni olamiz:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-02-adding-mut/output.txt}}
```

`mut` ishlatilganda `x` ga bog‘langan qiymatni `5` dan `6` ga o‘zgartirishga ruxsat beriladi. Oxir oqibat, oʻzgaruvchanlikni qoʻllash yoki qilmaslikni hal qilish sizga bogʻliq va bu vaziyatda eng aniq deb oʻylagan narsangizga bogʻliq.

### Konstantalar

Oʻzgarmas oʻzgaruvchilar singari, *konstantalar* nomga bogʻlangan va oʻzgarishi mumkin boʻlmagan qiymatlardir, lekin konstantalar va oʻzgaruvchilar oʻrtasida bir nechta farqlar mavjud.

Birinchidan, `mut` dan konstantalar bilan foydalanishga ruxsat berilmagan. Konstantalar standart boʻyicha shunchaki oʻzgarmas emas - ular har doim oʻzgarmasdir.Siz konstantalarni `let` kalit soʻzi oʻrniga `const` kalit soʻzidan foydalanib eʼlon qilasiz va qiymat turiga *annotatsiya qilinishi kerak*. Biz turlar va izohlarni keyingi ["Maʼlumotlar turlari"][data-types]<!-- ignore --> boʻlimida koʻrib chiqamiz, shuning uchun hozir tafsilotlar haqida qaygʻurmang. Bilingki, siz har doim turga annotate qoʻyishingiz kerak.

Konstantalar har qanday miqyosda, shu jumladan global miqyosda eʼlon qilinishi mumkin, bu ularni kodning koʻp qismlari bilishi kerak boʻlgan qiymatlar uchun foydali qiladi.

Oxirgi farq shundaki, konstantalar faqat ish vaqtida hisoblanishi mumkin boʻlgan qiymatning natijasi emas, balki faqat konstanta ifodaga oʻrnatilishi mumkin.

Mana konstanta deklaratsiyaga misol:

```rust
const SONIYADA_UCH_SOAT: u32 = 60 * 60 * 3;
```

Konstanta nomi `SONIYADA_UCH_SOAT` va uning qiymati 60 ni (bir daqiqadagi soniyalar soni) 60 ga (bir soatdagi daqiqalar soni) 3 ga (biz hisoblamoqchi boʻlgan soatlar soni) koʻpaytirish natijasiga oʻrnatiladi. Rustning konstantalar uchun nomlash konventsiyasi soʻzlar orasida barcha bosh harflarni pastki chiziq bilan ishlatishdir. Kompilyator kompilyatsiya vaqtida cheklangan operatsiyalar toʻplamini baholashga qodir, bu bizga ushbu qiymatni 10,800 qiymatiga oʻrnatmasdan, tushunish va tekshirish osonroq boʻlgan tarzda yozishni tanlash imkonini beradi.
Konstantalarni eʼlon qilishda qanday operatsiyalardan foydalanish mumkinligi haqida qoʻshimcha maʼlumot olish
[Rust Referencening konstantalar boʻlimiga qarang][const-eval]

Konstantalar dastur ishlayotgan butun vaqt davomida, ular eʼlon qilingan doirada amal qiladi. Bu xususiyat dasturning bir nechta qismlari bilishi kerak boʻlgan, masalan, oʻyinning har qanday oʻyinchisi olishi mumkin boʻlgan maksimal ball soni yoki yorugʻlik tezligi kabi, ilova domeningizdagi qiymatlar uchun foydali konstantalarni qiladi.

Dasturingiz davomida ishlatiladigan qattiq kodlangan qiymatlarni konstantalar sifatida nomlash ushbu qiymatning maʼnosini kodning kelajakdagi maintainerlariga yetkazishda foydalidir. Bu, shuningdek, kodingizda faqat bitta joyga ega boʻlishga yordam beradi, agar kelajakda qattiq kodlangan qiymat yangilanishi kerak boʻlsa, oʻzgartirishingiz kerak boʻladi.

### Shadowing

[2-bobdagi Taxmin qilish oʻyini][comparing-the-guess-to-the-secret-number]<!-- ignore --> boʻyicha qoʻllanmada koʻrganingizdek, oldingi oʻzgaruvchi bilan bir xil nomli yangi oʻzgaruvchini eʼlon qilishingiz mumkin.Rustaceanlarning aytishicha, birinchi oʻzgaruvchi ikkinchi oʻzgaruvchi tomonidan *shadow qilingan* yaʼni ikkinchi oʻzgaruvchi oʻzgaruvchi nomidan foydalanganda kompilyator koʻradigan narsadir.
Darhaqiqat, ikkinchi oʻzgaruvchi birinchisiga shadow qilib, oʻzgaruvchi nomidan har qanday foydalanishni uning oʻzi shadowli boʻlmaguncha yoki doirasi tugaguncha oladi.
Biz bir xil oʻzgaruvchining nomidan foydalanib, `let` kalit soʻzidan foydalanishni quyidagi tarzda takrorlash orqali oʻzgaruvchini shadow qilishimiz mumkin:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-03-shadowing/src/main.rs}}
```

Bu dastur avval `x` ni `5` qiymatiga bogʻlaydi. Keyin u `let x =` ni takrorlab, asl qiymatni olib, `1` qoʻshish orqali yangi `x` oʻzgaruvchisini yaratadi, shunda `x` qiymati `6` boʻladi. Keyin, jingalak qavslar bilan yaratilgan ichki doirada uchinchi `let` iborasi ham `x` ga shadow qiladi va yangi oʻzgaruvchini yaratadi va oldingi qiymatni `2` ga koʻpaytirib, `x` ga `12` qiymatini beradi.
Bu doira tugagach, ichki shadow tugaydi va `x` `6` ga qaytadi.
Ushbu dasturni ishga tushirganimizda, u quyidagilarni chiqaradi:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-03-shadowing/output.txt}}
```

Shadowing o‘zgaruvchini `mut` deb belgilashdan farq qiladi, chunki `let` kalit so‘zidan foydalanmasdan tasodifan ushbu o‘zgaruvchiga qayta tayinlashga harakat qilsak, kompilyatsiya vaqtida xatolikka yo‘l qo‘yamiz. `let` dan foydalanib, biz qiymat boʻyicha bir nechta oʻzgarishlarni amalga oshirishimiz mumkin, lekin bu oʻzgarishlar tugagandan soʻng oʻzgaruvchi oʻzgarmas boʻlishi mumkin.

`Mut` va shadow oʻrtasidagi boshqa farq shundaki, biz `let` kalit soʻzini qayta ishlatganimizda yangi oʻzgaruvchini samarali yaratayotganimiz sababli, qiymat turini o`zgartirishimiz mumkin, lekin bir xil nomni qayta ishlatishimiz ham mumkin. Misol uchun, bizning dasturimiz foydalanuvchidan boʻsh joy belgilarini kiritish orqali baʼzi matnlar orasida qancha boʻsh joy boʻlishini koʻrsatishni soʻraydi va biz ushbu kiritishni raqam sifatida saqlamoqchimiz:

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-04-shadowing-can-change-types/src/main.rs:here}}
```

Birinchi `joylar` oʻzgaruvchisi satr turi, ikkinchi `joylar` oʻzgaruvchisi esa raqam turi. Shadowing shu tariqa bizni turli nomlar bilan chiqishdan saqlaydi, masalan, `joylar_str` va `joylar_num`; Buning oʻrniga biz oddiyroq `joylar` nomini qayta ishlatishimiz mumkin. Biroq, bu erda koʻrsatilganidek, buning uchun `mut` dan foydalanmoqchi boʻlsak, kompilyatsiya vaqtida xatoga duch kelamiz:

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-05-mut-cant-change-types/src/main.rs:here}}
```

Xato bizga oʻzgaruvchining turini mutatsiyaga oʻtkazishga ruxsat yoʻqligini aytadi:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-05-mut-cant-change-types/output.txt}}
```

Endi biz oʻzgaruvchilar qanday ishlashini oʻrganib chiqdik, keling, ular boʻlishi mumkin boʻlgan koʻproq maʼlumotlar turlarini koʻrib chiqaylik.

[comparing-the-guess-to-the-secret-number]:
ch02-00-guessing-game-tutorial.html#comparing-the-guess-to-the-secret-number
[data-types]: ch03-02-data-types.html#data-types
[storing-values-with-variables]: ch02-00-guessing-game-tutorial.html#storing-values-with-variables
[const-eval]: ../reference/const_eval.html
