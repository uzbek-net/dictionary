## Oʻrnatish

Birinchi qadam Rustni oʻrnatishdir.Rustni Rust versiyalari va tegishli vositalarni boshqarish uchun buyruq qatori vositasi bo‘lgan `rustup` orqali yuklab olamiz. Yuklab olish uchun sizga internet ulanishi kerak boʻladi.

> Eslatma: Agar biron sababga koʻra `rustup` dan foydalanmaslikni xohlasangiz, boshqa variantlar uchun
> [Rustni oʻrnatishning boshqa usullari][otherinstall] sahifasiga qarang.

Quyidagi qadamlar Rust kompilyatorining soʻnggi barqaror versiyasini oʻrnatadi.
Rustning barqarorligi kafolati kitobdagi kompilyatsiya qilingan barcha misollar Rustning yangi versiyalari bilan kompilyatsiya qilishda davom etishini taʼminlaydi. Chiqish versiyalar orasida biroz farq qilishi mumkin, chunki Rust koʻpincha xato xabarlari va ogohlantirishlarni yaxshilaydi. Boshqacha qilib aytadigan boʻlsak, ushbu qadamlar yordamida oʻrnatgan har qanday yangi, barqaror Rust versiyasi ushbu kitob mazmuni bilan kutilganidek ishlashi kerak.

> ### Buyruqlar qatori yozuvi
>
> Ushbu bobda va butun kitobda biz terminalda ishlatiladigan baʼzi buyruqlarni koʻrsatamiz.
> Terminalga kiritishingiz kerak boʻlgan barcha qatorlar `$` bilan boshlanadi.
> `$` belgisini kiritishingiz shart emas; bu har bir buyruqning boshlanishini koʻrsatish
> uchun koʻrsatilgan buyruq qatori. `$` bilan boshlanmagan qatorlar odatda oldingi buyruqning
> natijasini koʻrsatadi. Bundan tashqari, PowerShell-ga xos misollarda `$` emas, `>` ishlatiladi.

### Linux yoki macOS-ga  `rustup` oʻrnatish

Agar siz Linux yoki macOS dan foydalansangiz, terminalni oching va quyidagi buyruqni kiriting:

```console
$ curl --proto '=httpsʼ --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

Buyruq skriptni yuklab oladi va Rustning eng soʻnggi barqaror versiyasini oʻrnatadigan `rustup` vositasini oʻrnatishni boshlaydi. Sizdan parol soʻralishi mumkin. Oʻrnatish muvaffaqiyatli boʻlsa, quyidagi qator paydo boʻladi:

```text
Rust is installed now. Great!
```

Shuningdek, sizga  *linker*, kerak boʻladi, yaʼni Rust oʻzining kompilyatsiya qilingan natijalarini bitta faylga birlashtirish uchun foydalanadigan dastur. Ehtimol,bu sizda allaqachon mavjud. Agar linker xatolarga duch kelsangiz, odatda linkerni oʻz ichiga olgan C kompilyatorini oʻrnatishingiz kerak. C kompilyatori ham foydalidir, chunki baʼzi umumiy Rust paketlari C kodiga bogʻliq va C kompilyatoriga muhtoj boʻladi.

MacOS-da siz C kompilyatorini ishga tushirish orqali olishingiz mumkin:

```console
$ xcode-select --install
```

Linux foydalanuvchilari odatda distributiv texnik hujjatlariga muvofiq GCC yoki Clang oʻrnatishlari kerak. Misol uchun, agar siz Ubuntuʼdan foydalansangiz, `build-essential` paketini oʻrnatishingiz mumkin.

### Windows-ga `rustup` oʻrnatish

Windows tizimida [https://www.rust-lang.org/tools/install][install] saytiga oʻting va Rustni oʻrnatish boʻyicha koʻrsatmalarga amal qiling. Oʻrnatishning bir nuqtasida sizga Visual Studio 2013 yoki undan keyingi versiyalari uchun MSVC yaratish vositalari kerakligi haqida xabar keladi.

Build toolsini olish uchun [Visual Studio 2022][visualstudio] ni oʻrnatishingiz kerak boʻladi. Qaysi ish dasturlarini oʻrnatish kerakligi soʻralganda, quyidagilarni  kiriting:

* “Desktop Development with C++”
* TWindows 10 yoki 11 SDK
* Ingliz tili toʻplami komponenti va siz tanlagan boshqa tillar toʻplami

Ushbu kitobning qolgan qismi *cmd.exe* va PowerShell da ishlaydigan buyruqlardan foydalanadi.
Agar aniq farqlar boʻlsa, qaysi birini ishlatishni tushuntiramiz.

### Muammolarni bartaraf etish

Rust toʻgʻri oʻrnatilganligini tekshirish uchun shellni oching va quyidagi qatorni kiriting:

```console
$ rustc --version
```

Quyidagi formatda chiqarilgan so‘nggi barqaror versiya uchun versiya raqami, xesh va tasdiqlangan sanani ko‘rishingiz kerak:

```text
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

Agar siz ushbu maʼlumotni koʻrsangiz, Rustni muvaffaqiyatli oʻrnatdingiz! Agar siz ushbu maʼlumotni koʻrmasangiz, Rust `%PATH%` tizim oʻzgaruvchingizda quyidagi tarzda ekanligini tekshiring.

Windows CMD-da quyidagilardan foydalaning:

```console
> echo %PATH%
```

PowerShell-da foydalaning:

```powershell
> echo $env:Path
```

Linux va macOS-da quyidagilardan foydalaning:

```console
$ echo $PATH
```

Agar hammasi toʻgʻri boʻlsa va Rust hali ham ishlamasa, yordam olishingiz mumkin boʻlgan bir qancha joylar mavjud. Boshqa Rustaceanlar (biz oʻzimizni chaqiradigan ahmoqona taxallus) bilan qanday bogʻlanishni [hamjamiyat sahifasida][community] bilib oling.

### Yangilash va oʻchirish

Rust `rustup` orqali oʻrnatilgandan soʻng, yangi chiqarilgan versiyaga yangilash oson. Shelldan quyidagi yangilash skriptini ishga tushiring:

```console
$ rustup update
```

Rust va  `rustup`-ni oʻchirish uchun shelldan quyidagi oʻchirish skriptini ishga tushiring:

```console
$ rustup self uninstall
```

### Mahalliy texnik hujjatlar

Rust-ning oʻrnatilishi texnik hujjatlarning mahalliy nusxasini ham oʻz ichiga oladi, shunda siz uni oflayn rejimda oʻqishingiz mumkin. Brauzeringizda mahalliy texnik hujjatlarni ochish uchun `rustup doc` dasturini ishga tushiring.

Istalgan vaqtda standart kutubxona tomonidan tur yoki funksiya taqdim etilsa va siz u nima qilishini yoki undan qanday foydalanishni bilmasangiz, bilish uchun amaliy dasturlash interfeysi (API) texnik hujjatlaridan foydalaning!

[otherinstall]: https://forge.rust-lang.org/infra/other-installation-methods.html
[install]: https://www.rust-lang.org/tools/install
[visualstudio]: https://visualstudio.microsoft.com/downloads/
[community]: https://www.rust-lang.org/community
