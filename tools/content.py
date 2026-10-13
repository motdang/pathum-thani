"""Pathum Thani page words. Facts come from research/facts.json (each with its source, read 2026-10-13); the frame is in content_frame.py."""
from content_frame import BANDS, HOLIDAYS, NAV, PICS, SITE, SOON, TOYS, WORDS  # noqa: F401

MOC = "https://pathumthani.moc.go.th/th/content/page/index/id/1055"
MOC_N = "Pathum Thani provincial profile, Ministry of Commerce"
THW = "https://th.wikipedia.org/wiki/"
ENW = "https://en.wikipedia.org/wiki/"
SAMKHOK = THW + "อำเภอสามโคก"
RANGSIT = ENW + "Rangsit_Canal"
NAEWNA = "https://www.naewna.com/lady/519506"


def b(en, th):
    return {"en": en, "th": th}


TLDR = [
    b("<b>Where:</b> the province just north of Bangkok, 27.8 km up Phahonyothin Road. The Chao Phraya runs 30 km through it.",
      "<b>อยู่ไหน:</b> จังหวัดติดกรุงเทพฯ ด้านเหนือ ไปตามถนนพหลโยธิน 27.8 กิโลเมตร แม่น้ำเจ้าพระยาไหลผ่าน 30 กิโลเมตร"),
    b("<b>The name:</b> “city of lotus”. King Rama II gave it in 1815, after the Mon of Sam Khok met him with lotus flowers.",
      "<b>ชื่อ:</b> “เมืองแห่งดอกบัว” รัชกาลที่ 2 พระราชทานเมื่อ พ.ศ. 2358 หลังชาวมอญสามโคกถวายดอกบัวรับเสด็จ"),
    b("<b>Mon roots:</b> Mon families from Burma settled at Sam Khok around 1660 and again in 1774. Sam Khok is still the most Mon district.",
      "<b>รากมอญ:</b> ชาวมอญอพยพมาตั้งบ้านที่สามโคกราว พ.ศ. 2203 และอีกครั้ง พ.ศ. 2317 สามโคกยังเป็นอำเภอที่มีชาวมอญหนาแน่นที่สุด"),
    b("<b>Canals:</b> Khlong Rangsit, dug from 1890, was Siam's first irrigation project. It turned the Rangsit swamps into rice fields. The province has about 84 canals.",
      "<b>คลอง:</b> คลองรังสิต เริ่มขุด พ.ศ. 2433 เป็นโครงการชลประทานแห่งแรกของสยาม เปลี่ยนทุ่งรังสิตเป็นนาข้าว ทั้งจังหวัดมีคลองราว 84 สาย"),
    b("<b>Now:</b> 1.24 million people; factories make nearly half the province's output. Talat Thai, Thailand's largest market, the Asian Institute of Technology and the National Science Museum are here.",
      "<b>วันนี้:</b> ประชากร 1.24 ล้านคน อุตสาหกรรมเกือบครึ่งของเศรษฐกิจจังหวัด มีตลาดไทซึ่งใหญ่ที่สุดในประเทศ สถาบันเทคโนโลยีแห่งเอเชีย และพิพิธภัณฑ์วิทยาศาสตร์แห่งชาติ"),
    b("<b>Eat:</b> boat noodles on the Rangsit–Nakhon Nayok road, Mon khao chae at Songkran, kalamae, river prawns, Pathum Thani fragrant rice.",
      "<b>กิน:</b> ก๋วยเตี๋ยวเรือสายรังสิต–นครนายก ข้าวแช่มอญช่วงสงกรานต์ กาละแม กุ้งแม่น้ำเผา ข้าวหอมปทุมธานี"),
    b("<b>See:</b> openbill storks at Wat Phai Lom, the shell chedis of Wat Chedi Hoi, alms by boat on the river after Ok Phansa.",
      "<b>ดู:</b> นกปากห่างวัดไผ่ล้อม เจดีย์หอยวัดเจดีย์หอย ตักบาตรพระร้อยทางเรือหลังออกพรรษา"),
]

NUMBERS = [
    {"v": "1,525.9", "l": b("square kilometres", "ตารางกิโลเมตร"), "src": MOC, "src_name": MOC_N},
    {"v": "1,236,471", "l": b("people, 2024", "คน พ.ศ. 2567"), "src": ENW + "Pathum_Thani_province", "src_name": "Wikipedia: Pathum Thani province"},
    {"v": "7 · 60", "l": b("districts · subdistricts", "อำเภอ · ตำบล"), "src": THW + "จังหวัดปทุมธานี", "src_name": "วิกิพีเดีย: จังหวัดปทุมธานี"},
    {"v": "27.8 km", "l": b("to Bangkok by Highway 1", "ถึงกรุงเทพฯ ทางหลวงหมายเลข 1"), "src": MOC, "src_name": MOC_N},
    {"v": "84", "l": b("canals, 1,062 km of them", "คลอง ยาวรวม 1,062 กม."), "src": MOC, "src_name": MOC_N},
    {"v": "56 km", "l": b("Khlong Rangsit, dug from 1890", "คลองรังสิต ขุด พ.ศ. 2433"), "src": THW + "คลองรังสิตประยูรศักดิ์", "src_name": "วิกิพีเดีย: คลองรังสิตประยูรศักดิ์"},
    {"v": "542 rai", "l": b("Talat Thai, 21 markets in one", "ตลาดไท 21 ตลาดย่อย"), "src": THW + "ตลาดไท", "src_name": "วิกิพีเดีย: ตลาดไท"},
    {"v": "84,788", "l": b("openbill storks counted, 1996", "นกปากห่างที่นับได้ พ.ศ. 2539"), "src": MOC, "src_name": MOC_N},
]
for n in NUMBERS:
    n["v"] = n["v"]

