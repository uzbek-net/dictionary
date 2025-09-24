# Taxmin qilish oʻyinini dasturlash

Keling, birgalikda amaliy loyiha orqali Rustga oʻtaylik! Ushbu bob sizni bir nechta umumiy Rust tushunchalari bilan tanishtirib, ulardan haqiqiy dasturda qanday foydalanishni koʻrsatib beradi.  Siz `let`, `match`, metodlari, bogʻlangan funksiyalar, external cratelardan foydalanish va boshqalar haqida bilib olasiz! Keyingi boblarda biz ushbu fikrlarni batafsilroq koʻrib chiqamiz. Ushbu bobda siz faqat asoslarni mashq qilasiz.

Biz klassik boshlangʻich dasturlash muammosini amalga oshiramiz: taxmin qilish oʻyini. Bu qanday ishlaydi: dastur 1 dan 100 gacha tasodifiy butun son hosil qiladi. Keyin u oʻyinchini taxmin qilishni taklif qiladi.Tahmin kiritilgandan soʻng, dastur taxmin kichik yoki katta ekanligini koʻrsatadi. Agar taxmin toʻgʻri boʻlsa, oʻyin tabrik xabarini chop etadi va chiqadi.

## Yangi loyiha yaratish

Yangi loyihani oʻrnatish uchun 1-bobda yaratgan *projects* jildiga oʻting va Cargo-dan foydalanib yangi loyiha yarating, masalan:

```console
$ cargo new taxminiy_raqam
$ cd taxminiy_raqam
```

Birinchi `cargo new` buyrugʻi birinchi argument sifatida loyiha nomini (`taxminiy_raqam`)ni oladi. Ikkinchi buyruq yangi loyiha jildiga kiradi.

Yaratilgan *Cargo.toml* fayliga qarang:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial
rm -rf no-listing-01-cargo-new
cargo new no-listing-01-cargo-new --name guessing_game
cd no-listing-01-cargo-new
cargo run > output.txt 2>&1
cd ../../..
-->

<span class="filename">Fayl nomi: Cargo.toml</span>

```toml
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/Cargo.toml}}
```

1-bobda koʻrganingizdek, `cargo new` siz uchun “Hello, world!” soʻzini chop etadigan dastur yaratadi. *src/main.rs* faylini tekshiring:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/src/main.rs}}
```

Keling, ushbu "Hello, world!" dasturni yarating va `cargo run` buyrugʻi yordamida ishga tushiring :

```console
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/output.txt}}
```

`run` buyrug‘i loyihani tezda takrorlash kerak bo‘lganda foydali bo‘ladi, biz bu o‘yinda qilganimizdek, keyingisiga o‘tishdan oldin har bir iteratsiyani tezda sinab ko‘ramiz.

*src/main.rs* faylini qayta oching. Siz ushbu fayldagi barcha kodlarni yozasiz.

## Taxmin qilish oʻyiniga ishlov berish

Taxmin qilish oʻyini dasturining birinchi qismi foydalanuvchi kiritishini soʻraydi, ushbu kiritishni qayta ishlaydi va kirish kutilgan shaklda ekanligini tekshiradi. Boshlash uchun biz oʻyinchiga taxmin kiritishga ruxsat beramiz. 2-1 roʻyxatdagi kodni *src/main.rs* ichiga kiriting.

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:all}}
```

<span class="caption">Roʻyxat 2-1: Foydalanuvchi tomonidan taxmin qilinadigan va uni chop etadigan kod</span>

Ushbu kod juda koʻp maʼlumotlarni oʻz ichiga oladi, shuning uchun uni satrga oʻtkazamiz. Foydalanuvchi kiritishini olish va natijani chiqish sifatida chop etish uchun biz `io` input/output kutubxonasini qamrab olishimiz kerak. `io` kutubxonasi `std` deb nomlanuvchi standart kutubxonadan keladi:

```rust,ignore
use std::io;
```

Odatda, Rust standart kutubxonada belgilangan elementlar toʻplamiga ega boʻlib, u har bir dastur doirasiga kiradi. Ushbu toʻplam *prelude* deb ataladi va siz undagi hamma narsani [standart kutubxona texnik hujjatlarida][prelude] koʻrishingiz mumkin.

Agar siz foydalanmoqchi boʻlgan tur preludeda boʻlmasa, siz ushbu turni `use` iborasi bilan aniq kiritishingiz kerak. `std::io` kutubxonasidan foydalanish sizga bir qator foydali xususiyatlarni, jumladan, foydalanuvchi kiritishini qabul qilish imkoniyatini beradi.

1-bobda koʻrganingizdek, `main` funksiya dasturga kirish nuqtasidir:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:main}}
```

`fn` sintaksisi yangi funktsiyani eʼlon qiladi; Qavslar, `()`, hech qanday parametr yoʻqligini bildiradi; va jingalak qavs, `{`, funksiyaning asosiy qismini boshlaydi.

1-bobda ham bilib olganingizdek, `println!` bu ekranga satrni chop etuvchi makros:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:print}}
```

Ushbu kod oʻyin nima ekanligini koʻrsatuvchi va foydalanuvchidan maʼlumot soʻrashni chop etadi.

### Oʻzgaruvchilar bilan qiymatlarni saqlash

Keyinchalik, foydalanuvchi maʼlumotlarini saqlash uchun *oʻzgaruvchi* yaratamiz, masalan:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:string}}
```

Endi dastur qiziqarli boʻlib bormoqda! Bu kichik satrda juda koʻp narsa bor. Oʻzgaruvchini yaratish uchun `let` iborasidan foydalanamiz. Mana yana bir misol:

```rust,ignore
let olmalar = 5;
```

Bu qator `olmalar` nomli yangi o‘zgaruvchini yaratadi va uni 5 qiymatiga bog‘laydi. Rustda oʻzgaruvchilar standard boʻyicha oʻzgarmasdir, yaʼni oʻzgaruvchiga qiymat berganimizdan keyin qiymat oʻzgarmaydi.Biz ushbu kontseptsiyani 3-bobdagi [”Oʻzgaruvchilar va Oʻzgaruvchanlik”][variables-and-mutability]<!-- ignore --> boʻlimida batafsil muhokama qilamiz. Oʻzgaruvchini oʻzgaruvchan qilish uchun oʻzgaruvchi nomidan oldin `mut` qoʻshamiz:

```rust,ignore
let olmalar = 5; // oʻzgarmas
let mut bananlar = 5; // oʻzgaruvchan
```

> Eslatma: `//` sintaksisi satr oxirigacha davom etadigan izohni
> boshlaydi. Rust izohlarda hamma narsani eʼtiborsiz qoldiradi.
> Izohlarni [3-bobda][comments]<!-- ignore --> batafsilroq muhokama qilamiz.

