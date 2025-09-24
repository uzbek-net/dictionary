## Hello, Cargo!

Cargo - bu Rustning build tizimi va paketlar menejeri. Aksariyat Rustaceanlar oʻzlarining Rust loyihalarini boshqarish uchun ushbu vositadan foydalanadilar, chunki Cargo siz uchun kodni yaratish, kodingizga bogʻliq kutubxonalarni yuklab olish va ushbu kutubxonalarni yaratish kabi koʻplab vazifalarni bajaradi.(Biz sizning kodingizga kerak boʻlgan kutubxonalarni chaqiramiz
*dependencies*.)

Eng oddiy Rust dasturlari, biz hozirgacha yozganimiz kabi, hech qanday dependencylarga ega emas. Agar biz  “Hello, world!” Cargo bilan loyiha boʻlsa, u faqat sizning kodingizni yaratish bilan shugʻullanadigan Cargo qismidan foydalanadi. Murakkab Rust dasturlarini yozganingizda, siz dependencylarni qoʻshasiz va agar siz Cargo yordamida loyihani boshlasangiz, dependencylarni qoʻshish osonroq boʻladi.

Rust loyihalarining aksariyati Cargolardan foydalanganligi sababli, ushbu kitobning qolgan qismida siz ham Cargodan foydalanasiz deb taxmin qilinadi. [Oʻrnatish][installation]<!-- ignore -->  boʻlimida muhokama qilingan rasmiy oʻrnatuvchilardan foydalansangiz, Cargo Rust bilan birga keladi. Agar siz Rust-ni boshqa vositalar orqali oʻrnatgan boʻlsangiz, terminalingizga quyidagilarni kiritish orqali Cargo oʻrnatilganligini tekshiring:

```console
$ cargo --version
```

Agar siz versiya raqamini koʻrsangiz, sizda bor! Agar siz `command not found` kabi xatolikni koʻrsangiz, Cargoni qanday qilib alohida oʻrnatish boʻyicha texnik hujjatlarni koʻrib chiqing.

### Cargo bilan loyiha yaratish

Keling, Cargo-dan foydalanib yangi loyiha yarataylik va u bizning asl “Hello, world!” loyihadan qanday farq qilishini koʻrib chiqaylik. Oʻzingizning *projects* jildigiga (yoki kodingizni saqlashga qaror qilgan joyingizga) qayting. Keyin istalgan operatsion tizimda quyidagilarni bajaring:

```console
$ cargo new hello_cargo
$ cd hello_cargo
```

Birinchi buyruq *hello_cargo* nomli yangi jild va loyihani yaratadi.
Biz loyihamizga *hello_cargo* deb nom berdik va Cargo oʻz fayllarini xuddi shu nomdagi jildda yaratadi.

*hello_cargo* jildiga oʻting va fayllar roʻyxatini koʻring.Cargo biz uchun ikkita fayl va bitta jild yaratganini koʻrasiz: *Cargo.toml* fayli va ichida *main.rs* fayli boʻlgan *src* jildi.

Shuningdek, u *.gitignore* fayli bilan birga yangi Git repositoryni ishga tushirdi. Mavjud Git repositoryda `cargo new` ni ishga tushirsangiz, Git fayllari yaratilmaydi; `cargo new - vcs=git` yordamida bu xatti-harakatni bekor qilishingiz mumkin.

> Eslatma: Git keng tarqalgan versiya boshqaruv tizimidir. Siz `--vcs` buyrugʻi yordamida
> `cargo new` ni boshqa versiyani boshqarish tizimidan foydalanishga yoki versiyani boshqarish
> tizimisiz foydalanishga oʻzgartirishingiz mumkin. Mavjud variantlarni
> koʻrish uchun `cargo new --help` ni ishga tushiring.

Siz tanlagan matn muharririda *Cargo.toml*ni oching. U 1-2 roʻyxatdagi kodga oʻxshash boʻlishi kerak.

<span class="filename">Fayl nomi: Cargo.toml</span>

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

<span class="caption">Roʻyxat 1-2: `cargo new` tomonidan yaratilgan *Cargo.toml* tarkibi</span>

Bu fayl [*TOML*][toml]<!-- ignore --> da (*Tom’s Obvious, Minimal
Language*) formati, bu Cargo konfiguratsiya formati.

Birinchi qator, `[package]`, boʻlim sarlavhasi boʻlib, quyidagi iboralar paketni sozlayotganligini bildiradi.Ushbu faylga qoʻshimcha maʼlumot qoʻshsak, biz boshqa boʻlimlarni qoʻshamiz.

Keyingi uchta qatorda Cargo dasturingizni kompilyatsiya qilish uchun kerak boʻlgan konfiguratsiya maʼlumotlarini oʻrnatadi: Rustning nomi, versiyasi va foydalanish uchun nashri.
[E ilovasi][appendix-e]<!-- ignore -->da `edition` kaliti haqida gaplashamiz.