TIMELINE = [
    {"y": b("1569", "2112"), "text": b("The first Sam Khok town, at Wat Phaya Mueang, empties after Ayutthaya falls.", "เมืองสามโคกแห่งแรกที่วัดพญาเมืองร้างไปหลังกรุงศรีอยุธยาเสียกรุง"), "src": SAMKHOK, "src_name": "วิกิพีเดีย: อำเภอสามโคก"},
    {"y": b("c. 1660", "ราว 2203"), "text": b("Saming Poe leads Mon refugees from Mottama to Ban Sam Khok; King Narai gives them the land.", "สมิงเปอนำชาวมอญจากเมาะตะมะมาตั้งบ้านที่บ้านสามโคก สมเด็จพระนารายณ์พระราชทานที่ดิน"), "src": SAMKHOK, "src_name": "วิกิพีเดีย: อำเภอสามโคก"},
    {"y": b("1667", "2210"), "text": b("Wat Sing, on the river at Sam Khok, receives its consecrated boundary.", "วัดสิงห์ริมเจ้าพระยาได้รับพระราชทานวิสุงคามสีมา"), "src": THW + "วัดสิงห์_(จังหวัดปทุมธานี)", "src_name": "วิกิพีเดีย: วัดสิงห์"},
    {"y": b("1726", "2269"), "text": b("A Dutch map marks Sam Khok as a pottery-making village.", "แผนที่ดัตช์ระบุสามโคกเป็นหมู่บ้านทำเครื่องปั้นดินเผา"), "src": ENW + "Sam_Khok_district", "src_name": "Wikipedia: Sam Khok district"},
    {"y": b("1774", "2317"), "text": b("A second Mon migration, under Phaya Cheng, in King Taksin's reign; part of it settles at Sam Khok.", "ชาวมอญอพยพครั้งใหญ่อีกครั้ง นำโดยพญาเจ่ง สมัยสมเด็จพระเจ้าตากสิน ส่วนหนึ่งตั้งบ้านที่สามโคก"), "src": SAMKHOK, "src_name": "วิกิพีเดีย: อำเภอสามโคก"},
    {"y": b("1815", "2358"), "text": b("King Rama II renames Sam Khok “Pratum Thani”. Thai Wikipedia gives 23 August; the Fine Arts Department says the day is not recorded and infers 16 October.",
                                       "รัชกาลที่ 2 พระราชทานนามเมืองสามโคกใหม่ว่า “ประทุมธานี” วิกิพีเดียไทยระบุ 23 สิงหาคม กรมศิลปากรว่าไม่พบบันทึกวันที่ สันนิษฐานว่า 16 ตุลาคม"), "src": MOC, "src_name": MOC_N},
    {"y": b("1890", "2433"), "text": b("Digging of Khlong Rangsit starts on 4 March: Siam's first irrigation project, dredged until 1905.", "เริ่มขุดคลองรังสิต 4 มีนาคม โครงการชลประทานแห่งแรกของสยาม ขุดต่อเนื่องถึง พ.ศ. 2448"), "src": RANGSIT, "src_name": "Wikipedia: Rangsit Canal"},
    {"y": b("1967", "2510"), "text": b("Tangerine growers move to Thung Rangsit; the fruit becomes “som Rangsit”.", "ชาวสวนย้ายมาปลูกส้มเขียวหวานที่ทุ่งรังสิต จนได้ชื่อว่าส้มรังสิต"), "src": THW + "ส้มเขียวหวาน", "src_name": "วิกิพีเดีย: ส้มเขียวหวาน"},
    {"y": b("1970", "2513"), "text": b("Wat Phra Dhammakaya is founded at Khlong Sam, Khlong Luang.", "ก่อตั้งวัดพระธรรมกายที่ตำบลคลองสาม อำเภอคลองหลวง"), "src": THW + "วัดพระธรรมกาย", "src_name": "วิกิพีเดีย: วัดพระธรรมกาย"},
    {"y": b("1978", "2521"), "text": b("Pathum Thani raises its first city pillar, on 23 August.", "ปทุมธานียกเสาหลักเมืองครั้งแรก 23 สิงหาคม"), "src": MOC, "src_name": MOC_N},
    {"y": b("1993", "2536"), "text": b("Dream World opens in Thanyaburi.", "ดรีมเวิลด์เปิดที่ธัญบุรี"), "src": THW + "ดรีมเวิลด์", "src_name": "วิกิพีเดีย: ดรีมเวิลด์"},
    {"y": b("1995", "2538"), "text": b("The National Science Museum is set up at Khlong Ha; Wat Chedi Hoi builds its chedis from fossil oyster shells.", "ตั้งองค์การพิพิธภัณฑ์วิทยาศาสตร์แห่งชาติที่คลองห้า วัดเจดีย์หอยก่อเจดีย์จากซากหอยนางรม"), "src": THW + "วัดเจดีย์หอย", "src_name": "วิกิพีเดีย: วัดเจดีย์หอย"},
    {"y": b("2017", "2560"), "text": b("Khao Hom Pathum Thani, the province's fragrant rice, is registered as a geographical indication.", "ข้าวหอมปทุมธานีขึ้นทะเบียนสิ่งบ่งชี้ทางภูมิศาสตร์"), "src": "https://webnew.ipthailand.go.th/wp-content/uploads/2026/03/gi_GI64100162.pdf", "src_name": "Department of Intellectual Property: GI register"},
]

