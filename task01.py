def total_salary(path: str):
    employee_number = 0
    salary_sum = 0

    try:
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue

                name, salary = line.split(',')
                employee_number += 1
                salary_sum += int(salary)

        average_salary = salary_sum / employee_number if employee_number else 0

        return salary_sum, average_salary
    except (FileNotFoundError, UnicodeError, ValueError) as error:
        print(f"Помилка обробки файлу: {error}")
        return 0, 0



if __name__ == '__main__':
    total, average = total_salary("salary.txt")

    print(f"Загальна сума заробітної плати: {total}")
    print(f"Середня заробітна плата: {average}")