Oxirgi qator, `[dependencies]`, loyihangizning har qanday dependencylarini roʻyxatlash uchun boʻlimning boshlanishi. Rustda kod paketlari *crates* deb ataladi. Ushbu loyiha uchun bizga boshqa cratelar kerak boʻlmaydi, lekin biz 2-bobdagi birinchi loyihada boʻlamiz, shuning uchun biz ushbu dependencies boʻlimidan foydalanamiz.

Endi *src/main.rs* oching va qarang:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo “Hello, world!” siz uchun dastur, xuddi biz Roʻyxat 1-1 da yozganimiz kabi! Hozircha, bizning loyihamiz va yaratilgan Cargo loyihasi oʻrtasidagi farq shundaki, Cargo kodni *src* jildiga joylashtirgan va bizda yuqori jildda *Cargo.toml* konfiguratsiya fayli mavjud.

Cargo sizning manba fayllaringiz *src* jildida turishini kutadi. Yuqori darajadagi loyiha jildi faqat README fayllari, litsenziya maʼlumotlari, konfiguratsiya fayllari va kodingizga aloqador boʻlmagan boshqa narsalar uchun moʻljallangan. Cargo-dan foydalanish loyihalaringizni tartibga solishga yordam beradi. Hamma narsaning oʻrni bor va hamma narsa oʻz oʻrnida.

Agar siz “Hello, world!” bilan qilganimizdek, Cargo-dan foydalanmaydigan loyihani boshlagan boʻlsangiz, uni Cargo-dan foydalanadigan loyihaga aylantirishingiz mumkin. Loyiha kodini *src* jildiga oʻtkazing va tegishli *Cargo.toml* faylini yarating.

### Cargo loyihasini qurish va ishga tushirish

Keling, “Hello, world!” ni qurish va ishga tushirishda nima farq qilishini koʻrib chiqaylik. Cargo bilan dasturni *hello_cargo* jildidan quyidagi buyruqni kiritish orqali loyihangizni build qiling:

```console
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

Ushbu buyruq bajariladigan faylni joriy jildingizda emas, balki *target/debug/hello_cargo* da (yoki Windowsda *target\debug\hello_cargo.exe*)da  yaratadi. Odatiy tuzilish debug tuzilishi boʻlgani uchun Cargo binary faylni *debug* nomli jildga joylashtiradi. Ushbu buyruq bilan bajariladigan faylni ishga tushirishingiz mumkin:

```console
$ ./target/debug/hello_cargo # yoki .\target\debug\hello_cargo.exe Windowsda
Hello, world!
```

Agar hammasi yaxshi boʻlsa, `Hello, world!` terminalga chop etilishi kerak.`cargo build` ni birinchi marta ishga tushirish ham Cargoning yuqori darajadagi yangi faylni yaratishiga olib keladi: *Cargo.lock*. Ushbu fayl loyihangizdagi dependencylarning aniq versiyalarini kuzatib boradi. Ushbu loyihada dependencylar yoʻq, shuning uchun faylda kod biroz kam. Siz hech qachon ushbu faylni qoʻlda oʻzgartirishingiz shart emas; Cargo uning tarkibini siz uchun boshqaradi.

Biz hozirgina `cargo build` orqali loyihasini build qildik va uni `./target/debug/hello_cargo` bilan ishga tushirdik, lekin kodni kompilyatsiya qilish uchun `cargo run` dan ham foydalanishimiz va natijada bajariladigan faylni bitta buyruqda ishga tushirishimiz mumkin:

```console
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

`cargo run` dan foydalanish `cargo build` ni ishga tushirishdan koʻra qulayroqdir va keyin binary yoʻlni toʻliq ishlatadi, shuning uchun koʻpchilik ishlab chiquvchilar `cargo run` dan foydalanadilar.

Eʼtibor bering, bu safar biz `Hello_cargo` ni kompilyatsiya qilayotganini koʻrsatadigan natijani koʻrmadik. Cargo fayllar oʻzgarmaganligini aniqladi, shuning uchun u qayta tiklanmadi, balki binary faylni ishga tushirdi. Agar siz manba kodingizni oʻzgartirgan boʻlsangiz, Cargo loyihani ishga tushirishdan oldin uni qayta build qilgan boʻlar edi va siz ushbu natijani koʻrgan boʻlar edingiz:

```console
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Cargo shuningdek, `cargo check` deb nomlangan buyruqni taqdim etadi. Bu buyruq kompilyatsiya qilish uchun kodingizni tezda tekshiradi, lekin bajariladigan fayl yaratmaydi:

```console
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