LEGENDS = [
    {"tag": b("Sam Khok", "สามโคก"), "name": b("Three mounds", "โคกสามแห่ง"),
     "text": b("Sam Khok means “three mounds”. One telling says they were kiln mounds for firing jars; another says the old town simply had three ancient mounds. A Dutch map of 1726 calls the place a pottery-making village.",
               "สามโคก แปลว่าโคกสามแห่ง ฉบับหนึ่งว่าเป็นโคกเตาเผาตุ่ม อีกฉบับว่าเมืองเก่ามีโคกโบราณสามแห่ง แผนที่ดัตช์ พ.ศ. 2269 เรียกที่นี่ว่าหมู่บ้านทำเครื่องปั้นดินเผา"),
     "src": ENW + "Sam_Khok_district", "src_name": "Wikipedia: Sam Khok district"},
    {"tag": b("1815", "2358"), "name": b("The lotus offering", "ถวายบัว"),
     "text": b("In the 11th lunar month of 1815 King Rama II came up the river and stayed at a pavilion near today's Wat Pathum Thong. The Mon brought him armfuls of royal lotus, and he renamed the town Pratum Thani.",
               "เดือน 11 พ.ศ. 2358 รัชกาลที่ 2 เสด็จทางชลมารค ประทับพลับพลาใกล้วัดปทุมทอง ชาวมอญนำบัวหลวงมาถวายมากมาย จึงพระราชทานนามเมืองว่าประทุมธานี"),
     "src": SAMKHOK, "src_name": "วิกิพีเดีย: อำเภอสามโคก"},
    {"tag": b("Mon wats", "วัดมอญ"), "name": b("The hamsa pole", "เสาหงส์"),
     "text": b("Mon temples raise a tall pole topped with a hamsa, the sacred goose, for Hongsawadi, the city the Mon left. The legend: the Buddha saw two golden hamsa bathing where the sea lay and foretold a great city there.",
               "วัดมอญปักเสาหงส์ระลึกถึงหงสาวดีที่จากมา ตำนานว่าพระพุทธเจ้าทอดพระเนตรหงส์ทองสองตัวเล่นน้ำในที่ซึ่งเป็นทะเล และทรงทำนายว่าจะเป็นมหานคร"),
     "src": THW + "เสาหงส์", "src_name": "วิกิพีเดีย: เสาหงส์"},
    {"tag": b("Wat Phai Lom", "วัดไผ่ล้อม"), "name": b("Two merchants and the storks", "สองเศรษฐีกับนกปากห่าง"),
     "text": b("The temple's legend says two rich merchants from Sukhothai, Thao Maha Phrom and Thao Mali, built it. Today its trees hold a colony of Asian openbill storks, nesting from November to June.",
               "ตำนานว่าท่านท้าวมหาพรหมกับท่านท้าวมาลี เศรษฐีจากสุโขทัย สร้างวัดนี้ วันนี้ต้นไม้ในวัดเป็นที่ทำรังของนกปากห่าง ช่วงพฤศจิกายนถึงมิถุนายน"),
     "src": THW + "วัดไผ่ล้อม_(จังหวัดปทุมธานี)", "src_name": "วิกิพีเดีย: วัดไผ่ล้อม"},
    {"tag": b("Wat Chedi Hoi", "วัดเจดีย์หอย"), "name": b("The city of Ratanawadi", "เมืองรัตนาวดี"),
     "text": b("Abbot Thong Klueng saw in a vision that the temple ground was a great city, Ratanawadi, eight million years ago. Diggers then struck giant fossil oysters, and in 1995 he built them into chedis.",
               "หลวงพ่อทองกลึงนิมิตว่าที่ตั้งวัดเมื่อแปดล้านปีก่อนเป็นเมืองใหญ่ชื่อรัตนาวดี ต่อมาขุดพบซากหอยนางรมยักษ์ ท่านนำมาก่อเป็นเจดีย์เมื่อ พ.ศ. 2538"),
     "src": THW + "วัดเจดีย์หอย", "src_name": "วิกิพีเดีย: วัดเจดีย์หอย"},
    {"tag": b("Wat Bot", "วัดโบสถ์"), "name": b("Luang Pho Luea, the one left", "หลวงพ่อเหลือ"),
     "text": b("Around 1964 thieves cut the heads from the Buddha images in Wat Bot's ubosot. One sandstone image was left whole, and villagers named it Luang Pho Luea, “the one that remains”. It is the guardian image of Pathum Thani.",
               "ราว พ.ศ. 2507 โจรตัดเศียรพระพุทธรูปในโบสถ์วัดโบสถ์ เหลือพระศิลาทรายปางมารวิชัยองค์เดียว ชาวบ้านเรียกหลวงพ่อเหลือ เป็นพระคู่บ้านคู่เมืองปทุมธานี"),
     "src": THW + "วัดโบสถ์_(อำเภอสามโคก)", "src_name": "วิกิพีเดีย: วัดโบสถ์ (สามโคก)"},
    {"tag": b("Wat Sing", "วัดสิงห์"), "name": b("Four Buddhas, four directions", "พระประธานสี่ทิศ"),
     "text": b("At Wat Sing people pay respect to four principal Buddha images, one at each direction. Locals call it the first temple of Mueang Sam Khok.",
               "ที่วัดสิงห์ผู้คนสักการะพระประธานสี่องค์ประจำสี่ทิศ คนในพื้นที่เรียกว่าวัดแห่งแรกของเมืองสามโคก"),
     "src": "https://www.thairath.co.th/horoscope/belief/2943520", "src_name": "Thairath: Wat Sing"},
]

