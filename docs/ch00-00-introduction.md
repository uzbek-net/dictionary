# Kirish

> Eslatma: Kitobning ushbu nashri [No Starch Press][nsp]-dan bosma va elektron kitob formatida mavjud boʻlgan
> [Rust dasturlash tili][nsprust] bilan bir xil.

[nsprust]: https://nostarch.com/rust-programming-language-2nd-edition
[nsp]: https://nostarch.com/

*Rust dasturlash tili*ga xush kelibsiz, Rust haqida kirish kitobi.
Rust dasturlash tili tezroq va ishonchli dasturlarni yozishga yordam beradi.
Yuqori darajadagi samaradorlik va low-leveldagi boshqaruv koʻpincha dasturlash tilini loyihalashda bir-biriga zid keladi; Rust bu ziddiyatga qarshi turadi. Kuchli texnik imkoniyatlar va ishlab chiquvchilarning ajoyib tajribasini muvozanatlash orqali Rust sizga anʼanaviy ravishda bunday nazorat bilan bogʻliq boʻlgan barcha qiyinchiliklarsiz low-leveldagi tafsilotlarni (masalan, xotiradan foydalanish) boshqarish imkoniyatini beradi.

## Rust kim uchun

Rust turli sabablarga koʻra koʻp odamlar uchun idealdir. Keling, eng muhim guruhlarning bir nechtasini koʻrib chiqaylik.

### Dasturchilar jamoalari

Rust turli darajadagi tizimlarni dasturlash boʻyicha bilimga ega boʻlgan yirik ishlab chiquvchilar guruhlari oʻrtasida hamkorlik qilish uchun samarali vosita ekanligini isbotlamoqda. Low-leveldagi kod turli xil nozik xatolarga moyil boʻlib, koʻpchilik boshqa tillarda ularni faqat keng koʻlamli sinov va tajribali ishlab chiquvchilar tomonidan sinchkovlik bilan tekshirish orqali aniqlash mumkin.Rust-da kompilyator ushbu qiyin xatolar, jumladan, parallellik xatolari bilan kodni kompilyatsiya qilishni rad etib, darvozabon rolini oʻynaydi. Kompilyator bilan birga ishlash orqali jamoa xatolarni taʼqib qilishdan koʻra, vaqtini dastur mantigʻiga qaratishga sarflashi mumkin.

Rust shuningdek, tizim dasturlash dunyosiga zamonaviy ishlab chiquvchilar vositalarini olib keladi:

* Cargo  dependency menejeri va build toolni oʻz ichiga oladi, Rust ekotizimida bogʻliqliklarni qoʻshish, kompilyatsiya qilish va boshqarishni qiyinchiliksiz va davomli qiladi.
* Rustfmt formatlash vositasi ishlab chiquvchilar orasida barqaror kodlash uslubini taʼminlaydi.
* Rust Language Server kodni toʻldirish va inline xato xabarlari uchun Integrated Development Environment (IDE) integratsiyasini quvvatlaydi.

Rust ekotizimidagi ushbu va boshqa vositalardan foydalangan holda, ishlab chiquvchilar tizim darajasidagi kodni yozishda samarali boʻlishi mumkin.

### Talabalar

Rust talabalar va tizim tushunchalarini oʻrganishga qiziquvchilar uchun. Rust-dan foydalanib, koʻp odamlar operatsion tizimlarni ishlab chiqish kabi mavzular haqida bilib oldilar. Jamiyat juda mehmondoʻst va talabalar savollariga javob berishdan xursand. Ushbu kitob kabi saʼy-harakatlar orqali Rust guruhlari tizim tushunchalarini koʻproq odamlar, ayniqsa dasturlash uchun yangi boʻlganlar uchun qulayroq qilishni xohlashadi.

### Kompaniyalar

Yuzlab yirik va kichik kompaniyalar ishlab chiqarishda Rust-dan CLI dasturlar, veb-xizmatlar, DevOps toollari, embedded qurilmalar, audio va video tahlillari va transkodlar, kriptovalyutalar, bioinformatika, qidiruv tizimlari, Internet of Things ilovalari kabi turli vazifalar uchun foydalanadilar. , machine learning va hatto Firefox veb-brauzerining asosiy qismlari.

### Open Source dasturchilar

Rust Rust dasturlash tilini, hamjamiyatini, ishlab chiquvchilar vositalarini va kutubxonalarini yaratmoqchi boʻlgan odamlar uchundir. Rust tiliga oʻz hissangizni qoʻshishingizni istardik.

### Tezlik va barqarorlikni qadrlaydigan odamlar