Nima uchun bajariladigan faylni xohlamaysiz? Koʻpincha `cargo check` `cargo build`dan koʻra tezroq boʻladi,, chunki u bajariladigan faylni yaratish bosqichini oʻtkazib yuboradi. Agar siz kod yozish paytida ishingizni doimiy ravishda tekshirayotgan boʻlsangiz, `cargo check` dan foydalanish loyihangiz hali ham kompilyatsiya qilinayotganligini bildirish jarayonini tezlashtiradi! Shunday qilib, koʻplab Rustaceanlar vaqti-vaqti bilan `cargo check` ni amalga oshiradilar, chunki ular oʻz dasturlarini kompilyatsiya qilishiga ishonch hosil qilish uchun yozadilar. Keyin ular bajariladigan fayldan foydalanishga tayyor boʻlgach, `cargo build` ni ishga tushiradilar.

Cargo haqida shu paytgacha oʻrganganlarimizni takrorlaymiz:

* Biz `cargo new` yordamida loyiha yaratamiz.
* `cargo build` yordamida loyihani build qilishimiz mumkin.
* Biz `cargo run` yordamida bir bosqichda loyiha build qilishimiz va ishga tushirishimiz mumkin.
* `cargo check` yordamida xatolarni tekshirish uchun binary  ishlab chiqarmasdan loyihani build qilishimiz mumkin.
* Build natijasini bizning kodimiz bilan bir xil jildda saqlash oʻrniga, Cargo uni *target/debug* jildida saqlaydi.

Cargo-dan foydalanishning qoʻshimcha afzalligi shundaki, qaysi operatsion tizimda ishlayotganingizdan qatʼi nazar, buyruqlar bir xil boʻladi. Shunday qilib, biz endi Linux va MacOS uchun Windows-ga nisbatan maxsus koʻrsatmalar bermaymiz.

### Loyihani Reliz qilish

Loyihangiz nihoyat relizga tayyor boʻlgach, uni optimallashtirish bilan kompilyatsiya qilish uchun `cargo build --release` dan foydalanishingiz mumkin. Ushbu buyruq *target/debug* oʻrniga *target/release* da bajariladigan fayl yaratadi. Optimizatsiya Rust kodingizni tezroq ishga tushiradi, lekin bu kompilyatsiya vaqtini uzaytiradi. Shuning uchun ikkita turli profil mavjud: biri tez va tez-tez qayta tiklamoqchi boʻlganingizda ishlab chiqish uchun, ikkinchisi esa oxirgi dasturni yaratish uchun siz foydalanuvchiga qayta tiklanmaydigan va mkon qadar tez ishlaydigan oxirgi dastur. Agar siz kodingizning ishlash vaqtini solishtirmoqchi boʻlsangiz, `cargo build --release` dasturini ishga tushiring va *target/release* da bajariladigan fayl bilan taqqoslang.

### Konventsiya sifatida Cargo

Oddiy loyihalar bilan Cargo `rustc` dan foydalanishdan koʻra unchalik katta foyda keltirmaydi, ammo dasturlaringiz yanada murakkablashgani sayin u oʻz qiymatini isbotlaydi.
Dasturlar bir nechta fayllarga koʻpayib rivojlanganda yoki ularga dependency kerak boʻlsa, Cargo-ga buildni muvofiqlashtirishga ruxsat berish ancha oson boʻladi.

`hello_cargo` loyihasi oddiy boʻlsa ham, u endi Rust karyerangizning qolgan qismida foydalanadigan haqiqiy asboblarning koʻp qismini ishlatadi. Haqiqatan ham, mavjud loyihalar ustida ishlash uchun siz Git yordamida kodni tekshirish, ushbu loyiha jildiga oʻzgartirish va build qilish uchun quyidagi buyruqlardan foydalanishingiz mumkin:

```console
$ git clone github.com/birorta-loyiha
$ cd birorta-loyiha
$ cargo build
```

Cargo haqida koʻproq maʼlumot olish uchun uning [texnik hujjatlarini][cargo] tekshiring.

## Xulosa

Siz allaqachon Rust sayohatingizni ajoyib boshladingiz! Ushbu bobda siz quyidagilarni oʻrgandingiz:

* Rust-ning soʻnggi barqaror versiyasini `rustup` yordamida oʻrnatish
* Rustning yangi versiyasiga yangilash
* Mahalliy oʻrnatilgan texnik hujjatlarni ochish
* “Hello, world!” deb yozing va ishga tushiring. toʻgʻridan-toʻgʻri `rustc` dan foydalangan holda dastur
* Cargo konventsiyalaridan foydalangan holda yangi loyiha yaratish va ishga tushirish

Bu Rust kodini oʻqish va yozishga odatlanish uchun yanada muhimroq dastur yaratish uchun ajoyib vaqt. Shunday qilib, 2-bobda biz taxminiy oʻyin dasturini tuzamiz.
Agar siz Rust-da umumiy dasturlash tushunchalari qanday ishlashini oʻrganishni afzal koʻrsangiz, 3-bobga qarang va keyin 2-bobga qayting.

[installation]: ch01-01-installation.html#installation
[toml]: https://toml.io
[appendix-e]: appendix-05-editions.html
[cargo]: https://doc.rust-lang.org/cargo/