PEOPLE = [
    {"tag": b("c. 1660", "ราว 2203"), "name": b("Saming Poe", "สมิงเปอ"), "text": b("Mon leader who brought refugees from Mottama to Ban Sam Khok in King Narai's reign.", "ผู้นำมอญที่พาครอบครัวจากเมาะตะมะมาตั้งบ้านที่สามโคก สมัยสมเด็จพระนารายณ์"), "src": SAMKHOK, "src_name": "วิกิพีเดีย: อำเภอสามโคก"},
    {"tag": b("1774", "2317"), "name": b("Phaya Cheng", "พญาเจ่ง"), "text": b("Led the Mon migration of 1774 in King Taksin's reign; part of it settled at Sam Khok.", "หัวหน้าชาวมอญที่อพยพ พ.ศ. 2317 สมัยพระเจ้าตากสิน ส่วนหนึ่งตั้งบ้านที่สามโคก"), "src": SAMKHOK, "src_name": "วิกิพีเดีย: อำเภอสามโคก"},
    {"tag": b("1885–1951", "2428–2494"), "name": b("Prince Rangsit", "พระองค์เจ้ารังสิตประยูรศักดิ์"), "text": b("Son of King Chulalongkorn and founder of the Ministry of Public Health. The canal, the town and the fields carry his name.", "พระราชโอรสในรัชกาลที่ 5 ผู้ก่อตั้งกระทรวงสาธารณสุข คลอง เมือง และทุ่งใช้พระนามของพระองค์"), "src": ENW + "Rangsit_Prayurasakdi", "src_name": "Wikipedia: Rangsit Prayurasakdi"},
    {"tag": b("1890", "2433"), "name": b("Prince Sai Snidvongs", "พระองค์เจ้าสายสนิทวงศ์"), "text": b("Prince Rangsit's grandfather; King Chulalongkorn put him at the head of the Rangsit canal project.", "พระอัยกาของพระองค์เจ้ารังสิต ทรงเป็นประธานโครงการขุดคลองรังสิต"), "src": RANGSIT, "src_name": "Wikipedia: Rangsit Canal"},
    {"tag": b("1892", "2435"), "name": b("Erwin Müller", "เออร์วิน มูลเลอร์"), "text": b("Austrian shareholder in the Siam Canals and Irrigation Company, which dug the Rangsit canals. His Thai title was Phra Patibat Ratchaprasong.", "ชาวออสเตรีย ผู้ถือหุ้นบริษัทขุดคลองแลคูนาสยาม ผู้ขุดคลองรังสิต บรรดาศักดิ์พระปฏิบัติราชประสงค์"), "src": THW + "คลองรังสิตประยูรศักดิ์", "src_name": "วิกิพีเดีย: คลองรังสิตประยูรศักดิ์"},
    {"tag": b("1918–1972", "2461–2515"), "name": b("Paiboon Butkhan", "ไพบูลย์ บุตรขัน"), "text": b("Composer and screenwriter, born at Ban Thong Khung, Sam Khok; named a Burapasilpin in 2015.", "นักแต่งเพลงและนักเขียนบท เกิดที่บ้านท้องคุ้ง สามโคก ได้รับยกย่องเป็นบูรพศิลปิน พ.ศ. 2558"), "src": ENW + "Paiboon_Butkhan", "src_name": "Wikipedia: Paiboon Butkhan"},
    {"tag": b("born 1969", "เกิด 2512"), "name": b("Ekkapot Wongnak", "เอกพจน์ วงศ์นาค"), "text": b("Luk thung singer of the late 1980s, mayor of Khlong Luang since 2021.", "นักร้องลูกทุ่งยุคปลาย 2520 นายกเทศมนตรีเมืองคลองหลวงตั้งแต่ พ.ศ. 2564"), "src": ENW + "Ekkapot_Wongnak", "src_name": "Wikipedia: Ekkapot Wongnak"},
    {"tag": b("born 1977", "เกิด 2520"), "name": b("Sirimongkol Singmanasak", "ศิริมงคล สิงห์มนัสศักดิ์"), "text": b("Boxer from Bueng Yi Tho, Thanyaburi; WBC bantamweight champion in 1997 and super-featherweight in 2002–03.", "นักมวยจากบึงยี่โถ ธัญบุรี แชมป์โลก WBC รุ่นแบนตัมเวท พ.ศ. 2540 และซูเปอร์เฟเธอร์เวท พ.ศ. 2545–46"), "src": ENW + "Sirimongkol_Singmanasak", "src_name": "Wikipedia: Sirimongkol Singmanasak"},
    {"tag": b("born 1971", "เกิด 2514"), "name": b("Saen Sor Ploenchit", "แสน ส.เพลินจิต"), "text": b("Boxer from Prachathipat, Thanyaburi; WBA flyweight champion 1994–96.", "นักมวยจากประชาธิปัตย์ ธัญบุรี แชมป์โลก WBA รุ่นฟลายเวท พ.ศ. 2537–39"), "src": ENW + "Saen_Sor_Ploenchit", "src_name": "Wikipedia: Saen Sor Ploenchit"},
    {"tag": b("1966–2021", "2509–2564"), "name": b("Sangtiennoi Sor.Rungroj", "แสงเทียนน้อย ส.รุ่งโรจน์"), "text": b("Muay Thai champion at Lumpinee and Rajadamnern; opened a gym in his native Pathum Thani.", "แชมป์มวยไทยเวทีลุมพินีและราชดำเนิน เปิดค่ายมวยที่ปทุมธานีบ้านเกิด"), "src": ENW + "Sangtiennoi_Sor.Rungroj", "src_name": "Wikipedia: Sangtiennoi Sor.Rungroj"},
    {"tag": b("born 1946", "เกิด 2489"), "name": b("Sonthi Boonyaratglin", "สนธิ บุญยรัตกลิน"), "text": b("Army commander-in-chief who led the coup of 19 September 2006; born in Pathum Thani.", "อดีตผู้บัญชาการทหารบก ผู้นำรัฐประหาร 19 กันยายน 2549 เกิดที่ปทุมธานี"), "src": ENW + "Sonthi_Boonyaratglin", "src_name": "Wikipedia: Sonthi Boonyaratglin"},
    {"tag": b("born 1994", "เกิด 2537"), "name": b("Arayha Suparurk", "อารยะ ศุภฤกษ์"), "text": b("Model, Miss Grand Thailand 2019 and second runner-up at Miss Grand International 2019.", "นางแบบ มิสแกรนด์ไทยแลนด์ 2019 และรองอันดับ 2 มิสแกรนด์อินเตอร์เนชันแนล 2019"), "src": ENW + "Arayha_Suparurk", "src_name": "Wikipedia: Arayha Suparurk"},
]

