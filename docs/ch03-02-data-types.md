## Maʼlumotlar turlari

Rust-dagi har bir qiymat maʼlum bir *maʼlumot turiga* tegishli boʻlib, Rustga qanday maʼlumotlar koʻrsatilayotganligini bildiradi, shuning uchun u ushbu maʼlumotlar bilan qanday ishlashni biladi. Biz ikkita maʼlumotlar turini koʻrib chiqamiz: skalyar va birikma.

Esda tutingki, Rust *statik tarzda yozilgan* tildir, yaʼni kompilyatsiya vaqtida barcha oʻzgaruvchilarning turlarini bilishi kerak. Kompilyator odatda qiymat va uni qanday ishlatishimiz asosida biz qaysi turdan foydalanmoqchi ekanligimiz haqida xulosa chiqarishi mumkin.
Ko‘p turlar mumkin bo‘lgan hollarda, masalan, 2-bobdagi [“Tahminni maxfiy raqam bilan solishtirish”][comparing-the-guess-to-the-secret-number]<!-- ignore --> bo‘limidagi `parse` yordamida `String`ni raqamli turga o‘zgartirganimizda, quyidagi turdagi izohni qo‘shishimiz kerak:

```rust
let taxmin: u32 = "42".parse().expect("Raqam emas!");
```

Oldingi kodda koʻrsatilgan `: u32` turidagi izohni qoʻshmasak, Rust quyidagi xatoni koʻrsatadi, yaʼni kompilyator bizdan qaysi turdan foydalanishni xohlayotganimizni bilish uchun qoʻshimcha maʼlumotga muhtoj:

```console
{{#include ../listings/ch03-common-programming-concepts/output-only-01-no-type-annotations/output.txt}}
```

Boshqa maʼlumotlar turlari uchun turli turdagi izohlarni koʻrasiz.

### Skalyar Turlar

*Skalyar* turi bitta qiymatni ifodalaydi. Rust toʻrtta asosiy skalyar turga ega: integerlar, floating-point number, boolean va belgilar. Siz ularni boshqa dasturlash tillaridan bilishingiz mumkin. Keling, ularning Rustda qanday ishlashini koʻrib chiqaylik.

#### Integer Turlari

*Integer* kasr komponenti bo‘lmagan sondir. Biz 2-bobda `u32` tipidagi bitta *integer* sonni ishlatdik. Ushbu turdagi deklaratsiya u bilan bogʻlangan qiymat 32 bit boʻsh joyni egallagan belgisiz butun son boʻlishi kerakligini bildiradi (Signed integer sonlar `u` oʻrniga `i` bilan boshlanadi). 3-1-jadvalda Rust-da oʻrnatilgan integer son turlari koʻrsatilgan. Integer son qiymatining turini eʼlon qilish uchun biz ushbu variantlardan foydalanishimiz mumkin.

<span class="caption">3-1-jadval: Rustdagi Integer sonlar turlari</span>

| Uzunlik | Signed  | Unsigned |
|---------|---------|----------|
| 8-bit   | `i8`    | `u8`     |
| 16-bit  | `i16`   | `u16`    |
| 32-bit  | `i32`   | `u32`    |
| 64-bit  | `i64`   | `u64`    |
| 128-bit | `i128`  | `u128`   |
| arch    | `isize` | `usize`  |

Signedlar kichkina `i` harfi bilan boshlanadi, Unsigned esa kichik `u` harfi bilan boshlanadi.

Har bir variant signed yoki unsigned boʻlishi mumkin va aniq oʻlchamga ega.
*Signed* va *Unsigned* raqam manfiy boʻlishi mumkinmi yoki yoʻqligini anglatadi, boshqacha qilib aytganda, raqam u bilan birga belgiga ega boʻlishi (signed) boʻlishi kerakmi yoki u faqat ijobiy boʻladimi va shuning uchun belgisiz (unsigned) ifodalanishi mumkinmi. Bu raqamlarni qogʻozga yozishga oʻxshaydi: belgi muhim boʻlsa, raqam ortiqcha yoki minus belgisi bilan koʻrsatiladi; ammo, agar raqamni ijobiy deb hisoblash xavfsiz boʻlsa, u hech qanday belgisiz koʻrsatiladi.
Signed raqamlar [ikkita toʻldiruvchi][twos-complement]<!-- ignore--> koʻrinish yordamida saqlanadi.