Taxmin qilish oʻyin dasturiga qaytsak, endi bilasizki, `let mut taxmin` `taxmin` nomli oʻzgaruvchan oʻzgaruvchini kiritadi. Teng belgisi (`=`) Rustga biz hozir biror narsani oʻzgaruvchiga bogʻlamoqchi ekanligimizni bildiradi. Tenglik belgisining oʻng tomonida `taxmin` bogʻlangan qiymat joylashgan boʻlib, u `String::new` funksiyasini chaqirish natijasidir, bu `String`ning yangi nusxasini qaytaradi.
[String][string]<!-- ignore --> standart kutubxona tomonidan taqdim etilgan string turi boʻlib, u rivojlantirib boriladigan, UTF-8 kodlangan matn bitidir.

`::new` qatoridagi `::` sintaksisi `new` `String` tipidagi bogʻlangan funksiya ekanligini bildiradi. *Assosiatsiyalangan funksiya* bu funksiya
turida amalga oshiriladi, bu holda `String`. Ushbu `new` funksiya yangi, boʻsh qatorni yaratadi. Siz koʻp turdagi `new` funksiyani topasiz, chunki u qandaydir yangi qiymatni yaratadigan funksiyaning umumiy nomi.

Toʻliq `let mut taxmin = String::new();` qatori hozirda `String` ning yangi, boʻsh nusxasiga bogʻlangan oʻzgaruvchan oʻzgaruvchini yaratadi.

### Foydalanuvchi maʼlumotlarini qabul qilish

Eslatib oʻtamiz, biz dasturning birinchi qatoriga `use std::io;` bilan standart kutubxonadan input/output funksiyasini kiritgan edik. Endi biz `io` modulidan `stdin` funksiyasini chaqiramiz, bu bizga foydalanuvchi kiritishini boshqarish imkonini beradi:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:read}}
```

Agar biz dasturning boshida `use std::io;` bilan `io` kutubxonasini import qilmagan boʻlsak, biz ushbu funktsiya chaqiruvini `std::io::stdin` sifatida yozish orqali funksiyadan foydalanishimiz xam mumkin. `stdin` funksiyasi [`std::io::Stdin`][iostdin]<!-- ignore --> misolini qaytaradi, bu sizning terminalingiz uchun standart kirish uchun asosni ifodalovchi tur.

Keyinchalik, `.read_line(&mut taxmin)` qatori foydalanuvchidan maʼlumot olish uchun standart kiritish nuqtasidagi [`read_line`][read_line]<!--ignore --> metodini chaqiradi.
Shuningdek, foydalanuvchi kiritgan maʼlumotlarni qaysi qatorda saqlash kerakligini aytish uchun `read_line` ga argument sifatida `&mut taxmin` ni oʻtkazamiz. `read_line` ning toʻliq vazifasi foydalanuvchi nima yozganidan qatʼiy nazar standart kiritishga olish va uni satrga qoʻshishdir (uning mazmunini qayta yozmasdan), shuning uchun biz bu qatorni argument sifatida beramiz. String argumenti oʻzgaruvchan boʻlishi kerak, shuning uchun metod string tarkibini oʻzgartirishi mumkin.

`&` bu argument reference(havola) ekanligini bildiradi, bu sizga kodingizning bir nechta qismlariga ushbu maʼlumotni xotiraga bir necha marta nusxalash kerak boʻlmasdan bitta maʼlumotga kirish imkonini beradi. Referencelar murakkab xususiyat boʻlib, Rustning asosiy afzalliklaridan biri havolalardan foydalanish qanchalik xavfsiz va oson ekanligidir. Ushbu dasturni tugatish uchun koʻp bilimlrga ega boʻlishingiz shart emas. Hozircha siz bilishingiz kerak boʻlgan narsa shundaki, oʻzgaruvchilar singari, havolalar ham standard boʻyicha oʻzgarmasdir. Demak, uni oʻzgaruvchan qilish uchun `&taxmin` oʻrniga `&mut taxmin` yozish kerak. (4-bobda havolalar koʻproq va yaxshiroq tushuntiriladi)

<!-- Old heading. Do not remove or links may break. -->
<a id="handling-potential-failure-with-the-result-type"></a>

### Potensial nosozlikni `Result` turi bilan hal qilish

Biz hali ham ushbu kod qatori ustida ishlayapmiz. Biz hozir matnning uchinchi qatorini muhokama qilmoqdamiz, lekin u hali ham bitta mantiqiy kod qatorining bir qismi ekanligini unutmang. Keyingi qism bu metod:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:expect}}
```

Biz ushbu kodni quyidagicha yozishimiz mumkin edi:

```rust,ignore
io::stdin().read_line(&mut taxmin).expect("Satrni o‘qib bo‘lmadi");
```

Biroq, bitta uzun qatorni oʻqish qiyin, shuning uchun uni boʻlish yaxshidir. `.method_name()` sintaksisi bilan metodni chaqirganda uzun qatorlarni ajratishga yordam berish uchun yangi qator va boshqa boʻshliqlarni kiritish koʻpincha oqilona. Endi bu kod nima qilishini muhokama qilaylik.

Yuqorida aytib oʻtilganidek, `read_line` foydalanuvchi kiritgan narsani biz unga oʻtkazadigan qatorga qoʻyadi, lekin u `Result` qiymatini ham qaytaradi. [`Result`][result]<!-- ignore --> - koʻpincha *enum* deb ataladigan [*enumeration*][enums]<!-- ignore -->, bu bir nechta mumkin boʻlgan holatlardan birida boʻlishi mumkin boʻlgan tur. Har bir mumkin boʻlgan holatni *variant* deb ataymiz.

[6-bobda][enums]<!-- ignore --> enumlar batafsilroq yoritiladi. Ushbu `Result` turlarining maqsadi xatolarni qayta ishlash maʼlumotlarini kodlashdir.

`Result` variantlari `Ok` va `Err`. `Ok` varianti operatsiya muvaffaqiyatli boʻlganligini bildiradi va `Ok` ichida muvaffaqiyatli yaratilgan qiymat.
`Err` varianti operatsiya bajarilmaganligini bildiradi va `Err` operatsiya qanday yoki nima uchun bajarilmagani haqida maʼlumotni oʻz ichiga oladi.