SITES = [
    {"tag": b("Sam Khok · 1667", "สามโคก · 2210"), "name": b("Wat Sing", "วัดสิงห์"), "text": b("Riverside Mon temple; boundary consecrated 1667, the ubosot standing now built in 1757.", "วัดมอญริมเจ้าพระยา ได้วิสุงคามสีมา พ.ศ. 2210 อุโบสถหลังปัจจุบันสร้าง พ.ศ. 2300"), "src": THW + "วัดสิงห์_(จังหวัดปทุมธานี)", "src_name": "วิกิพีเดีย: วัดสิงห์", "place": "/pth/p/sing-temple-225697159.html"},
    {"tag": b("Sam Khok", "สามโคก"), "name": b("Ong Ang kiln ruins", "โบราณสถานเตาโอ่งอ่าง"), "text": b("Old kilns that fired big jars, found by Mon settlers near Wat Sing. Sam Khok is still known for Mon earthenware.", "เตาเผาโอ่งอ่างโบราณที่ชาวมอญพบใกล้วัดสิงห์ สามโคกยังมีชื่อเรื่องเครื่องปั้นดินเผามอญ"), "src": THW + "ตำบลสามโคก", "src_name": "วิกิพีเดีย: ตำบลสามโคก", "place": "/pth/p/ong-ang-ancient-kiln-1418913270.html"},
    {"tag": b("Sam Khok", "สามโคก"), "name": b("Wat Bot", "วัดโบสถ์"), "text": b("Home of Luang Pho Luea and a 28-metre statue of Somdet To, built in 2006.", "ที่ประดิษฐานหลวงพ่อเหลือ และรูปปั้นสมเด็จพระพุฒาจารย์ (โต) สูง 28 เมตร สร้าง พ.ศ. 2549"), "src": THW + "วัดโบสถ์_(อำเภอสามโคก)", "src_name": "วิกิพีเดีย: วัดโบสถ์ (สามโคก)", "place": "/pth/p/wat-bot-sam-khok-221187143.html"},
    {"tag": b("Sam Khok", "สามโคก"), "name": b("Wat Phai Lom", "วัดไผ่ล้อม"), "text": b("74 rai on the river at Ban Ngio; with Wat Ampuwararam a no-hunting area since 2008, for the openbill storks.", "74 ไร่ริมเจ้าพระยา ตำบลบ้านงิ้ว ร่วมกับวัดอัมพุวรารามเป็นเขตห้ามล่าสัตว์ป่าตั้งแต่ พ.ศ. 2551 ถิ่นนกปากห่าง"), "src": MOC, "src_name": MOC_N, "place": "/pth/p/wat-phai-lom-219056070.html"},
    {"tag": b("Lat Lum Kaeo", "ลาดหลุมแก้ว"), "name": b("Wat Chedi Hoi", "วัดเจดีย์หอย"), "text": b("Founded 1988. Chedis of fossil oyster shell, and a museum that keeps Sam Khok jars.", "ตั้งวัด พ.ศ. 2531 เจดีย์ก่อด้วยซากหอยโบราณ มีพิพิธภัณฑ์เก็บตุ่มสามโคก"), "src": THW + "วัดเจดีย์หอย", "src_name": "วิกิพีเดีย: วัดเจดีย์หอย"},
    {"tag": b("1890", "2433"), "name": b("Khlong Rangsit", "คลองรังสิตประยูรศักดิ์"), "text": b("About 56 km from the Chao Phraya at Ban Mai east to the Nakhon Nayok River, with numbered canals crossing it.", "ยาวราว 56 กม. จากเจ้าพระยาที่บ้านใหม่ไปทางตะวันออกถึงแม่น้ำนครนายก มีคลองซอยหนึ่งถึงสิบสี่ตัดผ่าน"), "src": RANGSIT, "src_name": "Wikipedia: Rangsit Canal"},
    {"tag": b("Khlong Luang", "คลองหลวง"), "name": b("Talat Thai", "ตลาดไท"), "text": b("Thailand's largest market: 542 rai of farm wholesale at km 42 of Phahonyothin Road.", "ตลาดใหญ่ที่สุดในประเทศ ตลาดกลางสินค้าเกษตร 542 ไร่ ถนนพหลโยธิน กม. 42"), "src": THW + "ตลาดไท", "src_name": "วิกิพีเดีย: ตลาดไท"},
    {"tag": b("Khlong Luang", "คลองหลวง"), "name": b("Wat Phra Dhammakaya", "วัดพระธรรมกาย"), "text": b("A Mahanikaya temple founded in 1970 at Khlong Sam; its domed cetiya shows from the air.", "วัดมหานิกาย ก่อตั้ง พ.ศ. 2513 ที่คลองสาม มหาธรรมกายเจดีย์มองเห็นได้จากท้องฟ้า"), "src": THW + "วัดพระธรรมกาย", "src_name": "วิกิพีเดีย: วัดพระธรรมกาย", "place": "/pth/p/wat-phra-dhammakaya-41291954.html"},
    {"tag": b("Khlong Ha", "คลองห้า"), "name": b("National Science Museum", "องค์การพิพิธภัณฑ์วิทยาศาสตร์แห่งชาติ"), "text": b("Set up in 1995 at Technopolis, Khlong Ha.", "ตั้ง พ.ศ. 2538 ที่เทคโนธานี คลองห้า"), "src": THW + "องค์การพิพิธภัณฑ์วิทยาศาสตร์แห่งชาติ", "src_name": "วิกิพีเดีย: อพวช.", "place": "/pth/p/national-science-museum-253429082.html"},
    {"tag": b("Khlong Luang", "คลองหลวง"), "name": b("Asian Institute of Technology", "สถาบันเทคโนโลยีแห่งเอเชีย"), "text": b("International graduate school founded in 1959 as the SEATO Graduate School of Engineering; its neighbour is Thailand Science Park (2002).", "บัณฑิตศึกษานานาชาติ ก่อตั้ง พ.ศ. 2502 ในชื่อ SEATO Graduate School of Engineering ติดกับอุทยานวิทยาศาสตร์ประเทศไทย (2545)"), "src": ENW + "Asian_Institute_of_Technology", "src_name": "Wikipedia: Asian Institute of Technology", "place": "/pth/p/asian-institute-of-technology-366177862.html"},
    {"tag": b("Thanyaburi · 1993", "ธัญบุรี · 2536"), "name": b("Dream World", "ดรีมเวิลด์"), "text": b("Outdoor amusement park of about 160 rai at Bueng Yi Tho.", "สวนสนุกกลางแจ้งกว่า 160 ไร่ ที่บึงยี่โถ"), "src": THW + "ดรีมเวิลด์", "src_name": "วิกิพีเดีย: ดรีมเวิลด์", "place": "/pth/p/dream-would-4650839709.html"},
]

