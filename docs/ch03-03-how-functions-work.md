## Funksiyalar

Funksiyalar Rust kodida keng tarqalgan. Siz allaqachon tildagi eng muhim funksiyalardan birini koʻrgansiz: koʻplab dasturlarning kirish nuqtasi boʻlgan `main` funksiya. Siz yangi funksiyalarni eʼlon qilish imkonini beruvchi `fn` kalit soʻzini ham koʻrdingiz.

Rust kodi funksiya va oʻzgaruvchilar nomlari uchun anʼanaviy uslub sifatida *snake case* dan foydalanadi, unda barcha harflar kichik va alohida soʻzlarning tagiga chiziladi.
Mana, misol funksiya taʼrifini oʻz ichiga olgan dastur:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-16-functions/src/main.rs}}
```

Rust-da funksiyani `fn` soʻng funksiya nomi va qavslar toʻplamini kiritish orqali aniqlaymiz. Jingalak qavslar kompilyatorga funksiya tanasi qayerda boshlanishi va tugashini bildiradi.

Biz belgilagan har qanday funksiyani uning nomidan keyin qavslar toʻplamini kiritish orqali chaqirishimiz mumkin. Dasturda `boshqa_funksiya` ni aniqlanganligi sababli uni `main` funksiya ichidan chaqirish mumkin. Eʼtibor bering, biz `boshqa_funksiya` ni manba kodidagi `main` funksiyadan keyin belgilaganmiz; uni avval ham belgilashimiz mumkin edi. Rust sizning funksiyalaringizni qayerda belgilashingizning ahamiyati yoʻq, faqat ular soʻrov yuboruvchi tomonidan koʻrinadigan doirada aniqlangan.

Keling, funksiyalarni koʻproq oʻrganish uchun *funksiyalar* nomli yangi binary loyihani boshlaylik. `boshqa_funksiya` misolini *src/main.rs* ga joylashtiring va uni ishga tushiring.Quyidagi chiqishni koʻrishingiz kerak:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-16-functions/output.txt}}
```

Qatorlar `main` funksiyada paydo boʻladigan tartibda bajariladi.
Avvaliga "Hello, world!" xabar chop etiladi, keyin `boshqa_funksiya` chaqiriladi va uning xabari chop etiladi.

### Parametrlar

Biz funksiyalarni *parametrlari* boʻlishi uchun belgilashimiz mumkin, ular funksiya imzosining bir qismi boʻlgan maxsus oʻzgaruvchilardir. Agar funksiya parametrlarga ega boʻlsa, siz unga ushbu parametrlar uchun aniq qiymatlarni berishingiz mumkin. Texnik jihatdan aniq qiymatlar *argumentlar* deb ataladi, ammo tasodifiy suhbatda odamlar funksiya taʼrifidagi oʻzgaruvchilar yoki funksiyani chaqirganingizda qabul qilingan aniq qiymatlar uchun *parametr* va *argument* soʻzlarini bir-birining oʻrniga ishlatishga moyildirlar.

`boshqa_funksiya` ning ushbu versiyasida biz parametr qoʻshamiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-17-functions-with-parameters/src/main.rs}}
```

Ushbu dasturni ishga tushirishga harakat qiling; quyidagi chiqishni olishingiz kerak:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-17-functions-with-parameters/output.txt}}
```

`boshqa_funksiya` deklaratsiyasi `x` nomli bitta parametrga ega. `x` turi `i32` sifatida belgilangan. Biz `5`ni `boshqa_funksiya`ga o‘tkazganimizda, `println!` makros `5` ni `x`ni o‘z ichiga olgan jingalak qavslar juftligi format satrida joylashgan joyga qo‘yadi.

Funksiya signaturelarda siz har bir parametr turini eʼlon qilishingiz kerak. Bu Rust dizaynidagi ataylab qabul qilingan qaror: funksiya taʼriflarida turdagi izohlarni talab qilish kompilyatorga qaysi turni nazarda tutayotganingizni tushunish uchun ularni kodning boshqa joylarida ishlatishingizga deyarli hech qachon ehtiyoj sezmasligini anglatadi. Kompilyator, shuningdek, funksiya qanday turlarni kutayotganini bilsa, yanada foydali xato xabarlarini berishi mumkin.