Har bir signed variant -(2<sup>n - 1</sup>) dan 2<sup>n -
1</sup> -1 gacha boʻlgan raqamlarni saqlashi mumkin, bu erda *n* variant foydalanadigan bitlar soni.
Shunday qilib, `i8` -(2<sup>7</sup>) dan 2<sup>7</sup> - 1, gacha boʻlgan raqamlarni saqlashi mumkin, bu tengdir -128 dan 127 gacha.
Unsigned variantlar 0 dan 2<sup>n</sup> - 1 gacha raqamlarni saqlashi mumkin, shuning uchun `u8` 0 dan 2<sup>8</sup> - 1 gacha boʻlgan raqamlarni saqlashi mumkin, bu 0 dan 255 gacha.

Bundan tashqari, `isize` va `usize` turlari dasturingiz ishlayotgan kompyuterning arxitekturasiga bogʻliq boʻlib, u jadvalda “arch” sifatida koʻrsatilgan: agar siz 64 bitli arxitekturada boʻlsangiz 64 bit va 32 bitli arxitekturada boʻlsangiz 32 bit.

Integer sonlarni 3-2-jadvalda koʻrsatilgan istalgan shaklda yozishingiz mumkin. Eʼtibor bering, bir nechta raqamli turlar boʻlishi mumkin boʻlgan son harflari turni belgilash uchun `57u8` kabi tur qoʻshimchasiga ruxsat beradi. Raqamni oʻqishni osonlashtirish uchun `_` dan raqamli harflar ham foydalanishi mumkin, masalan, `1_000`, siz `1000` ni koʻrsatganingizdek bir xil qiymatga ega boʻladi.

<span class="caption">3-2-jadval: Rustdagi Integer literallar</span>

| Raqamli harflar   | Misol         |
|-------------------|---------------|
| Oʻnlik            | `98_222`      |
| Oʻn oltilik       | `0xff`        |
| Sakkizlik         | `0o77`        |
| Ikkilik           | `0b1111_0000` |
| Bayt (faqat "u8") | `bʼAʼ`        |

Xoʻsh, qaysi turdagi integer sonni ishlatishni qanday bilasiz? Agar ishonchingiz komil boʻlmasa, Rustning standart sozlamalari odatda boshlash uchun yaxshi joylardir: integer son turlari standart boʻyicha `i32` dir. `isize` yoki `usize` dan foydalanadigan asosiy holat toʻplamning bir turini indekslashdir.

> ##### Integer Overflow
>
> Aytaylik, sizda 0 dan 255 gacha boʻlgan qiymatlarni ushlab turadigan `u8` tipidagi oʻzgaruvchi bor.
> Agar siz oʻzgaruvchini ushbu diapazondan tashqaridagi qiymatga oʻzgartirishga harakat qilsangiz,
> masalan, 256, *integer overflow* sodir boʻladi, bu ikki xatti-harakatdan biriga olib kelishi mumkin.
> Debug mode rejimida kompilyatsiya qilayotganingizda, Rust butun sonlarning toʻlib ketishini
> tekshirishni oʻz ichiga oladi, bu esa dasturni ishga tushirish vaqtida *panic* chiqaradi. Rust
> dastur xato bilan chiqqanda *panicking* atamasini ishlatadi; Biz panic haqida 9-bobdagi
> [“`panic` bilan tuzatib boʻlmaydigan xatolar”][unrecoverable-errors-with-panic]<!-- ignore -->
> boʻlimda batafsil koʻrib chiqamiz
> 
> `--release` buyrugʻi bilan reliz rejimida kompilyatsiya qilayotganingizda, Rust
> panic keltirib chiqaradigan butun sonlarni tekshirishni *oʻz ichiga olmaydi*.
> overflow occur sodir boʻladi Rust *ikkitasini toʻldiruvchi wrapni* bajaradi. Qisqa qilib
> aytganda, turdagi maksimal qiymatdan kattaroq qiymatlar, tur ushlab turishi mumkin boʻlgan minimal
> qiymatlargacha "wrap" ni tashkil qiladi. `u8` holatida 256 qiymati 0 ga, 257 qiymati
> 1 ga aylanadi va hokazo. Dastur panic qoʻymaydi, lekin oʻzgaruvchi
> siz kutgan qiymatga ega boʻlmaydi. Butun sonlarni wrapga tayanish
> xato hisoblanadi. Owerflow ehtimolini aniq koʻrib chiqish uchun siz prime sonlar uchun
> standart kutubxona tomonidan taqdim etilgan ushbu metodlar oilalaridan foydalanishingiz mumkin:
> 
> * Barcha modelarni `wrapping_*` metodlari bilan oʻrash, masalan, `wrapping_add`.
> * Agar `checked_*` metodlari owerflow boʻlsa, `None` qiymatini qaytaring.
> * Qiymat va boolean qiymatni qaytaring, bu `overflowing_*` metodlari
>   bilan overflow boʻlganini koʻrsatadi.
> * Qiymatning minimal yoki maksimal qiymatlarida `saturating_*`
>   metodllari bilan saturate boʻlgan.