Rust dasturlash tili tezlik va barqarorlikni xohlaydigan odamlar uchundir. Tezlik deganda biz Rust kodi qanchalik tez ishlashini va Rust sizga dasturlar yozish imkonini beradigan tezligini nazarda tutamiz. Rust kompilyatorining tekshiruvlari qoʻshimcha funksiyalar va refaktoring orqali barqarorlikni taʼminlaydi. Bu ishlab chiquvchilar koʻpincha oʻzgartirishdan qoʻrqadigan ushbu tekshiruvlarsiz tillardagi moʻrt eski koddan farqli oʻlaroq. Nol xarajatli abstraktsiyalarga, qoʻlda yozilgan kod kabi tezroq lower-leveldagi kodni kompilyatsiya qiladigan higher-leveldagi funktsiyalarga intilish orqali Rust xavfsiz kodni ham tezkor kod qilishga intiladi.

Rust tili boshqa koʻplab foydalanuvchilarni ham qoʻllab-quvvatlashga umid qiladi; Bu yerda tilga olinganlar faqat eng katta manfaatdor tomonlardan biri hisoblanadi. Umuman olganda, Rustning eng katta ambitsiyalari xavfsizlik *va* unumdorlik, tezlik *va* samaradorlikni taʼminlash orqali dasturchilar oʻnlab yillar davomida qabul qilgan kelishuvlarni yoʻq qilishdir. Rust-ni sinab koʻring va uning tanlovlari sizga mos keladimi yoki yoʻqligini tekshiring.

## Bu kitob kim uchun

Ushbu kitobda siz boshqa dasturlash tilida kod yozgansiz deb taxmin qilinadi, lekin qaysi biri haqida hech qanday taxminlar yoʻq. Biz materialni turli xil dasturlash tajribasiga ega boʻlganlar uchun keng foydalanishga harakat qildik. Biz dasturlash nima ekanligi yoki u haqida qanday fikr yuritish haqida gapirishga koʻp vaqt sarflamaymiz. Agar siz dasturlashda mutlaqo yangi boʻlsangiz, dasturlash bilan tanishishni taʼminlaydigan kitobni oʻqisangiz yaxshi boʻlardi.

## Ushbu kitobdan qanday foydalanish kerak

Umuman olganda, bu kitob siz uni oldindan orqaga ketma-ket oʻqiyotganingizni taxmin qiladi. Keyingi boblar oldingi boblardagi tushunchalarga asoslanadi va oldingi boblar maʼlum bir mavzu boʻyicha tafsilotlarni oʻrganmasligi mumkin, lekin keyingi bobda mavzuni qayta koʻrib chiqadi.

Ushbu kitobda siz ikki xil boʻlimni topasiz: kontseptsiya boʻlimlari va loyiha boʻlimlari. Kontseptsiya boblarida siz Rustning bir tomoni haqida bilib olasiz. Loyiha boʻlimlarida biz hozirgacha oʻrganganlaringizni qoʻllagan holda kichik dasturlarni birgalikda tuzamiz. 2, 12 va 20-boblar loyiha boblari; qolganlari kontseptsiya boblari.

1-bobda Rustni qanday oʻrnatish, "Hello, world!" dasturi va Cargo, Rust paket menejeri va build tooldan qanday foydalanishni koʻrib chiqamiz. 2-bob Rustda dastur yozish boʻyicha amaliy kirish boʻlib, siz raqamlarni taxmin qilish oʻyinini tuzasiz. Bu yerda biz tushunchalarni yuqori darajada yoritamiz va keyingi boblarda qoʻshimcha tafsilotlar beriladi. Agar siz darhol qoʻllaringizni ifloslantirmoqchi boʻlsangiz, 2-bob buning uchun joy. 3-bobda boshqa dasturlash tillariga oʻxshash Rust funksiyalari yoritilgan va 4-bobda siz Rustning ownershp tizimi haqida bilib olasiz. Agar siz keyingisiga o‘tishdan oldin har bir tafsilotni o‘rganishni ma’qul ko‘radigan, ayniqsa sinchkov o‘quvchi bo‘lsangiz, 2-bobni o‘tkazib yuborib, to‘g‘ridan-to‘g‘ri 3-bobga o‘tishingiz va loyiha ustida ishlashni hohlaganingizda 2-bobga qaytishingiz mumkin. siz oʻrgangan tafsilotlar.

5-bobda structlar va metodlar muhokama qilinadi, 6-bob esa enumlar, `match` expressionlari va `if let` control flow konstruksiyasini qamrab oladi. Rust-da maxsus turlarni yaratish uchun struclar va enumlardan foydalanasiz.

7-bobda siz Rust modul tizimi va kodingizni va uning umumiy amaliy dasturlash interfeysini (API) tashkil qilish uchun maxfiylik qoidalari haqida bilib olasiz. 8-bobda standart kutubxona taqdim etadigan vektorlar, stringlar va hash maplar kabi umumiy yigʻish maʼlumotlar tuzilmalari muhokama qilinadi. 9-bob Rustning xatolarni hal qilish falsafasi va usullarini oʻrganadi.