`Result` turidagi qiymatlar, har qanday turdagi qiymatlar kabi, ularda aniqlangan metodlarga ega. `Result` misolida siz murojat qilishingiz mumkin boʻlgan [`expect` metodi][expect]<!-- ignore --> mavjud. Agar `Result` ning ushbu namunasi `Err` qiymati boʻlsa, `expect` dasturning ishlamay qolishiga olib keladi va `expect` ga argument sifatida siz uzatgan xabarni koʻrsatadi. Agar `read_line` metodi `Err`ni qaytarsa, bu asosiy operatsion tizimdan kelgan xato natijasi boʻlishi mumkin.

Agar `Result`ning ushbu namunasi `Ok` qiymati bo‘lsa, `expect` `Ok` ushlab turgan qaytarish qiymatini oladi va siz undan foydalanishingiz uchun aynan shu qiymatni sizga qaytaradi.
Bunday holda, bu qiymat foydalanuvchi kiritishidagi baytlar soni.

Agar siz `expect` ga murojat qilmasangiz, dastur kompilyatsiya qilinadi, lekin siz ogohlantirish olasiz:

```console
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-02-without-expect/output.txt}}
```

Rust `read_line` dan qaytarilgan `Result` qiymatini ishlatmaganligingiz haqida ogohlantiradi, bu dastur mumkin boʻlgan xatoni hal qilmaganligini koʻrsatadi.

Ogohlantirishni yoʻqotishning toʻgʻri yoʻli aslida xatolarni qayta ishlash kodini yozishdir, ammo bizning holatlarimizda muammo yuzaga kelganda biz ushbu dasturni ishdan chiqarishni xohlaymiz, shuning uchun biz `expect` dan foydalanishimiz mumkin. Xatolarni tiklash haqida [9-bobda]recover]<!-- ignore --> bilib olasiz.

### Qiymatlarni `println!`  bilan chop etish

Yopuvchi jingalak qavsdan tashqari, kodda hozirgacha muhokama qilinadigan yana bitta satr mavjud:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:print_guess}}
```

Ushbu satr foydalanuvchi kiritishini oʻz ichiga olgan qatorni chop etadi. `{}` jingalak qavslar toʻplami oʻrnini egallaydi: `{}` qiymatini joyida ushlab turadigan qisqichbaqa qisqichlari deb tasavvur qiling. Oʻzgaruvchining qiymatini chop etishda oʻzgaruvchi nomi jingalak qavslar ichiga kirishi mumkin. Ifodani baholash natijasini chop etishda format satriga boʻsh jingalak qavslarni joylashtiring, soʻngra har bir boʻsh jingalak qavs oʻrnini egallagan holda bir xil tartibda chop etish uchun vergul bilan ajratilgan iboralar roʻyxati bilan format qatoriga amal qiling. O‘zgaruvchini va ifoda natijasini `println!` ga bitta chaqiruvda chop etish quyidagicha ko‘rinadi:

```rust
let x = 5;
let y = 10;