CULTURE = [
    {"tag": b("Motto", "คำขวัญ"), "name": b("Land of the royal lotus", "ถิ่นบัวหลวง"),
     "text": b("The provincial motto: ถิ่นบัวหลวง เมืองรวงข้าว เชื้อชาวมอญ นครธรรมะ พระตำหนักรวมใจ สดใสเจ้าพระยา ก้าวหน้าอุตสาหกรรม. Land of the royal lotus, city of rice ears, of Mon descent, city of Dhamma, the palace that unites hearts, the bright Chao Phraya, industry going forward.",
               "ถิ่นบัวหลวง เมืองรวงข้าว เชื้อชาวมอญ นครธรรมะ พระตำหนักรวมใจ สดใสเจ้าพระยา ก้าวหน้าอุตสาหกรรม"), "src": MOC, "src_name": MOC_N},
    {"tag": b("Seal", "ตรา"), "name": b("Lotus and rice", "บัวกับรวงข้าว"),
     "text": b("The provincial seal: a pink royal lotus between two golden rice ears. The provincial flower is the lotus.", "ตราจังหวัดเป็นดอกบัวหลวงสีชมพูกลางรวงข้าวสีทองสองข้าง ดอกไม้ประจำจังหวัดคือบัวหลวง"), "src": MOC, "src_name": MOC_N},
    {"tag": b("11th month", "เดือน 11"), "name": b("Rap Bua, receiving the lotus", "ประเพณีรับบัว"),
     "text": b("A Mon festival at Sam Khok when the lotus blooms in the 11th lunar month. The Fine Arts Department ties the town's name to Rama II receiving lotus at this festival in 1815.", "ประเพณีมอญที่สามโคกช่วงบัวบานเดือน 11 กรมศิลปากรเชื่อมชื่อเมืองกับการที่รัชกาลที่ 2 รับบัวจากชาวมอญในงานนี้ พ.ศ. 2358"), "src": MOC, "src_name": MOC_N},
    {"tag": b("After Ok Phansa", "หลังออกพรรษา"), "name": b("Tak Bat Phra Roi", "ตักบาตรพระร้อย"),
     "text": b("Alms to a hundred monks, by boat. Monks paddle along the Chao Phraya and people give from the piers in front of their homes, from the first waning day of the 11th month. A Mon custom here for over a hundred years; in 2025 it ran at Wat Makham, Wat Hong Pathummawat, Wat Bot and Wat Chinwararam.",
               "พระพายเรือบิณฑบาตตามท่าน้ำหน้าบ้านริมเจ้าพระยา ตั้งแต่แรม 1 ค่ำ เดือน 11 ประเพณีมอญที่สืบมากว่าร้อยปี ปี 2568 จัดที่วัดมะขาม วัดหงษ์ปทุมาวาส วัดโบสถ์ และวัดชินวรารามวรวิหาร"),
     "src": "https://www.naewna.com/local/919150", "src_name": "Naewna, 6 Oct 2025: Tak Bat Phra Roi"},
    {"tag": b("April", "เมษายน"), "name": b("Thai-Mon Songkran", "สงกรานต์ไทย-มอญ"),
     "text": b("The province's Songkran fair at the old provincial hall brings Mon piphat bands, sand chedis and the Thai-Raman maiden contest; Mon households make khao chae.", "สงกรานต์ของจังหวัดหน้าศาลากลางหลังเก่า มีปี่พาทย์มอญ ก่อเจดีย์ทราย ประกวดธิดาไทย-รามัญ บ้านมอญทำข้าวแช่"), "src": "https://www.thaipost.net/main/detail/6856", "src_name": "Thai Post: Thai-Mon Songkran"},
    {"tag": b("Dance", "นาฏศิลป์"), "name": b("Pathum Thani Mon dance", "รำมอญปทุมธานี"),
     "text": b("Professional Mon dance troupes keep the province's dances; one piece, Mon Rap Sadet, retells the 1815 welcome of the king.", "คณะรำมอญอาชีพสืบทอดรำมอญปทุมธานี ชุดมอญรับเสด็จเล่าเรื่องการรับเสด็จ พ.ศ. 2358"), "src": "https://so01.tci-thaijo.org/index.php/humanjubru/article/view/243145", "src_name": "Journal article on Pathum Thani Mon dance, 2021"},
    {"tag": b("People", "ผู้คน"), "name": b("Mon, Chinese, Muslim", "ไทยรามัญ ไทยจีน ไทยมุสลิม"),
     "text": b("Three communities shape the province: Thai-Raman (Mon), Thai-Chinese and Thai-Muslim. The Mon are densest in Sam Khok.", "สามกลุ่มหลักของจังหวัด ไทยรามัญ ไทยจีน ไทยมุสลิม ชาวมอญอยู่หนาแน่นที่สามโคก"), "src": "https://www.thaipost.net/main/detail/6856", "src_name": "Thai Post: Thai-Mon Songkran"},
    {"tag": b("1978", "2521"), "name": b("A city pillar, late", "หลักเมืองที่มาทีหลัง"),
     "text": b("Pathum Thani had no city pillar until 23 August 1978, when one was raised in front of the provincial hall.", "ปทุมธานีไม่เคยมีหลักเมืองจนถึง 23 สิงหาคม 2521 จึงยกเสาหลักเมืองหน้าศาลากลางจังหวัด"), "src": MOC, "src_name": MOC_N},
]