10-bob generiklar, traitlar va lifetimeni oʻrganadi, bu sizga bir nechta turlarga tegishli kodni aniqlash imkoniyatini beradi. 11-bob sinovdan oʻtadi, bu hatto Rustning xavfsizlik kafolatlari bilan ham dasturingiz mantigʻining toʻgʻriligini taʼminlash uchun zarurdir. 12-bobda biz fayllar ichidagi matnni qidiradigan `grep` buyruq qatori vositasidan oʻzimizning funksiyalar toʻplamini yaratamiz. Buning uchun biz oldingi boblarda muhokama qilgan koʻplab tushunchalardan foydalanamiz.

13-bob yopilishlar va iteratorlarni oʻrganadi: Rustning funktsional dasturlash tillaridan kelib chiqadigan xususiyatlari. 14-bobda biz Cargolarni chuqurroq koʻrib chiqamiz va kutubxonalaringizni boshqalar bilan baham koʻrishning eng yaxshi amaliyotlari haqida gaplashamiz.
15-bobda standart kutubxona taqdim etadigan smart pointerlar va ularning funksionalligini taʼminlaydigan traitlar muhokama qilinadi.

16-bobda biz bir vaqtning oʻzida dasturlashning turli modellarini koʻrib chiqamiz va Rust sizga bir nechta mavzularda qoʻrqmasdan dasturlashda qanday yordam berishi haqida gaplashamiz.
17-bobda Rust idiomlari sizga tanish boʻlishi mumkin boʻlgan obyektga yoʻnaltirilgan(OOP) dasturlash tamoyillari bilan qanday taqqoslanishi koʻrib chiqiladi.

18-bobda Rust dasturlari boʻylab gʻoyalarni ifodalashning kuchli usullari boʻlgan patternlar va patternlarni moslashtirish haqida maʼlumot berilgan. 19-bobda ilgʻor qiziqarli mavzular, jumladan xavfli Rust, makroslar va boshqa koʻp narsalar mavjud.

20-bobda biz low-leveldagi koʻp tarmoqli veb-serverni amalga oshiradigan loyihani yakunlaymiz!

Va nihoyat, baʼzi qoʻshimchalarda til haqida foydali maʼlumotlar koʻproq mos yozuvlar formatida mavjud. A ilovasida Rustning kalit soʻzlari, B ilovasida Rust operatorlari va belgilari, C ilovasi standart kutubxona tomonidan taqdim etilgan hosila traitlarini oʻz ichiga oladi, D ilovasi baʼzi foydali ishlab chiqish vositalarini qamrab oladi va E ilovasida Rust nashrlari tushuntiriladi. F ilovasida siz kitobning tarjimalarini topishingiz mumkin, G ilovasida esa Rust qanday qilinganligi va  nightlyli Rust nima ekanligini koʻrib chiqamiz.

Ushbu kitobni oʻqishning notoʻgʻri usuli yoʻq: agar siz oldinga oʻtmoqchi boʻlsangiz, unga boring! Agar chalkashliklarga duch kelsangiz, avvalgi boblarga qaytishingiz kerak boʻlishi mumkin. Lekin siz uchun nima ish qilsa, shuni qiling.

<span id="ferris"></span>

Rustni oʻrganish jarayonining muhim qismi kompilyator koʻrsatadigan xato xabarlarini oʻqishni oʻrganishdir: ular sizni ish kodiga yoʻnaltiradi.
Shunday qilib, biz kompilyator har bir vaziyatda sizga koʻrsatadigan xato xabari bilan birga kompilyatsiya qilinmaydigan koʻplab misollarni keltiramiz. Bilingki, agar siz tasodifiy misol kiritsangiz va ishlatsangiz, u kompilyatsiya qilinmasligi mumkin! Ishlamoqchi boʻlgan misol xato uchun moʻljallanganligini bilish uchun atrofdagi matnni oʻqiganingizga ishonch hosil qiling. Ferris, shuningdek, ishlash uchun moʻljallanmagan kodni ajratishga yordam beradi:

| Ferris                                                                                                           | Maʼnosi                                         |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <img src="img/ferris/does_not_compile.svg" class="ferris-explain" alt="Ferris with a question mark"/>            | Bu kod kompilyatsiya qilinmaydi!                      |
| <img src="img/ferris/panics.svg" class="ferris-explain" alt="Ferris throwing up their hands"/>                   | Bu kod panic!                                |
| <img src="img/ferris/not_desired_behavior.svg" class="ferris-explain" alt="Ferris with one claw up, shrugging"/> | Ushbu kod kerakli xatti-harakatni keltirib chiqarmaydi. |

Aksariyat hollarda biz sizni kompilyatsiya qilinmagan har qanday kodning toʻgʻri versiyasiga olib boramiz.

## Manba kodi

Ushbu kitob yaratilgan manba fayllarni [GitHub][book]da topish mumkin.

[book]: https://github.com/rust-lang/book/tree/main/src