#### Floating-Point Turlari

Rust shuningdek *floating-point raqamlar* uchun ikkita primitive turga ega, ular kasrli raqamlardir.
Rust-ning floating-point turlari `f32` va `f64` boʻlib, ular mos ravishda 32 bit va 64 bit oʻlchamga ega.
Standart tur `f64` dir, chunki zamonaviy protsessorlarda u `f32` bilan bir xil tezlikda, lekin aniqroq boʻlishga qodir.
Barcha floating-point turlari signeddir.

Bu yerda harakatdagi floating-point raqamlarni koʻrsatadigan misol:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-06-floating-point/src/main.rs}}
```

Floating-point raqamlari IEEE-754 standartiga muvofiq taqdim etiladi. `f32` turi bitta aniqlikdagi floatdir va `f64` ikki tomonlama aniqlikka ega.

#### Raqamli operatsiyalar

Rust barcha turdagi raqamlar uchun kutilgan asosiy matematik operatsiyalarni qoʻllab-quvvatlaydi: qoʻshish, ayirish, koʻpaytirish, boʻlish va qoldiq. Butun sonni boʻlish noldan eng yaqin butun songa qisqaradi. Quyidagi kod `let` iborasida har bir raqamli operatsiyadan qanday foydalanishni koʻrsatadi:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-07-numeric-operations/src/main.rs}}
```

Ushbu bayonotlardagi har bir ifoda matematik operatordan foydalanadi va bitta qiymatga baholanadi, keyin esa oʻzgaruvchiga bogʻlanadi. [B ilovasi][appendix_b]<!-- ignore --> da
Rust taqdim etgan barcha operatorlar roʻyxati mavjud.

#### Boolean turi

Koʻpgina boshqa dasturlash tillarida boʻlgani kabi, Rust-da ham Boolean turi ikkita mumkin boʻlgan qiymatga ega: `true` va `false`. Boolean hajmi bir baytga teng.
Rustdagi boolean turi `bool` yordamida belgilanadi. Misol uchun:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-08-boolean/src/main.rs}}
```

Boolean qiymatlardan foydalanishning asosiy metodi shartlardir, masalan, `if` ifodasidir. Rustda `if` iboralari qanday ishlashini [“Control Flow”][control-flow]<!-- ignore --> bo‘limida ko‘rib chiqamiz.

#### Belgilar(Character) turi

Rustning `char` turi tilning eng primitive alifbo turidir. Mana `char` qiymatlarini eʼlon qilishning ba`zi misollari:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-09-char/src/main.rs}}
```

Eʼtibor bering, biz qoʻsh tirnoq ishlatadigan satr harflaridan farqli oʻlaroq, `char` harflarini bitta tirnoq bilan belgilaymiz. Rustning `char` turi toʻrt bayt oʻlchamga ega va Unicode Scalar qiymatini ifodalaydi, yaʼni u ASCIIdan koʻra koʻproq narsani anglatishi mumkin.
Urgʻuli harflar; Xitoy, yapon va koreys belgilar; emoji; va nol kenglikdagi boʻshliqlar Rust-dagi barcha haqiqiy `char` qiymatlaridir. Unicode Scalar qiymatlari `U+0000`dan `U+D7FF`gacha va `U+E000`dan `U+10FFFF`gacha.
Biroq, “character” aslida Unicode-da tushuncha emas, shuning uchun “character” nima ekanligi haqidagi Rustdagi `char` bilan mos kelmasligi mumkin. Biz ushbu mavzuni 8-bobdagi [“UTF-8 kodlangan matnni satrlar bilan saqlash”][strings]<!-- ignore --> boʻlimida batafsil muhokama qilamiz.

### Murakkab turlar

*Murakkab turlar* bir nechta qiymatlarni bir turga toʻplashi mumkin.Rust ikkita primitive birikma turiga ega: tuplelar va arraylar.

#### Tuple turi

*tuple* - bu turli xil turlarga ega boʻlgan bir qator qiymatlarni bitta qoʻshma turga birlashtirishning umumiy metodi.Tuplelar belgilangan uzunlikka ega: bir marta eʼlon qilingandan soʻng, ular oʻsishi yoki kichrayishi mumkin emas.

Qavslar ichida vergul bilan ajratilgan qiymatlar roʻyxatini yozish orqali tuple yaratamiz. Tupledagi har bir pozitsiya oʻz turiga ega va tupledagi turli qiymatlarning turlari bir xil boʻlishi shart emas. Ushbu misolda biz ixtiyoriy turdagi izohlarni qoʻshdik:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-10-tuples/src/main.rs}}
```

