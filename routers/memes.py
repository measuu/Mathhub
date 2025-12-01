import random

from fastapi import APIRouter, HTTPException

router = APIRouter()

memes_db = [
    {
        "id": 1,
        "title": "Коли вчитель сказав: 'Зараз буде легка задача'",
        "url": "/static/memes/1.jpg",
        "likes": 0,
    },
    {
        "id": 2,
        "title": "Математика — це не важко. Важко зрозуміти математику",
        "url": "/static/memes/2.jpg",
        "likes": 0,
    },
    {
        "id": 3,
        "title": "Коли 20 хвилин рахуєш, а вчитель каже: 'А можна було простіше'",
        "url": "/static/memes/3.jpg",
        "likes": 0,
    },
    {
        "id": 4,
        "title": "Синус чи косинус? Довіряй — але перевіряй",
        "url": "/static/memes/4.jpg",
        "likes": 0,
    },
    {
        "id": 5,
        "title": "Коли нарешті зрозумів тему, а урок закінчився",
        "url": "/static/memes/5.jpg",
        "likes": 0,
    },
    {
        "id": 6,
        "title": "Коли відповідь 0 — але ти не впевнений, чи це геніально, чи помилка",
        "url": "/static/memes/6.jpg",
        "likes": 0,
    },
    {
        "id": 7,
        "title": "— Скільки буде 2+2? — Залежить від контексту",
        "url": "/static/memes/7.jpg",
        "likes": 0,
    },
    {
        "id": 8,
        "title": "Математики не плачуть — вони просто мінімізують функцію смутку",
        "url": "/static/memes/8.jpg",
        "likes": 0,
    },
    {
        "id": 9,
        "title": "Коли згадав формулу — але через секунду забув",
        "url": "/static/memes/9.jpg",
        "likes": 0,
    },
    {
        "id": 10,
        "title": "Піфагор би пишався… або ні",
        "url": "/static/memes/10.jpg",
        "likes": 0,
    },
    {
        "id": 11,
        "title": "Усі дороги ведуть до теореми Піфагора",
        "url": "/static/memes/11.jpg",
        "likes": 0,
    },
    {
        "id": 12,
        "title": "Коли коло ідеальне, а життя — ні",
        "url": "/static/memes/12.jpg",
        "likes": 0,
    },
    {
        "id": 13,
        "title": "Чому квадрат має 4 кути? — Бо може собі дозволити",
        "url": "/static/memes/13.jpg",
        "likes": 0,
    },
    {
        "id": 14,
        "title": "Коли побачив задачу з геометрії — і зразу став двовимірним від шоку",
        "url": "/static/memes/14.jpg",
        "likes": 0,
    },
    {
        "id": 15,
        "title": "Знайти x? Він сам себе не знайде",
        "url": "/static/memes/15.jpg",
        "likes": 0,
    },
    {
        "id": 16,
        "title": "Алгебра — це коли букви вирішили стати цифрами",
        "url": "/static/memes/16.jpg",
        "likes": 0,
    },
    {
        "id": 17,
        "title": "Вирази прості: а от життя — ні",
        "url": "/static/memes/17.jpg",
        "likes": 0,
    },
    {
        "id": 18,
        "title": "Коли спростив вираз, а він став ще гіршим…",
        "url": "/static/memes/18.jpg",
        "likes": 0,
    },
    {
        "id": 19,
        "title": "Похідні — коли треба дізнатися, наскільки сильно все змінюється",
        "url": "/static/memes/19.jpg",
        "likes": 0,
    },
    {
        "id": 20,
        "title": "Інтеграл? Ні, дякую, я не голодний",
        "url": "/static/memes/20.jpg",
        "likes": 0,
    },
    {
        "id": 21,
        "title": "Коли взяв інтеграл — і отримав плюс C",
        "url": "/static/memes/21.jpg",
        "likes": 0,
    },
    {
        "id": 22,
        "title": "Похідна мого терпіння дорівнює нулю",
        "url": "/static/memes/22.jpg",
        "likes": 0,
    },
    {
        "id": 23,
        "title": "Легко — це коли вчитель розв’язує",
        "url": "/static/memes/23.jpg",
        "likes": 0,
    },
    {
        "id": 24,
        "title": "Коли вчитель каже 'зрозуміло?' — а ти вже в іншій реальності",
        "url": "/static/memes/24.jpg",
        "likes": 0,
    },
    {
        "id": 25,
        "title": "Контрольна з математики: 90% страху, 10% математики",
        "url": "/static/memes/25.jpg",
        "likes": 0,
    },
    {
        "id": 26,
        "title": "Я: *вчу математику* — Мозок: 'Давай подумаємо про сенс життя…'",
        "url": "/static/memes/26.jpg",
        "likes": 0,
    },
    {
        "id": 27,
        "title": "Коли думав, що зрозумів, але тест показав інше",
        "url": "/static/memes/27.jpg",
        "likes": 0,
    },
    {
        "id": 28,
        "title": "Якщо a^2 + b^2 = c^2, то ти в правильному місці",
        "url": "/static/memes/28.jpg",
        "likes": 0,
    },
    {
        "id": 29,
        "title": "Коли шукаєш похідну і знаходиш інтеграл",
        "url": "/static/memes/29.jpg",
        "likes": 0,
    },
    {
        "id": 30,
        "title": "Множини: збирай, як колекцію магнітів",
        "url": "/static/memes/30.jpg",
        "likes": 0,
    },
    {
        "id": 31,
        "title": "Коли границя не існує — і це твій настрій",
        "url": "/static/memes/31.jpg",
        "likes": 0,
    },
    {
        "id": 32,
        "title": "Коли у задачі з’являється π — і серце калатає",
        "url": "/static/memes/32.jpg",
        "likes": 0,
    },
    {
        "id": 33,
        "title": "Дроби: коли ділимо все на половину життя",
        "url": "/static/memes/33.jpg",
        "likes": 0,
    },
    {
        "id": 34,
        "title": "Факторіал! Коли прості числа просто не вистачає",
        "url": "/static/memes/34.jpg",
        "likes": 0,
    },
    {
        "id": 35,
        "title": "Коли побачив рівняння 3-го ступеня — і захотів спати",
        "url": "/static/memes/35.jpg",
        "likes": 0,
    },
    {
        "id": 36,
        "title": "Коли розв’язав задачу — і вчитель сказав 'правильно, але без доказу'",
        "url": "/static/memes/36.jpg",
        "likes": 0,
    },
    {
        "id": 37,
        "title": "Коли графік виглядає як гірка — і ти на ньому як екстремум",
        "url": "/static/memes/37.jpg",
        "likes": 0,
    },
    {
        "id": 38,
        "title": "Коли задача з комбінаторики виглядає як хаос",
        "url": "/static/memes/38.jpg",
        "likes": 0,
    },
    {
        "id": 39,
        "title": "Коли розв’язав систему рівнянь і відчув себе богом",
        "url": "/static/memes/39.jpg",
        "likes": 0,
    },
    {
        "id": 40,
        "title": "Логарифми: маленькі числа великого значення",
        "url": "/static/memes/40.jpg",
        "likes": 0,
    },
    {
        "id": 41,
        "title": "Коли побачив задачу на інтеграли за 20 балів",
        "url": "/static/memes/41.jpg",
        "likes": 0,
    },
    {
        "id": 42,
        "title": "Коли вчитель каже 'це просто' — а ти в розпачі",
        "url": "/static/memes/42.jpg",
        "likes": 0,
    },
    {
        "id": 43,
        "title": "Коли хочеш перевірити відповідь — а її немає",
        "url": "/static/memes/43.jpg",
        "likes": 0,
    },
    {
        "id": 44,
        "title": "Коли задачу з геометрії треба вирішити усно",
        "url": "/static/memes/44.jpg",
        "likes": 0,
    },
    {
        "id": 45,
        "title": "Коли розв’язав квадратне рівняння — і все одно сумніваєшся",
        "url": "/static/memes/45.jpg",
        "likes": 0,
    },
    {
        "id": 46,
        "title": "Математичні парадокси: коли логіка проти тебе",
        "url": "/static/memes/46.jpg",
        "likes": 0,
    },
    {
        "id": 47,
        "title": "Коли у задачі з’являється знаменник 0",
        "url": "/static/memes/47.jpg",
        "likes": 0,
    },
    {
        "id": 48,
        "title": "Коли інтуїція підказує, а формули заперечують",
        "url": "/static/memes/48.jpg",
        "likes": 0,
    },
    {
        "id": 49,
        "title": "Коли похідна = 0, а це екстремум твого настрою",
        "url": "/static/memes/49.jpg",
        "likes": 0,
    },
    {
        "id": 50,
        "title": "Коли формули красиві, а задачі страшні",
        "url": "/static/memes/50.jpg",
        "likes": 0,
    },
]


@router.get("/memes/random")
def get_random_meme():
    if not memes_db:
        raise HTTPException(404, "Мемів поки немає")
    return random.choice(memes_db)


@router.get("/memes/all")
def get_all_memes():
    return memes_db


@router.post("/memes/add")
def add_meme(text: str):
    if not text:
        raise HTTPException(400, "Текст мемa не може бути порожнім")

    meme_id = len(memes_db) + 1
    new_meme = {"id": meme_id, "text": text, "likes": 0}
    memes_db.append(new_meme)
    return {"status": "ok", "meme": new_meme}


@router.post("/memes/vote/{meme_id}")
def vote_meme(meme_id: int, up: bool = True):
    for meme in memes_db:
        if meme["id"] == meme_id:
            meme["likes"] += 1 if up else -1
            if meme["likes"] < 0:
                meme["likes"] = 0
            return {"id": meme_id, "likes": meme["likes"]}
    raise HTTPException(404, "Мем не знайдено")


@router.get("/memes/popular")
def get_popular_memes(limit: int = 10):
    return sorted(memes_db, key=lambda x: x["likes"], reverse=True)[:limit]