FOOD = [
    {"tag": b("Rangsit", "รังสิต"), "name": b("Boat noodles", "ก๋วยเตี๋ยวเรือ"), "text": b("Small bowls, a little strong broth. Shops line the Rangsit–Nakhon Nayok road.", "ชามเล็ก น้ำซุปน้อยแต่เข้ม ร้านเรียงริมถนนรังสิต–นครนายก"), "src": NAEWNA, "src_name": "Naewna: Pathum Thani food"},
    {"tag": b("Songkran", "สงกรานต์"), "name": b("Khao chae Mon", "ข้าวแช่มอญ"), "text": b("Rice in cool flower water with seven sides: shrimp-paste balls, sweet fish floss, egg with pickled garlic, sweet mustard greens, young jackfruit, salted crab with green mango, fried noodles. Offered to the spirits and monks.", "ข้าวในน้ำดอกไม้เย็น กับเครื่องเคียงเจ็ดอย่าง กะปิทอด ปลาป่นหวาน กระเทียมดองผัดไข่ ผักกาดหวาน ยำขนุนอ่อน ยำปูเค็มมะม่วง ก๋วยเตี๋ยวผัด ถวายเทวดาและพระ"), "src": NAEWNA, "src_name": "Naewna: Pathum Thani food"},
    {"tag": b("Mon", "มอญ"), "name": b("Mon sesame rice crackers", "ข้าวเกรียบงาปิ้ง"), "text": b("Grilled rice crackers with sesame, made by families whose forebears came from Hongsawadi.", "ข้าวเกรียบมอญโบราณ ทำโดยลูกหลานชาวมอญที่มาจากหงสาวดี"), "src": NAEWNA, "src_name": "Naewna: Pathum Thani food"},
    {"tag": b("Sweet", "ขนม"), "name": b("Kalamae", "กาละแม"), "text": b("Sticky rice, sugar and coconut milk stirred for hours, made for Songkran and merit-making. Pathum Thani has long had a name for it.", "ข้าวเหนียว น้ำตาล กะทิ กวนนาน ทำช่วงสงกรานต์และงานบุญ ปทุมธานีขึ้นชื่อเรื่องนี้มานาน"), "src": NAEWNA, "src_name": "Naewna: Pathum Thani food"},
    {"tag": b("River", "ริมน้ำ"), "name": b("Grilled river prawns", "กุ้งแม่น้ำเผา"), "text": b("Big river prawns off the grill with a sharp dip, eaten by the Chao Phraya.", "กุ้งแม่น้ำตัวโตเผา จิ้มน้ำจิ้มแซ่บ กินริมเจ้าพระยา"), "src": NAEWNA, "src_name": "Naewna: Pathum Thani food"},
    {"tag": b("Farms", "ฟาร์ม"), "name": b("Sun-dried catfish", "ปลาดุกแดดเดียว"), "text": b("Catfish dried one day, then fried or curried. The province farms a lot of catfish.", "ปลาดุกตากแดดหนึ่งวัน ทอดหรือแกง ปทุมธานีเลี้ยงปลาดุกมาก"), "src": NAEWNA, "src_name": "Naewna: Pathum Thani food"},
    {"tag": b("GI 2017", "GI 2560"), "name": b("Khao Hom Pathum Thani", "ข้าวหอมปทุมธานี"), "text": b("Fragrant rice from the Pathum Thani 1 variety: long slender grain, soft and a little sticky, faint scent.", "ข้าวพันธุ์ปทุมธานี 1 เมล็ดเรียวยาว หุงนุ่มค่อนข้างเหนียว หอมอ่อน"), "src": "https://webnew.ipthailand.go.th/wp-content/uploads/2026/03/gi_GI64100162.pdf", "src_name": "Department of Intellectual Property: GI register"},
    {"tag": b("Thung Rangsit", "ทุ่งรังสิต"), "name": b("Som Rangsit", "ส้มรังสิต"), "text": b("Tangerines. From 1967 Thung Rangsit grew the most in Thailand; few orchards remain.", "ส้มเขียวหวาน ตั้งแต่ พ.ศ. 2510 ทุ่งรังสิตปลูกมากที่สุดในประเทศ ปัจจุบันเหลือไม่มาก"), "src": THW + "ส้มเขียวหวาน", "src_name": "วิกิพีเดีย: ส้มเขียวหวาน"},
]