`tup` oʻzgaruvchisi butun tuplega bogʻlanadi, chunki tuple bitta birikma element hisoblanadi. Tupledan individual qiymatlarni olish uchun biz tuple qiymatini buzish uchun pattern moslashuvidan foydalanishimiz mumkin, masalan:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-11-destructuring-tuples/src/main.rs}}
```

Bu dastur avval tuple yaratadi va uni `tup` oʻzgaruvchisiga bogʻlaydi.Keyin u `tup`ni olish va uni uchta alohida o‘zgaruvchiga, `x`, `y` va `z` ga aylantirish uchun `let` bilan pattern ishlatadi. Bu  *destruktura* deb ataladi, chunki u bitta tupleni uch qismga ajratadi. Nihoyat, dastur `y` qiymatini chop etadi, bu `6,4`.

Shuningdek, biz toʻgʻridan-toʻgʻri nuqta (`.`) va undan keyin kirishni xohlagan qiymat indeksidan foydalanib, tuple elementiga kirishimiz mumkin. Misol uchun:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-12-tuple-indexing/src/main.rs}}
```

Bu dastur `x` tuplesini yaratadi va soʻngra oʻz indekslari yordamida tuplening har bir elementiga kiradi. Koʻpgina dasturlash tillarida boʻlgani kabi, tupledagi birinchi indeks 0 ga teng.

Hech qanday qiymatsiz tuple maxsus nomga, *unit* ega. Bu qiymat va unga mos keladigan tur `()` yoziladi va boʻsh qiymat yoki boʻsh qaytish turini ifodalaydi. Ifodalar, agar ular boshqa qiymatni qaytarmasa, bilvosita birlik qiymatini qaytaradi.

#### Array Turi

Bir nechta qiymatlar toʻplamiga ega boʻlishning yana bir usuli *array*dir. Tupledan farqli oʻlaroq, arrayning har bir elementi bir xil turdagi boʻlishi kerak. Baʼzi boshqa tillardagi arraylardan farqli oʻlaroq, Rustdagi arraylar belgilangan uzunlikka ega.

Biz arraydagi qiymatlarni kvadrat qavslar ichida vergul bilan ajratilgan roʻyxat sifatida yozamiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-13-arrays/src/main.rs}}
```

Arraylar maʼlumotlaringizni toʻplamga emas, balki stekga ajratishni istasangiz foydali boʻladi (biz [4-bobda][stack-and-heap]<!-- ignore -->) stek va toʻplam haqida koʻproq gaplashamiz yoki sizda har doim maʼlum miqdordagi elementlar mavjudligini taʼminlashni istasangiz).
Array vektor turi kabi moslashuvchan emas. *Vektor* standart kutubxona tomonidan taqdim etilgan oʻxshash toʻplam turi boʻlib, uning hajmini oʻstirish yoki kichraytirishi mumkin. Agar array yoki vektordan foydalanishga ishonchingiz komil boʻlmasa, vektordan foydalanishingiz mumkin.
[8-bobda][vectors]<!-- ignore --> vektorlar batafsilroq muhokama qilinadi.

Biroq, agar elementlar sonini oʻzgartirish kerak boʻlmasligini bilsangiz, arraylar foydaliroq boʻladi. Misol uchun, agar siz dasturda oy nomlaridan foydalansangiz, vektordan koʻra massivdan foydalanar edingiz, chunki u har doim 12 ta elementdan iborat boʻlishini bilasiz:

```rust
let oylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul",
              "Avgust", "Setabr", "Oktabr", "Noyabr", "Dekabr"];