println!("x = {x} va y + 2 = {}", y + 2);
```

Bu kod `x = 5 va y + 2 = 12` ni chop etadi.

### Birinchi qismni sinovdan oʻtkazish

Keling, taxmin qilish oʻyinining birinchi qismini sinab koʻraylik. Uni `cargo run` yordamida ishga tushiring:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-01/
cargo clean
cargo run
input 6 -->

```console
$ cargo run
   Compiling taxminiy_raqam v0.1.0 (file:///projects/taxminiy_raqam)
    Finished dev [unoptimized + debuginfo] target(s) in 6.44s
     Running `target/debug/taxminiy_raqam`
Raqamni topish oʻyini!
Iltimos, taxminingizni kiriting.
6
Sizni taxminingiz: 6
```

Shu nuqtada, oʻyinning birinchi qismi tugadi: biz klaviaturadan maʼlumotlarni olamiz va keyin uni chop etamiz.

## Yashirin raqam yaratish

Keyinchalik, foydalanuvchi taxmin qilishga harakat qiladigan maxfiy raqamni yaratishimiz kerak. Yashirin raqam har safar boshqacha boʻlishi kerak, shuning uchun oʻyinni bir necha marta oʻynash qiziqarli boʻladi. Oʻyin juda qiyin boʻlmasligi uchun biz 1 dan 100 gacha boʻlgan tasodifiy raqamdan foydalanamiz. Rust hali oʻzining standart kutubxonasida tasodifiy raqamlar funksiyasini oʻz ichiga olmaydi. Biroq, Rust jamoasi ushbu funksiyaga [`rand` crate][randcrate]i taqdim etadi.

### Koʻproq funksionallikka ega boʻlish uchun Cratedan foydalanish

Esda tutingki, crate Rust manba kodi fayllari toʻplamidir. Biz qurayotgan loyiha *binary crate* boʻlib, u bajariladigan. `rand` crate boshqa dasturlarda foydalanish uchun moʻljallangan va mustaqil ravishda bajarib boʻlmaydigan kodni oʻz ichiga olgan *library crate*.

Cargoning tashqi cratelarni muvofiqlashtirishi bu erda Cargp haqiqatan ham ishlaydi. `rand` dan foydalanadigan kodni yozishdan oldin, biz *Cargo.toml* faylini `rand` cratesini dependency sifatida qo‘shish uchun o‘zgartirishimiz kerak. Hozir o‘sha faylni oching va Cargo siz uchun yaratgan`[dependencies]` bo‘limi sarlavhasi ostiga quyidagi qatorni qo‘shing.`rand` ni aynan bizda boʻlganidek, ushbu versiya raqami bilan belgilaganingizga ishonch hosil qiling, aks holda ushbu qoʻllanmadagi kod misollari ishlamasligi mumkin:

<!-- When updating the version of `rand` used, also update the version of
`rand` used in these files so they all match:
* ch07-04-bringing-paths-into-scope-with-the-use-keyword.md
* ch14-03-cargo-workspaces.md
-->

<span class="filename">Fayl nomi: Cargo.toml</span>

```toml
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-02/Cargo.toml:8:}}
```

*Cargo.toml* faylida sarlavhadan keyingi hamma narsa boshqa boʻlim boshlanmaguncha davom etadigan boʻlimning bir qismidir. `[dependencies]` da siz Cargo loyihangiz qaysi tashqi cratelarga bogʻliqligini va bu cratelarning qaysi versiyalari kerakligini aytasiz. Bunday holda, biz `rand` crateni `0.8.5` semantik versiya spetsifikatsiyasi bilan belgilaymiz. Cargo versiya raqamlarini yozish uchun standart boʻlgan [Semantic Versioning][semver]<!-- ignore -->ni (baʼzan *SemVer* deb ataladi) tushunadi. `0.8.5` spetsifikatsiyasi aslida `^0.8.5` ning qisqartmasi boʻlib, kamida 0.8.5, lekin 0.9.0 dan past boʻlgan har qanday versiyani bildiradi.

Cargo ushbu versiyalarni 0.8.5 versiyasiga mos keladigan umumiy API-larga ega deb hisoblaydi va bu spetsifikatsiya sizga ushbu bobdagi kod bilan tuziladigan so‘nggi patch versiyasini olishingizni kafolatlaydi. 0.9.0 yoki undan kattaroq versiyalar quyidagi misollar ishlatadigan API bilan bir xil boʻlishi kafolatlanmaydi.

Endi, hech qanday kodni oʻzgartirmasdan, 2-2 roʻyxatda koʻrsatilganidek, loyihani build qilaylik.

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-02/
rm Cargo.lock
cargo clean
cargo build -->

```console
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_core v0.6.3
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling taxminiy_raqam v0.1.0 (file:///projects/taxminiy_raqam)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

<span class="caption">Roʻyxat 2-2: rand cratesini dependency sifatida qoʻshgandan soʻng `cargo build` dan olingan natija</span>

Siz turli xil versiya raqamlarini (lekin ularning barchasi SemVer tufayli kod bilan mos keladi!) va turli xil satrlarni (operatsion tizimga qarab) koʻrishingiz mumkin va satrlar boshqa tartibda boʻlishi mumkin.

Biz tashqi dependency qoʻshganimizda, Cargo [Crates.io][cratesio] maʼlumotlarining nusxasi boʻlgan  *registry* dan dependency uchun zarur boʻlgan barcha narsalarning soʻnggi versiyalarini oladi.Crates.io - bu Rust ekotizimidagi odamlar oʻzlarining ochiq manbali Rust loyihalarini boshqalar foydalanishi uchun joylashtiradigan joy.

registrni yangilagandan soʻng, Cargo  `[dependencies]`  boʻlimini tekshiradi va roʻyxatda hali yuklab olinmagan cratelarni yuklab oladi. Bu holatda, garchi biz faqat `rand` ni dependency sifatida koʻrsatgan boʻlsak-da, Cargo `rand` ishlashga bogʻliq boʻlgan boshqa cratelarni ham oldi. Cratelarni yuklab olgandan soʻng, Rust ularni kompilyatsiya qiladi va keyin mavjud boʻlgan dependency bilan loyihani tuzadi.

Agar siz hech qanday oʻzgartirishlarsiz darhol `cargo build` ni qayta ishga tushirsangiz, `Finished` qatoridan boshqa hech qanday natija olmaysiz. Cargo allaqachon dependencylarni yuklab olganini va kompilyatsiya qilganini biladi va siz *Cargo.toml* faylida ular haqida hech narsani oʻzgartirmagansiz. Cargo, shuningdek, kodingiz haqida hech narsani oʻzgartirmaganligingizni biladi, shuning uchun u ham uni qayta kompilyatsiya qilmaydi. Hech narsa qilmasdan, u shunchaki chiqib ketadi.

Agar siz *src/main.rs* faylini ochsangiz, ahamiyatsiz oʻzgarishlarni amalga oshirsangiz va keyin uni saqlab va qayta build qilsangiz, siz faqat ikkita chiqish qatorini koʻrasiz:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-02/
touch src/main.rs
cargo build -->

```console
$ cargo build
   Compiling taxminiy_raqam v0.1.0 (file:///projects/taxminiy_raqam)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

Bu satrlar shuni koʻrsatadiki, Cargo faqat *src/main.rs* fayliga kichik oʻzgartirishingiz bilan buildni yangilaydi. Sizning dependencylaringiz oʻzgarmadi, shuning uchun Cargo allaqachon yuklab olingan va ular uchun tuzilgan narsadan qayta foydalanishi mumkinligini biladi..

#### *Cargo.lock* fayli bilan qayta tiklanadigan tuzilmalarni taʼminlash

Cargoda siz yoki boshqa birov kodingizni har safar yaratganingizda bir xil artefaktni qayta tiklashingiz mumkinligini taʼminlaydigan mexanizm mavjud: Siz aksini koʻrsatmaguningizcha, cargo faqat siz koʻrsatgan dependency versiyalaridan foydalanadi. Masalan, kelasi hafta `rand` cratening 0.8.6 versiyasi chiqadi va bu versiyada muhim xatoliklar tuzatilgan, lekin u sizning kodingizni buzadigan regressiyani ham o‘z ichiga oladi. Buni hal qilish uchun Rust birinchi marta  `cargo build` dasturini ishga tushirganingizda *Cargo.lock* faylini yaratadi, shuning uchun biz endi bu *guessing_game* jildida mavjud.

Loyihani birinchi marta yaratganingizda, Cargo mezonlarga mos keladigan dependencylarning barcha versiyalarini aniqlaydi va keyin ularni *Cargo.lock* fayliga yozadi. Keyingi loyihangizni yaratganingizda, Cargo *Cargo.lock* fayli mavjudligini koʻradi va versiyalarni qayta aniqlash uchun barcha ishlarni bajarishdan koʻra, u erda koʻrsatilgan versiyalardan foydalanadi. Bu sizga avtomatik ravishda takrorlanadigan tuzilishga ega boʻlish imkonini beradi. Boshqacha qilib aytganda, *Cargo.lock* fayli tufayli loyihangiz aniq yangilanmaguningizcha 0.8.5 da qoladi.
*Cargo.lock* fayli qayta tiklanadigan tuzilmalar uchun muhim boʻlgani uchun u koʻpincha loyihangizdagi kodning qolgan qismi bilan manba nazoratida tekshiriladi.

#### Yangi versiyani olish uchun Crateni yangilash

Crateni yangilamoqchi boʻlsangiz, Cargo `update` buyrugʻini beradi, bu buyruq *Cargo.lock* faylini eʼtiborsiz qoldiradi va *Cargo.toml* dagi texnik xususiyatlaringizga mos keladigan barcha soʻnggi versiyalarni aniqlaydi. Keyin Cargo ushbu versiyalarni *Cargo.lock* fayliga yozadi. Aks holda, standart boʻyicha, Cargo faqat 0.8.5 dan katta va 0.9.0 dan kichik versiyalarni qidiradi. Agar `rand` cratesi ikkita yangi 0.8.6 va 0.9.0 versiyalarini chiqargan boʻlsa, `cargo update` ni ishga tushirgan boʻlsangiz, quyidagilarni koʻrasiz:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-02/
cargo update
assuming there is a new 0.8.x version of rand; otherwise use another update
as a guide to creating the hypothetical output shown here -->

```console
$ cargo update
    Updating crates.io index
    Updating rand v0.8.5 -> v0.8.6
```

Cargo 0.9.0 versiyasiga eʼtibor bermaydi. Bu vaqtda siz *Cargo.lock* faylingizda oʻzgarishlarni ham sezasiz, bunda siz hozir foydalanayotgan `rand`  cratesi versiyasi 0.8.6. `rand` 0.9.0 versiyasidan yoki 0.9.*x* seriyasining istalgan versiyasidan foydalanish uchun *Cargo.toml* faylini quyidagi koʻrinishda yangilashingiz kerak boʻladi:

```toml
[dependencies]
rand = "0.9.0"
```

Keyingi safar `cargo build`ni ishga tushirganingizda, Cargo mavjud cratelar reestrini yangilaydi va siz ko‘rsatgan yangi versiyaga muvofiq `rand` talablaringizni qayta baholaydi.

[Cargo][doccargo]<!-- ignore --> va uning [ekotizimlari][doccratesio]<!-- ignore --> haqida koʻp gapirish mumkin, biz ularni 14-bobda muhokama qilamiz, ammo hozircha bilishingiz kerak boʻlgan narsa shu. Cargo kutubxonalarni qayta ishlatishni juda osonlashtiradi, shuning uchun Rustaceans bir nechta paketlardan yigʻilgan kichikroq loyihalarni yozishga qodir.

### Tasodifiy raqamni yaratish

Keling, taxmin qilish uchun raqam yaratishda `rand` dan foydalanishni boshlaylik. Keyingi qadam 2-3 roʻyxatda koʻrsatilganidek *src/main.rs* ni yangilashdir.

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-03/src/main.rs:all}}
```

<span class="caption">Roʻyxat 2-3: Tasodifiy raqam yaratish uchun kod qoʻshiladi</span>

Avval `use rand::Rng;` qatorini qoʻshamiz. `Rng` traiti tasodifiy sonlar generatorlari qoʻllaydigan metodlarni belgilaydi va biz ushbu usullardan foydalanishimiz uchun bu trait mos boʻlishi kerak. 10-bobda traitlar batafsil yoritiladi.

Keyin oʻrtada ikkita qator qoʻshamiz. Birinchi qatorda biz `rand::thread_rng` funksiyasini chaqiramiz, bu bizga biz foydalanmoqchi boʻlgan tasodifiy sonlar generatorini beradi: joriy bajarilish oqimi uchun mahalliy boʻlgan va operatsion tizim tomonidan ekilgan. Keyin tasodifiy sonlar generatorida `gen_range` metodini chaqiramiz. Bu metod biz `use rand::Rng;`  iborasi bilan qamrab olgan `Rng` traiti bilan aniqlanadi. `gen_range` metodi argument sifatida diapazon ifodasini oladi va diapazonda tasodifiy son hosil qiladi. Biz bu yerda foydalanayotgan diapazon ifodasi turi `start..=end`  shaklini oladi va pastki va yuqori chegaralarni qamrab oladi, shuning uchun biz 1 va 100 oralig‘idagi raqamni so‘rash uchun `1..=100` ni belgilashimiz kerak. .


> Eslatma: Siz faqat qaysi traitlardan foydalanishni va qaysi metodlar va funktsiyalarni
> cratedan chaqirishni bila olmaysiz, shuning uchun har bir crateda foydalanish boʻyicha
> koʻrsatmalar mavjud. Cargo-ning yana bir qulay xususiyati shundaki, `cargo doc --open` buyrugʻini
> ishga tushirish sizning barcha dependencylar tomonidan taqdim etilgan texnik hujjatlarni
> mahalliy sifatida tuzadi va uni brauzeringizda ochadi. Agar siz `rand` cratedagi boshqa
> funksiyalarga qiziqsangiz, masalan, `cargo doc --open` ni ishga tushiring va chap tomondagi
> yon paneldagi `rand` tugmasini bosing.

Ikkinchi yangi qator maxfiy raqamni chop etadi. Bu dasturni ishlab chiqishda uni sinab koʻrishimiz uchun foydalidir, lekin biz uni oxirgi versiyadan oʻchirib tashlaymiz. Agar dastur boshlanishi bilanoq javobni chop etsa, bu unchalik oʻyin emas!

Dasturni bir necha marta ishga tushirishga harakat qiling:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-03/
cargo run
4
cargo run
5
-->

```console
$ cargo run
   Compiling taxminiy_raqam v0.1.0 (file:///projects/taxminiy_raqam)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/taxminiy_raqam`
Raqamni topish oʻyini!
Yashirin raqam: 7
Iltimos, taxminingizni kiriting.
4
Siznig taxminingiz: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/taxminiy_raqam`
Raqamni topish oʻyini!
Yashirin raqam: 83
Iltimos, taxminingizni kiriting.
5
Siznig taxminingiz: 5
```

Siz turli xil tasodifiy raqamlarni olishingiz kerak va ularning barchasi 1 dan 100 gacha raqamlar boʻlishi kerak. Ajoyib ish!

## Taxminni maxfiy raqam bilan solishtirish

Endi bizda foydalanuvchi kiritishi va tasodifiy raqam bor, biz ularni solishtirishimiz mumkin. Ushbu qadam 2-4 roʻyxatda koʻrsatilgan. Eʼtibor bering, bu kod hozircha kompilatsiya boʻlmaydi, biz tushuntiramiz.

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-04/src/main.rs:here}}
```

<span class="caption">Roʻyxat 2-4: Ikki raqamni solishtirishning mumkin boʻlgan qaytish qiymatlarini boshqarish</span>

Avval biz standart kutubxonadan `std::cmp::Ording` deb nomlangan turni olib keladigan yana bir `use` iborasini qoʻshamiz. `Ordering` turi boshqa raqam boʻlib, `Less`, `Greater` va `Equal` variantlariga ega. Bu ikkita qiymatni solishtirganda mumkin boʻlgan uchta natijadir.

Keyin pastki qismida `Ordering` turidan foydalanadigan beshta yangi qator qoʻshamiz. `cmp` metodi ikkita qiymatni solishtiradi va uni solishtirish mumkin boʻlgan har qanday narsani chaqirish mumkin. Siz solishtirmoqchi boʻlgan narsaga reference kerak: bu yerda `taxmin` bilan `yashirin_raqam` solishtiriladi. Keyin u biz `use`  iborasi bilan qamrab olgan `Ordering`  raqamining variantini qaytaradi. Biz `taxmin` va `yashirin_raqam` qiymatlari bilan `cmp` ga murojatdan `Ordering` ning qaysi varianti qaytarilganiga qarab, keyin nima qilish kerakligini hal qilish uchun [`match`][match]<!-- ignore --> ifodasidan foydalanamiz.

`Match` ifodasi *arms* dan tuzilgan. Arm mos keladigan *pattern* va agar `match` ga berilgan qiymat armning patterniga mos kelsa, bajarilishi kerak boʻlgan koddan iborat. Rust `match` ga berilgan qiymatni oladi va har bir armning patternini oʻz navbatida koʻrib chiqadi. Patternlar va `match` konstruksiyasi Rust-ning kuchli xususiyatlari hisoblanadi: ular sizning kodingiz duch kelishi mumkin boʻlgan turli vaziyatlarni ifodalash imkonini beradi va ularning barchasini boshqarishingizga ishonch hosil qiladi. Bu xususiyatlar mos ravishda 6-bobda va 18-bobda batafsil yoritiladi.

Keling, bu yerda ishlatadigan `match` iborasi bilan bir misolni koʻrib chiqaylik. Aytaylik, foydalanuvchi 50 ni taxmin qilgan va bu safar tasodifiy yaratilgan maxfiy raqam 38 ni tashkil qiladi.

Kod 50 ni 38 ga solishtirganda, `cmp` metodi `Ordering::Greater` ni qaytaradi, chunki 50 38 dan katta. `match` ifodasi `Ordering::Greater` qiymatini oladi va har bir armning patternini tekshirishni boshlaydi. U birinchi armning `Ordering::Less` patternini koʻrib chiqadi va `Ordering::Greater` qiymati `Ordering::Less` qiymatiga mos kelmasligini koʻradi, shuning uchun u armdagi kodga eʼtibor bermaydi va keyingi armga oʻtadi. Keyingi armning namunasi `Ordering::Greater` boʻlib, `Ordering::Greater` bilan *does* match  keladi! Oʻsha armdagi bogʻlangan kod ishga tushadi va ekranga `Raqam katta!` deb chop etiladi. `match` iborasi birinchi muvaffaqiyatli oʻyindan keyin tugaydi, shuning uchun bu senariydagi oxirgi armni koʻrib chiqmaydi.

Biroq, 2-4 roʻyxatdagi kod hali kompilyatsiya qilinmaydi. Keling, sinab koʻraylik:

<!--
The error numbers in this output should be that of the code **WITHOUT** the
anchor or snip comments
-->

```console
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-04/output.txt}}
```

Xatoning asosi *mos kelmaydigan turlar* mavjudligini bildiradi. Rust kuchli, statik turdagi tizimga ega. Biroq, u ham turdagi inference ega. Biz `let mut taxmin = String::new()` deb yozganimizda, Rust `taxmin` `String` boʻlishi kerak degan xulosaga keldi va bizni turni yozishga majburlamadi. Boshqa tomondan, `yashirin_raqam` raqam turidir. Rust raqamlarining bir nechta turlari 1 dan 100 gacha qiymatga ega boʻlishi mumkin: `i32`, 32 bitli raqam; `u32`, unsigned 32-bitli raqam; `i64`, 64-bitli raqam; boshqalar kabi. Agar boshqacha koʻrsatilmagan boʻlsa, Rust standart boʻyicha `i32` ga oʻrnatiladi, bu `yashirin_raqam` turiga, agar siz Rustning boshqa raqamli turini chiqarishiga olib keladigan turdagi maʼlumotlarni boshqa joyga qoʻshmasangiz. Xatoning sababi shundaki, Rust string va raqam turini taqqoslay olmaydi.

Oxir-oqibat, biz dastur tomonidan kiritilgan `String` ni haqiqiy son turiga aylantirmoqchimiz, shuning uchun uni raqamli raqam bilan yashirin raqam bilan solishtirishimiz mumkin.Buni `main` funksiya tanasiga ushbu qatorni qoʻshish orqali qilamiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-03-convert-string-to-number/src/main.rs:here}}
```

