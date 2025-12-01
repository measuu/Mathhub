import math
import random

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

games = {}

DIFFICULTY_LEVELS = {1: 100, 2: 1000, 3: 1_000_000}


@router.post("/guess")
def guess_game(player_id: str, difficulty: int | None = None, guess: int | None = None):
    if difficulty is not None and guess is None:

        if difficulty not in DIFFICULTY_LEVELS:
            return {"error": "Невірна складність. Використовуйте 1, 2 або 3."}

        max_value = DIFFICULTY_LEVELS[difficulty]
        secret = random.randint(1, max_value)

        games[player_id] = {"number": secret, "attempts": 0, "max_value": max_value}

        return {"message": "Гру запущено!", "діапазон": f"1 – {max_value}"}

    if guess is not None:

        if player_id not in games:
            return {"error": "Гра не знайдена. Спочатку запустіть гру."}

        game = games[player_id]
        game["attempts"] += 1
        target = game["number"]

        if guess < target:
            return {"result": "Більше!"}

        elif guess > target:
            return {"result": "Менше!"}

        else:
            attempts = game["attempts"]
            max_val = game["max_value"]

            del games[player_id]

            return {
                "result": "Ви вгадали!",
                "кількість_спроб": attempts,
                "діапазон": f"1 – {max_val}",
            }

    return {"error": "Передайте або difficulty (для старту), або guess (для ходу)."}


# -------------------------------------Друга гра--------------------------------------------


class GameRequest(BaseModel):
    difficulty: int = Field(..., description="Складність: 1–100, 2–1000, 3–1_000_000")
    answer: int | None = Field(None, description="Ваша відповідь на поточне питання")


game_state = {
    "questions": [],
    "answers": [],
    "current": 0,
    "correct": 0,
    "started": False,
    "difficulty": 1,
}


@router.post("/game")
def game(req: GameRequest):
    global game_state

    if not game_state["started"]:
        game_state["difficulty"] = req.difficulty
        max_val = {1: 100, 2: 1000, 3: 1_000_000}.get(req.difficulty, 100)
        game_state["questions"] = [
            (
                random.randint(1, max_val),
                random.randint(1, max_val),
                random.choice(["+", "-", "*"]),
            )
            for _ in range(10)
        ]
        game_state["answers"] = []
        game_state["current"] = 0
        game_state["correct"] = 0
        game_state["started"] = True

        a, b, op = game_state["questions"][0]
        question_text = f"{a} {op} {b}"
        return {
            "message": "Гру розпочато! Відповідайте на перше питання!",
            "question_number": 1,
            "question": question_text,
        }

    if req.answer is None:
        return {"message": "Введіть відповідь у полі answer!"}

    a, b, op = game_state["questions"][game_state["current"]]
    if op == "+":
        correct_answer = a + b
    elif op == "-":
        correct_answer = a - b
    else:  # "*"
        correct_answer = a * b

    if req.answer == correct_answer:
        game_state["correct"] += 1

    game_state["answers"].append(req.answer)
    game_state["current"] += 1

    if game_state["current"] >= 10:
        percent = (game_state["correct"] / 10) * 100
        final_message = ""
        if percent >= 60:
            final_message = f"Вітаю! Ви добре справились: {game_state['correct']} правильних відповідей з 10 ({percent}%)."
        else:
            final_message = f"На жаль, результат невдалий: {game_state['correct']} правильних відповідей з 10 ({percent}%). Наступного разу спробуйте краще."

        game_state["started"] = False
        return {
            "message": final_message,
            "total_correct": game_state["correct"],
            "total_incorrect": 10 - game_state["correct"],
            "percent": percent,
        }

    a, b, op = game_state["questions"][game_state["current"]]
    question_text = f"{a} {op} {b}"
    return {
        "message": "Відповідайте на наступне питання!",
        "question_number": game_state["current"] + 1,
        "question": question_text,
    }


# -------------------------------------Третя гра--------------------------------------------


class PrimeGameRequest(BaseModel):
    difficulty: int = Field(..., description="Складність: 1–легко, 2–середньо, 3–важко")
    answer: str | None = Field(
        None, description="Ваша відповідь на питання: 'так' або 'ні'"
    )


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


games = {}


