class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    YELLOW_SELECT = '\033[43m'
    UNDERLINE = '\033[4m'
    WHITE = '\33[37m'
    VIOLET = '\33[35m'


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
                print("\t", bcolors.OKCYAN, arg, bcolors.ENDC)
            elif arg == lesson.day and state:
                print("\t", arg, "\n")
            elif arg in (lesson.date, lesson.day) and state == False:
                pass
            elif arg == lesson.number:
                if arg is not None:
                    print(bcolors.YELLOW_SELECT, arg, bcolors.ENDC, end='')
                else:
                    print("╔", "─", sep="", end='')
            elif arg == lesson.time:
                if state:
                    end = "─"*12
                else:
                    end = ''
                print("─"*4, bcolors.WARNING, arg, bcolors.ENDC, "─"*4, end, sep="")

            elif arg == lesson.lesson_type:
                if lesson.lesson_type == "Лекция":
                        color = bcolors.OKCYAN
                elif lesson.lesson_type == "Практические занятия":
                        color = bcolors.OKCYAN
                elif lesson.lesson_type == "Лабораторная работа":
                        color = bcolors.WARNING
                elif lesson.lesson_type == "Консультация":
                        color = bcolors.WARNING
                elif lesson.lesson_type in ("Экзамен", "Зачет"):
                        color = bcolors.FAIL
                else:
                    color = bcolors.WHITE
                print("│ ", color, arg, bcolors.ENDC, sep="")

            elif arg == lesson.teacher:
                print("│ ", bcolors.VIOLET, arg, bcolors.ENDC, sep="")
            else:
                print('│', arg)


    print("╚", "─"*32, sep="")