Bir nechta parametrlarni belgilashda parametr deklaratsiyasini vergul bilan ajrating, masalan:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-18-functions-with-multiple-parameters/src/main.rs}}
```

Ushbu misol ikkita parametrli `belgilangan_vaqt` nomli funksiyani yaratadi. Birinchi parametr `value` deb nomlangan va `i32` dir. Ikkinchisi `unit_label` deb nomlanadi va `char` turidir. Keyin funksiya `value` va ``unit_label` ni o‘z ichiga olgan matnni chop etadi.

Keling, ushbu kodni ishga tushirishga harakat qilaylik. Hozirda *funksiyalar* loyihangizning *src/main.rs* faylidagi dasturni oldingi misol bilan almashtiring va uni `cargo run` yordamida ishga tushiring:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-18-functions-with-multiple-parameters/output.txt}}
```

Biz funksiyani `value` qiymati sifatida `5` va `unit_label` qiymati sifatida `'hʼ` deb ataganimiz sababli, dastur chiqishi ushbu qiymatlarni o`z ichiga oladi.

### Statementlar va  Expressionlar

Funksiya qismlari ixtiyoriy ravishda statement bilan tugaydigan bir qator expressionlardan iborat. Hozircha biz koʻrib chiqqan funksiyalar yakuniy expressionni oʻz ichiga olmagan, lekin siz expressionni statementning bir qismi sifatida koʻrdingiz. Rust expressionga asoslangan til boʻlganligi sababli, bu tushunish uchun muhim farqdir. Boshqa tillar bir xil farqlarga ega emas, shuning uchun keling, qanday statementlar va expressionlar ekanligini va ularning farqlari funksiyalar tanasiga qanday taʼsir qilishini koʻrib chiqaylik.

* **Statementlar** baʼzi amallarni bajaradigan va qiymat qaytarmaydigan koʻrsatmalardir.
* **Expressionlar** qiymatga baholanadi. Keling, baʼzi misollarni koʻrib chiqaylik.

Biz allaqachon statementlar va expressionlarni ishlatganmiz. Oʻzgaruvchini yaratish va unga `let` kalit soʻzi bilan qiymat berish - bu statement. 3-1 roʻyxatda `let y = 6;` - bu statement.

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/listing-03-01/src/main.rs}}
```

<span class="caption">Roʻyxat 3-1: Bitta statementni oʻz ichiga olgan `main` funksiya deklaratsiyasi</span>

Funksiya definitionlari ham statementlardir; oldingi misol oʻz-oʻzidan bir statementdir.

Statementlar qiymatlarni qaytarmaydi. Shuning uchun siz boshqa oʻzgaruvchiga `let` iborasini tayinlay olmaysiz, chunki quyidagi kod bunga harakat qiladi; siz xatoga duch kelasiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-19-statements-vs-expressions/src/main.rs}}
```

Ushbu dasturni ishga tushirganingizda, sizda paydo boʻladigan xato quyidagicha koʻrinadi:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-19-statements-vs-expressions/output.txt}}
```

`let y = 6` statementi qiymat qaytarmaydi, shuning uchun `x` bogʻlanishi uchun hech narsa yoʻq. Bu boshqa tillarda sodir boʻladigan narsadan farq qiladi, masalan, C va Ruby, bu yerda assignment assignmentning qiymatini qaytaradi. Bu tillarda siz `x = y = 6` yozishingiz mumkin va `x` va `y` ham `6` qiymatiga ega; Rustda bunday emas.

Expressionlar qiymatga baholanadi va siz Rust-da yozadigan kodning qolgan qismini tashkil qiladi. `5 + 6` kabi matematik amalni koʻrib chiqing, bu `11` qiymatini beruvchi expressiondir. Expressionlar statementlarning bir qismi boʻlishi mumkin: 3-1 roʻyxatdagi `let y = 6;` ifodasidagi `6`, `6` qiymatini beruvchi expressiondir. Funksiyani chaqirish expressiondir. Makroni chaqirish expressiondir. Jingalak qavslar bilan yaratilgan yangi qamrov bloki expressiondir, masalan:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-20-blocks-are-expressions/src/main.rs}}
```

Bu expression:

