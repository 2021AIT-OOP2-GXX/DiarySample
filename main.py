from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary
from diaries.Nagata2Diary import Nagata2Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NagataniDiary(),
    Nagata2Diary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
