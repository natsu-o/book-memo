def register_book():
    title = input("本のタイトルを入力してください: ")
    impression = input("読んだ感想を入力してください: ")

    with open("books.txt", "a", encoding="utf-8") as f:
        f.write(f"{title} : {impression}\n")

    print("本を登録しました。")

def show_books():
    try:
        with open("books.txt", "r", encoding="utf-8") as f:
            books = f.readlines()

        if books:
            print("\n★★ 登録された本 ★★")
            for i, book in enumerate(books,1):
                print(f"{i}. {book.strip()}")
            print("------------------------")
        else:
            print("まだ本が登録されていません。")
    except FileNotFoundError:
        print("まだ本が登録されていません。")

def delete_book():
    try:
        with open("books.txt", "r", encoding="utf-8") as f:
            books = f.readlines()

        if not books:
            print("削除する本がありません。")
            return

        print("\n★★ 本の一覧 ★★")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.strip()}")
        print("------------------------")

        delete_num = input("削除したい本の番号を入力してください: ")

        if delete_num.isdigit() and 1 <= int(delete_num) <= len(books):
            delete_index = int(delete_num) - 1
            deleted_book = books.pop(delete_index)

            with open("books.txt", "w", encoding="utf-8") as f:
                f.writelines(books)

            print(f"「{deleted_book.strip()}」を削除しました。")
        else:
            print("無効な番号です。")

    except FileNotFoundError:
        print("まだ本の記録がありません。")

def main():
    while True:
        print("\n--- 読んだ本の記録 ---")
        print("1. 本を登録する")
        print("2. 登録した本を見る")
        print("3. 本を削除する")
        print("4. 終了する")

        choice = input("番号を選んでください: ")

        if choice == "1":
            register_book()
            
        elif choice == "2":
            show_books()

        elif choice == "3":
            delete_book()
            
        elif choice == "4":
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度入力してください。")

if __name__ == "__main__":
    main()
    