Satr

```rust,ignore
let taxmin: u32 = taxmin.trim().parse().expect("Iltimos, raqam yozing!");
```

Biz `taxmin` nomli oʻzgaruvchini yaratamiz. Ammo shoshilmang, dasturda allaqachon `taxmin` nomli oʻzgaruvchi mavjud emasmi? Bu shunday, lekin foydali Rust bizga `taxmin` ning oldingi qiymatini yangisi bilan ergashtirish imkonini beradi. *Shadowing* bizga ikkita noyob oʻzgaruvchini yaratish oʻrniga, `taxmin` oʻzgaruvchi nomidan qayta foydalanish imkonini beradi, masalan, `taxmin_str` va `taxmin`. Biz buni [3-bobda][shadowing]<!-- ignore --> batafsil koʻrib chiqamiz, ammo hozircha shuni bilingki, bu xususiyat koʻpincha qiymatni bir turdan boshqa turga aylantirmoqchi boʻlganingizda ishlatiladi.

Biz bu yangi oʻzgaruvchini `taxmin.trim().parse()` ifodasiga bogʻlaymiz. Ifodadagi `taxmin` matni qator sifatida kiritilgan asl `taxmin` oʻzgaruvchisiga ishora qiladi. `String` misolidagi `trim` metodi boshida va oxiridagi har qanday bo‘shliqni yo‘q qiladi, bu qatorni faqat raqamli ma’lumotlarni o‘z ichiga olishi mumkin bo‘lgan `u32` bilan solishtirishimiz uchun buni qilishimiz kerak. Foydalanuvchi `read_line` ni toʻldirish uchun <span class="keystroke">enter</span>tugmasini bosib, ularni kiritishi kerak
satrga yangi satr belgisini qoʻshadigan taxmin. Masalan, agar foydalanuvchi <span class="keystroke">5</span> raqamini kiritsa va va <span class="keystroke">enter</span> tugmasini bossa `taxmin` shunday koʻrinadi: `5\n`.
`\n` “yangi qator”ni bildiradi. (Windows tizimida <span class="keystroke">enter</span> tugmasini bosish natijasida carriage qaytariladi va yangi qator `\r\n` chiqadi.)
 `trim` metodi `\n` yoki `\r\n`ni yoʻq qiladi, natijada atigi `5` bo`ladi.

Satrlardagi [`parse` metodi][parse]<!-- ignore --> qatorni boshqa turga aylantiradi.
Bu yerda biz uni stringdan raqamga aylantirish uchun foydalanamiz. Biz Rustga `let taxmin: u32` yordamida kerakli raqam turini aytishimiz kerak. `taxmin` dan keyin ikki nuqta (`:`) Rustga oʻzgaruvchining turiga izoh berishimizni aytadi. Rust bir nechta oʻrnatilgan raqam turlariga ega; Bu yerda koʻrilgan `u32` unsigned, 32-bitli butun son.
Bu kichik ijobiy raqam uchun yaxshi standart tanlovdir. Boshqa raqamlar turlari haqida [3-bobda][integers]<!-- ignore --> bilib olasiz.

Bundan tashqari, ushbu misol dasturidagi `u32` annotation va `yashirin_raqam` bilan taqqoslash Rust `yashirin_raqam` ham `u32` boʻlishi kerak degan xulosaga keladi. Shunday qilib, endi taqqoslash bir xil turdagi ikkita qiymat oʻrtasida boʻladi!

`parse` metodii faqat mantiqiy ravishda raqamlarga aylantirilishi mumkin boʻlgan belgilarda ishlaydi va shuning uchun osongina xatolarga olib kelishi mumkin. Agar, masalan, satrda `A👍%` boʻlsa, uni raqamga aylantirishning hech qanday metodi boʻlmaydi. Muvaffaqiyatsiz boʻlishi mumkinligi sababli, `parse` metodii `read_line` metodi kabi `Result` turini qaytaradi (oldingi ["`Result` bilan potentsial muvaffaqiyatsizlikni koʻrib chiqish"] boʻlimida muhokama qilingan)(#handling-potential-failure-with-result)<!-- ignore-->). Biz ushbu `Result` ga yana `expect` metodini qoʻllash orqali xuddi shunday munosabatda boʻlamiz. Agar `parse` qatordan raqam yarata olmagani uchun `Err` `Result` variantini qaytarsa, `expect` chaqiruvi o‘yinni buzadi va biz bergan xabarni chop etadi.
Agar `parse` qatorni raqamga muvaffaqiyatli aylantira olsa, u `Result`ning `Ok` variantini qaytaradi va `expect` biz xohlagan raqamni `Ok` qiymatidan qaytaradi.

Endi dasturni ishga tushiramiz:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/no-listing-03-convert-string-to-number/
cargo run
  76
-->

```console
$ cargo run
   Compiling taxminiy_raqam v0.1.0 (file:///projects/taxminiy_raqam)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/taxminiy_raqam`
Raqamni topish oʻyini!
Yashirin raqam: 58
Iltimos, taxminingizni kiriting.
  76
Sizning taxminingiz: 76
Raqam katta!
```

Yaxshi! Tahmindan oldin boʻshliqlar qoʻshilgan boʻlsa ham, dastur foydalanuvchi 76 ni taxmin qilganini aniqladi. Har xil turdagi kirishlar bilan turli xatti-harakatlarni tekshirish uchun dasturni bir necha marta ishga tushiring: raqamni toʻgʻri taxmin qiling, katta raqamni taxmin qiling va kichik raqamni taxmin qiling.

Hozir bizda oʻyinning koʻp qismi ishlayapti, lekin foydalanuvchi faqat bitta taxmin qila oladi. Keling, buni loop qoʻshish orqali oʻzgartiraylik!

## Loop bilan bir nechta taxminlarga ruxsat berish

`loop` kalit soʻzi cheksiz tsiklni yaratadi. Biz foydalanuvchilarga raqamni taxmin qilishda koʻproq imkoniyat berish uchun tsikl qoʻshamiz:
<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-04-looping/src/main.rs:here}}
```

Koʻrib turganingizdek, biz hamma narsani taxminiy kiritish soʻrovidan boshlab tsiklga oʻtkazdik. Ilova ichidagi satrlarni har birida yana toʻrtta boʻsh joydan oʻtkazganingizga ishonch hosil qiling va dasturni qayta ishga tushiring. Dastur endi boshqa bir taxminni abadiy yani har doim soʻraydi, bu aslida yangi muammoni keltirib chiqaradi. Foydalanuvchi chiqa olmaydiganga oʻxshaydi!

Foydalanuvchi har doim <span class="keystroke">ctrl-c</span> klaviatura yorligʻi yordamida dasturni toʻxtatishi mumkin. Ammo bu toʻyib boʻlmaydigan yirtqich hayvondan qochishning yana bir yoʻli bor, [“Taxminni maxfiy raqam bilan solishtirish“](#comparing-the-guess-to-the-secret-number)<!--ignore -->: mavzusidagi `parse` muhokamasida aytib oʻtilganidek, agar foydalanuvchi raqam boʻlmagan javobni kiritsa, dastur buziladi. Bu yerda koʻrsatilganidek, foydalanuvchiga chiqishga ruxsat berish uchun undan foydalanishimiz mumkin

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/no-listing-04-looping/
cargo run
(too small guess)
(too big guess)
(correct guess)
quit
-->

```console
$ cargo run
   Compiling taxminiy_raqam v0.1.0 (file:///projects/taxminiy_raqam)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/taxminiy_raqam`
Raqamni topish oʻyini!
Yashirin raqam: 59
Iltimos, taxminingizni kiriting.
45
Sizning taxminingiz: 45
Raqam Kichik!
Iltimos, taxminingizni kiriting.
60
Sizning taxminingiz: 60
Raqam katta!
Iltimos, taxminingizni kiriting.
59
Sizning taxminingiz: 59
Siz yutdingiz!
Iltimos, taxminingizni kiriting.
quit
thread 'mainʼ panicked at 'Please type a number!: ParseIntError { kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

`quit` deb yozsangiz, o‘yin tugaydi, lekin siz ko‘rganingizdek, boshqa raqam bo‘lmagan ma’lumotlarni kiritish ham shunday bo‘ladi. Bu, eng kamida, suboptimaldir; Biz toʻgʻri raqam taxmin qilinganda ham oʻyin toʻxtashini xohlaymiz.

### Toʻgʻri taxmindan keyin chiqish

Keling, foydalanuvchi gʻalaba qozonganida `break` iborasini qoʻshish orqali oʻyinni toʻxtatish uchun dasturlashtiramiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-05-quitting/src/main.rs:here}}
```

`Siz yutdingiz!` so‘ng `break` qatorini qo‘shish foydalanuvchi maxfiy raqamni to‘g‘ri taxmin qilganda dasturni tsikldan chiqadi. Loopdan chiqish dasturdan chiqishni ham anglatadi, chunki sikl `main` ning oxirgi qismidir.

### Notoʻgʻri kiritish

Oʻyinning xatti-harakatlarini yanada yaxshilash uchun, foydalanuvchi raqamlardan boshqa belgilar kiritganda dasturni ishdan chiqargandan koʻra, foydalanuvchi taxmin qilishni davom ettirishi uchun oʻyinni raqam boʻlmagan belgilarga eʼtibor bermaslikka harakat qildiraylik. Buni 2-5 roʻyxatda koʻrsatilganidek, `taxmin` satrdan `u32` ga aylantirilgan qatorni oʻzgartirish orqali amalga oshirishimiz mumkin.

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-05/src/main.rs:here}}
```

<span class="caption">Roʻyxat 2-5: Raqamsiz taxminga eʼtibor bermaslik va dasturni ishdan chiqarish oʻrniga boshqa taxminni soʻrash</span>

Xato ustida ishlamay qolishdan xatoni hal qilishga o‘tish uchun biz `expect` chaqiruvidan `match` ifodasiga o‘tamiz. Esda tutingki, `parse` `Result` turini qaytaradi, `Result` esa `Ok` va `Err` variantlariga ega boʻlgan raqamdir. Biz bu yerda `cmp` metodining `Ordering` natijasi bilan bo‘lgani kabi `match` ifodasidan foydalanmoqdamiz.

Agar `parse` qatorni raqamga muvaffaqiyatli aylantira olsa, natijada olingan raqamni oʻz ichiga olgan `Ok` qiymatini qaytaradi. Bu `Ok` qiymati birinchi armning patterniga mos keladi va `match` ifodasi `parse` ishlab chiqarilgan va `Ok` qiymatiga qoʻygan `num` qiymatini qaytaradi. Bu raqam biz yaratayotgan yangi `taxmin`  oʻzgaruvchisida biz xohlagan joyda tugaydi

Agar `parse` satrni raqamga aylantira olmasa xato haqida qoʻshimcha maʼlumotni oʻz ichiga olgan `Err` qiymatini qaytaradi. `Err` qiymati birinchi `match` bo‘limidagi `Ok(num)` patterniga mos kelmaydi, lekin ikkinchi armdagi `Err(_)` patterniga mos keladi. Pastki chiziq, `_`, diqqatga sazovor qiymatdir; bu misolda biz barcha `Err` qiymatlariga, ular ichida qanday maʼlumotlar boʻlishidan qatʼiy nazar, mos kelmoqchimiz deymiz. Shunday qilib, dastur ikkinchi armning `continue` kodini bajaradi, bu dasturga `loop` ning keyingi iteratsiyasiga oʻtishni va boshqa taxminni soʻrashni aytadi. Shunday qilib, dastur `parse` duch kelishi mumkin boʻlgan barcha xatolarga eʼtibor bermaydi!

Endi dasturdagi hamma narsa kutilganidek ishlashi kerak. Keling, sinab koʻraylik:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-05/
cargo run
(too small guess)
(too big guess)
foo
(correct guess)
-->

```console
$ cargo run
   Compiling taxminiy_raqam v0.1.0 (file:///projects/taxminiy_raqam)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/taxminiy_raqam`
Raqamni topish oʻyini!
Yashirin raqam: 61
Iltimos, taxminingizni kiriting.
10
Sizning taxminingiz: 10
Raqam Kichik!
Iltimos, taxminingizni kiriting.
99
Sizning taxminingiz: 99
Raqam katta!
Iltimos, taxminingizni kiriting.
foo
Iltimos, taxminingizni kiriting.
61
Sizning taxminingiz: 61
Siz yutdingiz!
```

Ajoyib! Bitta kichik soʻnggi tweak bilan biz taxmin qilish oʻyinini tugatamiz. Eslatib oʻtamiz, dastur hali ham maxfiy raqamni chop etmoqda. Bu sinov uchun yaxshi ishladi, lekin oʻyinni buzadi. Maxfiy raqamni chiqaradigan `println!`ni oʻchirib tashlaymiz. 2-6 roʻyxat yakuniy kodni koʻrishingiz mumkin.

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-06/src/main.rs}}
```

<span class="caption">Roʻyxat 2-6: Toʻliq taxmin qilish oʻyin kodini</span>

Shu nuqtada, siz taxmin qilish oʻyinini muvaffaqiyatli yaratdingiz. Tabriklaymiz!

## Xulosa

Ushbu loyiha sizni Rustning koʻplab yangi tushunchalari bilan tanishtirishning amaliy usuli boʻldi: `let`, `match`, funktsiyalar, tashqi cratelardan foydalanish va boshqalar. Keyingi bir necha boblarda siz ushbu tushunchalar haqida batafsilroq bilib olasiz. 3-bob koʻpchilik dasturlash tillarida mavjud boʻlgan oʻzgaruvchilar, maʼlumotlar turlari va funktsiyalari kabi tushunchalarni qamrab oladi va ulardan Rustda qanday foydalanishni koʻrsatadi. 4-bobda Rust tilini boshqa tillardan ajratib turadigan egalik huquqi o‘rganiladi. 5-bobda tuzilmalar va metodlar sintaksisi muhokama qilinadi va 6-bobda enumlar qanday ishlashi tushuntiriladi.

[prelude]: ../std/prelude/index.html
[variables-and-mutability]: ch03-01-variables-and-mutability.html#variables-and-mutability
[comments]: ch03-04-comments.html
[string]: ../std/string/struct.String.html
[iostdin]: ../std/io/struct.Stdin.html
[read_line]: ../std/io/struct.Stdin.html#method.read_line
[result]: ../std/result/enum.Result.html
[enums]: ch06-00-enums.html
[expect]: ../std/result/enum.Result.html#method.expect
[recover]: ch09-02-recoverable-errors-with-result.html
[randcrate]: https://crates.io/crates/rand
[semver]: http://semver.org
[cratesio]: https://crates.io/
[doccargo]: http://doc.crates.io
[doccratesio]: http://doc.crates.io/crates-io.html
[match]: ch06-02-match.html
[shadowing]: ch03-01-variables-and-mutability.html#shadowing
[parse]: ../std/primitive.str.html#method.parse
[integers]: ch03-02-data-types.html#integer-types
