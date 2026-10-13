
def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

    except (FileNotFoundError, UnicodeError, OSError, ValueError) as error:
        print(f"Помилка читання файлу: {error}")
        return []

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)