```rust,ignore
{
    let x = 3;
    x + 1
}
```

blok boʻlib, bu holda `4` ga evaluate boʻladi. Bu qiymat `let` statementining bir qismi sifatida `y` ga bogʻlanadi. Eʼtibor bering, "`x + 1` qatorining oxirida nuqta-vergul yoʻq, bu siz koʻrgan koʻpgina qatorlardan farqli oʻlaroq. Expressionlar yakuniy nuqtali vergullarni oʻz ichiga olmaydi. Ifodaning oxiriga nuqtali vergul qoʻshsangiz, uni statementga aylantirasiz va u keyinchalik qiymatni qaytarmaydi. Keyingi funksiyani qaytarish qiymatlari va expressionlarini oʻrganayotganda buni yodda tuting.

### Return qiymatlari bilan funksiyalar

Funksiyalar qiymatlarni ularni chaqiradigan kodga return qaytarishi mumkin. Return qiymatlarini nomlamaymiz, lekin ularning turini oʻqdan keyin eʼlon qilishimiz kerak (`->`). Rustda funksiyaning return qiymati funksiya tanasi blokidagi yakuniy ifodaning qiymati bilan sinonimdir. Siz `return` kalit soʻzidan foydalanib va qiymatni belgilash orqali funksiyadan erta qaytishingiz mumkin, lekin koʻpchilik funksiyalar oxirgi expressionni bevosita qaytaradi. Mana qiymatni return qiladigan funksiyaga misol:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-21-function-return-values/src/main.rs}}
```

`besh` funksiyasida funksiya chaqiruvlari, makroslar va hatto `let` iboralari ham yo‘q – faqat `5` raqamining o‘zi. Bu Rust-da juda toʻgʻri funksiya. Funksiyaning return turi ham `-> i32` sifatida koʻrsatilganligini unutmang.Ushbu kodni ishga tushirishga harakat qiling; chiqish quyidagicha koʻrinishi kerak:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-21-function-return-values/output.txt}}
```

`besh` dagi `5` funksiyaning return qiymatidir, shuning uchun return turi `i32`dir. Keling, buni batafsilroq koʻrib chiqaylik. Ikkita muhim bit mavjud: birinchidan, `let x = besh();` qatori biz oʻzgaruvchini ishga tushirish uchun funksiyaning return qiymatidan foydalanayotganimizni koʻrsatadi. Chunki `besh` funksiyasi `5`ni qaytaradi, bu qator quyidagi bilan bir xil:

```rust
let x = 5;
```

Ikkinchidan, `besh` funksiyasi hech qanday parametrga ega emas va return qiladigan qiymat turini belgilaydi, lekin funksiyaning tanasi nuqta-vergulsiz yolg‘iz `5` bo‘ladi, chunki bu biz qiymatini qaytarmoqchi bo‘lgan ifodadir.

Keling, yana bir misolni koʻrib chiqaylik:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-22-function-parameter-and-return/src/main.rs}}
```

Ushbu kodni ishga tushirish `x qiymati: 6` ni chop etadi. Ammo, agar biz `x + 1` boʻlgan satr oxiriga nuqta-vergul qoʻysak, uni expressiondan statementga oʻzgartirsak, xatoga yoʻl qoʻyamiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-23-statements-dont-return-values/src/main.rs}}
```

Ushbu kodni kompilyatsiya qilish quyidagi kabi xatoga olib keladi:

```console
{{#include ../listings/ch03-common-programming-concepts/no-listing-23-statements-dont-return-values/output.txt}}
```

Asosiy xato xabari, `mismatched types`(mos kelmaydigan turlar) ushbu kod bilan bogʻliq asosiy muammoni ochib beradi. `qoshilgan_bir` funksiyasining taʼrifida aytilishicha, u `i32` ni qaytaradi, lekin statementlar birlik turi boʻlgan `()` bilan expression boʻlgan qiymatga evaluate boʻlmaydi. Shuning uchun, hech narsa return qilinmaydi, bu funksiya definitioniga zid keladi va xatolikka olib keladi. Ushbu chiqishda Rust bu muammoni tuzatishga yordam beradigan xabarni taqdim etadi: u nuqta-vergulni olib tashlashni taklif qiladi, bu xatoni tuzatadi.