```

Siz har bir element turi, nuqta-vergul va arraydagi elementlar soni bilan kvadrat qavslar yordamida array turini yozasiz, masalan:

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

Bu erda `i32` har bir elementning turi. Nuqtali verguldan keyin `5` raqami array beshta elementdan iboratligini bildiradi.

Bundan tashqari, har bir element uchun bir xil qiymatni oʻz ichiga olgan arrayni boshlangʻich qiymatdan keyin nuqta-vergul qoʻyib, soʻngra bu yerda koʻrsatilgandek kvadrat qavs ichida array uzunligini belgilash orqali ishga tushirishingiz mumkin:

```rust
let a = [3; 5];
```

`a` nomli array dastlab `3` qiymatiga oʻrnatiladigan `5` elementni oʻz ichiga oladi. Bu `let a = [3, 3, 3, 3, 3];` yozish bilan bir xil, ammo qisqaroq tarzda.

##### Array elementlariga kirish

Array - bu stekda taqsimlanishi mumkin boʻlgan maʼlum, qatʼiy oʻlchamdagi xotiraning bitta boʻlagi. Siz indekslash yordamida array elementlariga kirishingiz mumkin, masalan:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-14-array-indexing/src/main.rs}}
```

Bu misolda `birinchi` deb nomlangan o‘zgaruvchi `1` qiymatini oladi, chunki bu arraydagi `[0]` indeksidagi qiymatdir. `ikkinchi` deb nomlangan ozgaruvchi arraydagi `[1]` indeksidan `2` qiymatini oladi.

##### Yaroqsiz Array elementlariga kirish

Keling, array oxiridan o‘tgan array elementiga kirishga harakat qilsangiz nima bo‘lishini ko‘rib chiqamiz. Aytaylik, foydalanuvchidan array indeksini olish uchun 2-bobdagi taxminiy o‘yinga o‘xshash ushbu kodni ishlatasiz:

<span class="filename">Fayl nomi: src/main.rs</span>

```rust,ignore,panics
{{#rustdoc_include ../listings/ch03-common-programming-concepts/no-listing-15-invalid-array-access/src/main.rs}}
```

Ushbu kod muvaffaqiyatli kompilyatsiya qilinadi.Agar siz ushbu kodni `cargo run` yordamida ishga tushirsangiz va `0`, `1`, `2`, `3` yoki `4` kiritsangiz, dastur arraydagi ushbu indeksdagi mos qiymatni chop etadi. Buning oʻrniga array oxiridan oʻtgan raqamni kiritsangiz, masalan, `10`, siz shunday chiqishni koʻrasiz:

<!-- manual-regeneration
cd listings/ch03-common-programming-concepts/no-listing-15-invalid-array-access
cargo run
10
-->

```console
thread 'mainʼ panicked at 'index out of bounds: the len is 5 but the index is 10', src/main.rs:19:19
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Dastur indekslash operatsiyasida yaroqsiz qiymatdan foydalanish nuqtasida *runtime* xatosiga olib keldi. Dastur xato xabari bilan chiqdi va yakuniy `println!` bayonotini bajarmadi. Indekslash yordamida elementga kirishga harakat qilganingizda, Rust siz koʻrsatgan indeks array uzunligidan kamroq ekanligini tekshiradi. Agar indeks uzunlikdan kattaroq yoki unga teng boʻlsa, Rust panic chiqaradi. Bu tekshirish runtimeda amalga oshirilishi kerak, ayniqsa bu holatda, chunki kompilyator foydalanuvchi kodni keyinroq ishga tushirganda qanday qiymat kiritishini bila olmaydi.

Bu Rustning xotira xavfsizligi tamoyillarining amaldagi namunasidir. Koʻpgina low-leveldagi tillarda bunday tekshirish amalga oshirilmaydi va notoʻgʻri indeksni taqdim etganingizda, yaroqsiz xotiraga kirish mumkin. Rust xotiraga kirishga ruxsat berish va davom ettirish oʻrniga darhol chiqish orqali sizni bunday xatolardan himoya qiladi. 9-bobda Rust-ning xatolarini qanday hal qilish va siz panic qoʻymaydigan va yaroqsiz xotiraga kirishga ruxsat bermaydigan oʻqilishi mumkin boʻlgan xavfsiz kodni qanday yozishingiz mumkinligi muhokama qilinadi.

[comparing-the-guess-to-the-secret-number]:
ch02-00-guessing-game-tutorial.html#comparing-the-guess-to-the-secret-number
[twos-complement]: https://en.wikipedia.org/wiki/Two%27s_complement
[control-flow]: ch03-05-control-flow.html#control-flow
[strings]: ch08-02-strings.html#storing-utf-8-encoded-text-with-strings
[stack-and-heap]: ch04-01-what-is-ownership.html#the-stack-and-the-heap
[vectors]: ch08-01-vectors.html
[unrecoverable-errors-with-panic]: ch09-01-unrecoverable-errors-with-panic.html
[appendix_b]: appendix-02-operators.md
