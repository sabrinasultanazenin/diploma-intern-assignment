def my_name_is():
    print("My name is Sabrina Sultana Zenin")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"

course_and_learn=[
    {   'course': 'Python & Web',
        'learn': 'Python',
        'learn2': 'HTML, CSS, Bootstrap'
    },
    {
        'course': 'Java Spring Boot',
        'learn': 'Java',
        'learn2': 'HTML, CSS, Hibernet'
    },
    {
        'course': 'C# & ASP.NET Core',
        'learn': 'C#',
        'learn2': 'Entity Framework, Razor'
    },
    {
        'course': 'MERN Development',
        'learn': 'Node, React',
        'learn2': 'HTML, CSS'
    }
]

for value in course_and_learn:
    course_name=value['course']
    backend= value['learn']
    frontend= value['learn2']

    my_name_is()
    i_have_enrolled_course(course_name)
    i_have_learning(backend, frontend)