@router.post("/prime_game")
def prime_game(req: PrimeGameRequest):
    global games

    if "game" not in games or req.answer is None:
        if req.difficulty == 1:
            min_n, max_n = 1, 100
        elif req.difficulty == 2:
            min_n, max_n = 1, 1000
        else:
            min_n, max_n = 1, 10000

        games["game"] = {
            "difficulty": req.difficulty,
            "questions": [random.randint(min_n, max_n) for _ in range(5)],
            "current": 0,
            "correct": 0,
        }
        number = games["game"]["questions"][0]
        return {
            "message": f"Гра розпочато! Перше число: {number}. Введіть 'так' якщо просте, 'ні' якщо ні.",
            "question_number": 1,
            "number": number,
        }

    game = games["game"]
    idx = game["current"]
    number = game["questions"][idx]
    correct_answer = "так" if is_prime(number) else "ні"

    if req.answer.lower() == correct_answer:
        game["correct"] += 1
        feedback = "Вірно!"
    else:
        feedback = f"Невірно, правильна відповідь: {correct_answer}. Гарна спроба, наступного разу буде краще!"

    game["current"] += 1

    if game["current"] >= 5:
        score = game["correct"]
        percent = score / 5 * 100
        if percent == 100:
            final_message = f"Вітаємо! Ви відповіли правильно на всі 5 питань!"
        elif percent >= 60:
            final_message = (
                f"Добре зроблено! Ви відповіли правильно на {score}/5 ({percent}%)."
            )
        else:
            final_message = f"Спроба не вдалася. Ви відповіли правильно на {score}/5 ({percent}%). Наступного разу буде краще!"
        games.pop("game")
        return {"message": final_message, "score": score, "percent": percent}

    next_number = game["questions"][game["current"]]
    return {
        "feedback": feedback,
        "question_number": game["current"] + 1,
        "number": next_number,
    }


# -------------------------------------Четверта гра--------------------------------------------


class MemoryRequest(BaseModel):
    difficulty_length: int = Field(
        ...,
        description="Кількість чисел: 1–легко (3 числа), 2–середньо (5), 3–важко (7)",
    )
    difficulty_numbers: int = Field(
        ...,
        description="Складність чисел: 1–1-значні, 2–2-значні, 3–3-значні, 4–4-значні, 5–5-значні",
    )
    sequence: list[int] | None = Field(
        None, description="Ваша відповідь, поверніть послідовність чисел"
    )


memory_games = {}


@router.post("/memory_game")
def memory_game(req: MemoryRequest):
    global memory_games
    if "game" not in memory_games or req.sequence is None:
        # Кількість чисел
        if req.difficulty_length == 1:
            length = 3
        elif req.difficulty_length == 2:
            length = 5
        else:
            length = 7

        if req.difficulty_numbers == 1:
            min_val, max_val = 1, 9
        elif req.difficulty_numbers == 2:
            min_val, max_val = 10, 99
        elif req.difficulty_numbers == 3:
            min_val, max_val = 100, 999
        elif req.difficulty_numbers == 4:
            min_val, max_val = 1000, 9999
        else:
            min_val, max_val = 10000, 99999

        sequence = [random.randint(min_val, max_val) for _ in range(length)]
        memory_games["game"] = {"sequence": sequence, "length": length}

        return {
            "message": f"Гра Memory Game розпочато! Запам'ятайте цю послідовність чисел.",
            "sequence": sequence,
            "length": length,
            "number_difficulty": req.difficulty_numbers,
        }

    game = memory_games["game"]
    correct_sequence = game["sequence"]

    if req.sequence == correct_sequence:
        result_message = "Вітаємо! Ви правильно повторили послідовність."
    else:
        result_message = (
            f"Невірно! Правильна послідовність: {correct_sequence}. Спробуйте ще раз."
        )

    memory_games.pop("game")
    return {"message": result_message}


# -------------------------------------П'ята гра--------------------------------------------


WORDS = [
    "синус",
    "косинус",
    "тангенс",
    "катет",
    "гіпотенуза",
    "радіус",
    "діаметр",
    "площа",
    "обʼєм",
    "периметр",
    "коло",
    "точка",
    "вектор",
    "матриця",
]


def shuffle_word(word: str) -> str:
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


class CheckRequest(BaseModel):
    index: int
    answer: str


class CheckResponse(BaseModel):
    correct_word: str
    is_correct: bool


@router.get("/")
def get_anagram():
    index = random.randint(0, len(WORDS) - 1)
    original = WORDS[index]
    anagram = shuffle_word(original)

    return {"index": index, "anagram": anagram}


@router.post("/")
def check_anagram(data: CheckRequest):
    correct = WORDS[data.index]

    is_correct = data.answer.strip().lower() == correct.lower()

    return CheckResponse(correct_word=correct, is_correct=is_correct)
