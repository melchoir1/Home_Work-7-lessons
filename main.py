import utils




def get_student_by_pk(pk):
    students = utils.load_students()
    #student = students["]
    for student in students:
        if student["pk"] == pk:
            return student

def get_profession_by_title(title):
    professions = utils.load_professions()
    for profession in professions:
        if profession["title"] == title:
            return profession

def check_fitness(student, profession):
    student_skill = student["skills"]
    profession_skill = profession["skills"]
    a = set(student_skill) #создаем множество
    b = set(profession_skill)
    lacks = b.difference(a) #скиллы которые нет у студента но есть в профессии
    has = b.intersection(a) #пересечение множеств
    fit_percent =int(len(has) / len(profession_skill) * 100)
    return {"has": list(has),
            "lacks": list(lacks),
            "fit_percent": fit_percent}

if __name__ == "__main__":
    print("Введите номер студента: ")
    user = int(input("Пользователь: "))
    student = get_student_by_pk(user)
    if student is None:
        print("У нас нет такого студента")
        exit()
    print(f'Выберите специальность для оценки студента {student["full_name"]}: ')
    user_profesion = input("Пользователь: ")
    profession = get_profession_by_title(user_profesion)
    if profession is None:
        print("У нас нет такой специальности")
        exit()

    #print(check_fitness(student, profession))

    fit = check_fitness(student, profession)
    print(f'Пригодность {fit["fit_percent"]}%')
    print(f'{student["full_name"]} знает {", ".join(fit["has"])}')
    print(f'{student["full_name"]} не знает {", ".join(fit["lacks"])}')

