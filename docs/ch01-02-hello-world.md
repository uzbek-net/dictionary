## Hello, World!

Endi siz Rustni oʻrnatdingiz, hozir sizning birinchi Rust dasturingizni yozishning ayni vaqti.
Yangi dasturlash tilini oʻrganishda `Hello, World!` matnini ekranga chop etuvchi kichik va sodda
dastur tuzish anʼanaga aylangan, shunday ekan biz ham sinab koʻramiz!

> Eslatma: Bu kitob terminal bilan ishlay olishning boshlangʻich koʻnikmalarini
> talab qiladi. Rust sizning kod muxarriringiz foydalanadigan asboblaringiz va
> kodingizni qayerda joylayishi boʻyicha talablar qoʻymaydi, shuning uchun agar siz
> terminal oʻrniga integratsiyalashgan ishlab chiqish muhitidan (IDE) foydalanishni afzal koʻrsangiz,
> oʻzingizning sevimli IDE-dan foydalaning. Koʻpgina IDElar endi maʼlum darajada
> Rust-ni qoʻllab-quvvatlaydi; tafsilotlar uchun IDE hujjatlarini tekshiring.
> Rust jamoasi `rust-analyzer` orqali ajoyib IDE yordamini taʼminlashga eʼtibor qaratdi.
> Batafsil ma’lumot uchun [D ilovasi][devtools]<!-- ignore -->ni koʻzdan kechiring.

### Loyiha jildini yaratish

Siz ishni Rust kodingizni joylaytirish uchun jild yaratishdan boshlaysiz.
Rust uchun sizning kodingiz qayerda joylashining ahamiyati yoʻq, lekin biz
bu kitobdagi mashq va loyihalarni joylash uchun *projects* nomli jild yaratishingizni
maslahat beramiz.

Terminalni oching va *projects* jildini yaratish va uning ichidan “Hello, world!” loyihasi
jildini yaratish uchun quyidagi buyruqlarni kiriting.

Linux, macOS va Windows Powershell uchun:

```console
$ mkdir ~/projects
$ cd ~/projects
$ mkdir hello_world
$ cd hello_world
```

Windows CMD uchun:

```cmd
> mkdir "%USERPROFILE%\projects"
> cd /d "%USERPROFILE%\projects"
> mkdir hello_world
> cd hello_world
```

### Rust dasturi yozish va ishga tushirish.

Endi, *main.rs* nomli yangi fayl yarating. Rust kodlar har doim *.rs* kengaytmasi
bilan tugaydi. Agar fayl nomida bir nechta soʻzlardan foydalansangiz, ularni ajratish uchun pastki chiziqdan foydalanish shart. Masalan, *helloworld.rs* oʻrniga *hello_world.rs* dan foydalaning.

Endi hozirgina yaratgan *main.rs* faylingizni kod muharririda oching.

<span class="filename">Fayl nomi: main.rs</span>

```rust
fn main() {
    println!("Hello, world!");
}
```

<span class="caption">Roʻyxat 1-1: `Hello, world!` ni chop etuvchi dastur</span>

Faylni saqlang va Terminalda *~/projects/hello_world* jildiga qayting.
Linux yoki macOS da faylni kompilyatsiya qilish va ishga tushirish uchun quyidagi buyruqlarni kiriting:

```console
$ rustc main.rs
$ ./main
Hello, world!
```

Windowsda `./main` ning oʻrniga `.\main.exe` buyrugʻini kiriting:

```powershell
> rustc main.rs
> .\main.exe
Hello, world!
```
Operatsion tizimingizdan qatʼi nazar, terminalda `Hello, world!` qatori chop etilishi kerak.Agar siz ushbu chiqishni koʻrmasangiz, yordam olish usullari uchun Oʻrnatish boʻlimining [”Muammolarni bartaraf etish”][troubleshooting]<!-- ignore --> boʻlimiga qayting.

Agar `Hello, world!` chop etilgan boʻlsa, tabriklaymiz! Siz rasmiy ravishda Rust dasturini yozdingiz. Bu sizni Rust dasturchisiga aylantiradi - xush kelibsiz!

### Rust dasturining tuzilishi.

Keling "Hello, world!" dasturiga chuqurroq nazar solamiz. Boshqotirmaning 1-qismi:

```rust
fn main() {

}
```

Bu qatorlar `main` nomli funksiyani eʼlon qiladi. `main` funksiyasi alohida: u har doim bajariladigan Rust dasturida ishlaydigan birinchi koddir. Bu yerda birinchi satr hech qanday parametrga ega boʻlmagan va hech narsani qaytarmaydigan `main` funksiyasini eʼlon qiladi.
Agar parametrlar mavjud boʻlsa, ular `()` qavslar ichiga kiradi.

Funksiyasing tanasi `{}` bilan oʻralgan. Rust har bir funksiyalarda eʼlon qilishda
`{}` dan foydalanishni talab qiladi.

> Eslatma: Agar siz Rust loyihalarda standart usulda kod yozmoqchi boʻlsangiz
> kodingizni maʼlum bir uslubda formatlash uchun `rustfmt` nomli avtomatik formatlash vositasidan
> foydalanishingiz mumkin (batafsilroq `rustfmt` [D ilovasi][devtools]<!-- ignore --> -da)
> Rust jamoasi ushbu vositani standart Rust distributiviga kiritdi,
> chunki `rustc` kabi, u allaqachon kompyuteringizga oʻrnatilgan boʻlishi kerak!

