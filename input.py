
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "expenses.csv"
FIELDNAMES = ["date", "amount", "category", "notes"]


def create_csv_if_needed():
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def get_expense_date():
    while True:
        date_text = input("支出日期 (YYYY-MM-DD)：").strip()
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("日期格式錯誤，請重新輸入。")


def get_amount():
    while True:
        amount_text = input("支出金額：").strip()
        try:
            amount = Decimal(amount_text)
            if amount <= 0:
                print("金額必須大於 0。")
                continue
            return f"{amount:.2f}"
        except InvalidOperation:
            print("金額格式錯誤，請輸入數字。")


def add_expense():
    date = get_expense_date()
    amount = get_amount()

    while True:
        category = input("支出類別：").strip()
        if category:
            break
        print("類別不可空白。")

    notes = input("備註（可選）：").strip()

    create_csv_if_needed()

    with DATA_FILE.open("a", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date,
            "amount": amount,
            "category": category,
            "notes": notes
        })

    print("支出已成功儲存！")


def main():
    create_csv_if_needed()
    print("===== 支出記錄工具 =====")

    while True:
        add_expense()

        while True:
            choice = input("是否繼續新增支出？(y/n)：").strip().lower()
            if choice in ("y", "n"):
                break
            print("請輸入 y 或 n。")

        if choice == "n":
            print("輸入結束。")
            break


if __name__ == "__main__":
    main()
