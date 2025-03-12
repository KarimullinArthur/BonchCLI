class Colors:
    DATE = "\x1b[93;1m"
    DAY = "\x1b[93;1m"
    NUMBER = "\x1b[93;41m"
    TIME = "\x1b[93;5m"
    SUBJECTSTR = ""
    LECTURE = "\x1b[94;5m"
    LAB = "\x1b[91;5m"
    PRACTICAL_JOB = "\x1b[92;5m"
    CONSULTATION = "\x1b[95;5m"
    EXAM = "\x1b[91;5m"
    LOCATION = ""
    TEACHER = "\x1b[77;1m"
    DEFAULT_LESSON_TYPE = ""
    RESET = "\x1b[0m"


def render_timetable(rsp):
    week: list[str] = []
    state = True
    firstly = True
    count = 0

    for lesson in rsp:
        try:
            if week[-1] != lesson.date:
                week.append(lesson.date)
        except IndexError:
            week.append(lesson.date)

    for lesson in rsp:
        if firstly:
            firstly = False
            state = True
        elif lesson.date == week[count]:
            state = False
        else:
            print("╚", "─"*32, sep="")
            state = True
            count += 1

        for arg in lesson:
            if arg == lesson.date and state:
                print("\t", Colors.DATE, arg, Colors.RESET)
            elif arg == lesson.day and state:
                print("\t", arg, "\n")
            elif arg in (lesson.date, lesson.day) and state == False:
                pass
            elif arg == lesson.number:
                if arg is not None:
                    print(Colors.NUMBER, arg, Colors.RESET, end='')
                else:
                    print("╔", "─", sep="", end='')
            elif arg == lesson.time:
                if state:
                    end = "─"*12
                else:
                    end = ''
                print("─"*4, Colors.TIME, arg, Colors.RESET, "─"*4, end, sep="")

            elif arg == lesson.lesson_type:
                if lesson.lesson_type == "Лекция":
                        color = Colors.LECTURE
                elif lesson.lesson_type == "Практические занятия":
                        color = Colors.PRACTICAL_JOB
                elif lesson.lesson_type == "Лабораторная работа":
                        color = Colors.LAB
                elif lesson.lesson_type == "Консультация":
                        color = Colors.CONSULTATION
                elif lesson.lesson_type in ("Экзамен", "Зачет"):
                        color = Colors.EXAM
                else:
                    color = Colors.DEFAULT_LESSON_TYPE
                print("│ ", color, arg, Colors.RESET, sep="")

            elif arg == lesson.teacher:
                print("│ ", Colors.TEACHER, arg, Colors.RESET, sep="")
            else:
                print('│', arg)


    print("╚", "─"*32, sep="")