`main` funksiyaning tanasi quyidagi kodni oʻz ichiga oladi:

```rust
    println!("Hello, world!");
```

Shu bir qator kod shu kichik dasturdagi barcha ishni amalga oshiardi: u
matnni ekranga chop etadi.Bu yerda ahamiyat qaratish zarur boʻlgan
toʻrtta muhim narsalar bor.

<!-- Birinchidan, Rust stili 4ta boʻsh joydan iborat 1ta tabdan emas. -->
Birinchidan, Rust style toʻrtta boʻshliqdan iborat tab emas

Ikkinchidan, `println!` Rust makrosini chaqiradi. Agar u funktsiyani oʻrniga chaqirgan boʻlsa, u `println` (`!` belgisiz) sifatida kiritiladi. Biz Rust makrolari haqida 19-bobda batafsilroq muhokama qilamiz.Hozircha siz shuni bilishingiz kerakki, `!` belgisidan foydalanish oddiy funksiya o‘rniga makrosni chaqirayotganingizni anglatadi va makrolar har doim ham funksiyalar bilan bir xil qoidalarga amal qilmaydi.

Uchinchidan, siz `"Hello, world!"` qatorini koʻrasiz. Bu satrni argument sifatida `println!` ga uzatamiz va satr ekranga chop etiladi.

Toʻrtinchidan, satrni nuqtali vergul (`;`) bilan tugatamiz, bu esa bu ifoda tugaganligini va keyingisi boshlashga tayyorligini bildiradi. Rust kodining aksariyat satrlari nuqtali vergul bilan tugaydi.


### Kompilyatsiya va ishga tushirish alohida bosqichlardir

Siz yangi yaratilgan dasturni ishga tushirdingiz, shuning uchun jarayonning har bir bosqichini koʻrib chiqamiz.

Rust dasturini ishga tushirishdan oldin uni Rust kompilyatoridan foydalanib, `rustc` buyrug‘ini kiritib, unga manba faylingiz nomini quyidagi tarzda kiritishingiz kerak:

```console
$ rustc main.rs
```

Agar siz C yoki C++ bilan ishlagan boʻlsangiz, bu `gcc` yoki `clang` ga oʻxshashligini sezasiz. Muvaffaqiyatli kompilyatsiyadan soʻng Rust binary bajariladigan faylni chiqaradi.

Linux, macOS va Windows-dagi PowerShell-da siz shelldagi `ls` buyrugʻini kiritish orqali bajariladigan faylni koʻrishingiz mumkin:


```console
$ ls
main  main.rs
```

Linux va macOS-da siz ikkita faylni koʻrasiz. Windows-dagi PowerShell bilan siz CMD-dan foydalangan holda koʻrgan uchta faylni koʻrasiz. Windows-da CMD bilan siz quyidagilarni kiritasiz:


```cmd
> dir /B %= the /B faqat fayl nomlarini koʻrsatishni aytadi =%
main.exe
main.pdb
main.rs
```

Bu sizga *.rs* kengaytmali kod faylini, bajariluvchi faylni(Windowsda `main.exe`
boshqa barcha tizimlarda `main`), va Windowsdan foydalanayotganingizda, debugging 
maʼlumotlarini oʻz ichida saqlovchi *.pdb* kengaytmali faylni koʻrsatadi.

Bu yerdan siz *main* yoki *main.exe* faylini ishga tushirasiz, masalan:

```console
$ ./main # or .\Windows-da main.exe
```

Agar sizning *main.rs* faylingiz “Hello, world!” dasturi boʻlsa, bu dastur
ekranga `Hello, world!` matnini chop etadi.

Agar siz Ruby, Python yoki JavaScript kabi dinamik tilni yaxshi bilsangiz, dasturni alohida bosqichlar sifatida kompilyatsiya qilish va ishga tushirishga odatlanmagan boʻlishingiz mumkin. Rust - bu oldindan tuzilgan kompilyatsiya tili, yaʼni siz dasturni kompilyatsiya qilishingiz va bajariladigan faylni boshqa birovga berishingiz mumkin va ular Rustni oʻrnatmasdan ham uni ishga tushirishlari mumkin.Agar siz kimgadir *.rb*, *.py* yoki *.js* faylini bersangiz, ularda Ruby, Python yoki JavaScript ilovasi oʻrnatilgan boʻlishi kerak (mos ravishda). Ammo bu tillarda dasturni kompilyatsiya qilish va ishga tushirish uchun faqat bitta buyruq kerak boʻladi. Til dizaynida hamma narsa oʻzaro kelishuvdir.

Oddiy dasturlar uchun `rustc` bilan kompilyatsiya qilish juda mos keladi, lekin loyihangiz oʻsib borishi bilan siz barcha variantlarni boshqarishni va kodingizni almashishni osonlashtirishni xohlaysiz.
Endi, biz siz bilan haqiqiy Rust dasturlarini tuzishda qulaylik yaratuvchi
Cargo yordamchisi bilan tanishamiz.

[troubleshooting]: ch01-01-installation.html#troubleshooting
[devtools]: appendix-04-useful-development-tools.md
