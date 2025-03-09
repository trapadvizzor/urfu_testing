from flask import Flask, request, jsonify
from gen_words import generate_words

app = Flask(__name__)


# Обработчик для корневого пути, чтобы не было ошибки 404
@app.route('/')
def index():
    #return "Добро пожаловать! Используйте /suggest для поиска."
    return """
    <html>
<head>
    <title> Детский центр </title>
    <link rel="stylesheet" href="static/style.css"/>
    <meta name="google-site-verification" content="XRkb5IQ3eT5Dz9f54UEE6N5eLGlDouy5I6qlRZbDlH8" />
</head>
<body>
<header>
    <a href="#contacts">
        Записаться
    </a>
    <a href="suggest"> Расписание </a>
    <img src="/static/36_group.svg"/>
</header>
<main>
    <h1> Детский центр "Премьер" </h1>
    <h2> Принимаем детей с любовью! </h2>
    <p> В нашей команде целая армия педагогов профессианалов! Чего стоит только преподаватель английского. </p>
    <p> Также мы можем предложить ребенку множество интересных занятий на выбор:
    <ul>
        <li>Бассейн с тренером <b>(</b>профессианальный опыт у которого, на минуточку, <b>ЦЕЛЫХ 10 ЛЕТ</b>!<b>)</b>, </li>
        <li>продленка для школьников и ребят подготовительного уровня,</li>
        <li>занятия с логопедом, </li>
        <li>психологом </li>
        <li> и многими другими героями нашего времени! </li>
    </ul>
    </p>
    <p>
        В нашем детском саду - школе для каждого ребенка разработана индивидуальная среда. Группы собраны по возрасту, в нашем Детском саду - школе есть 4 группы для детей дошкольного отделения:
    <ol>
        <li> Ягодки
            <p>
                Группа «Ягодки» – самая младшая группа, ее посещают дети от 2 до 3 лет, которые только начинают свое знакомство с детским садом. Максимальное количество детей в группе - 15 человек
                ​​​​​​​                     </p>
            <p>
                Восприятие ребенка этого возраста носит непроизвольный характер, он может выделить в предмете лишь его ярко выраженные признаки, часто являющиеся второстепенными. Развитие восприятия происходит на основе внешнеориентированного действия (по форме, величине, цвету) при непосредственном соотношении и сравнении предметов.
            </p>
        </li>
        <li> Птенчики
            <p>
                Группа «Птенчики» является средней группой, которую посещают дети от 4 до 5 лет.
            </p>
            <p>
                Максимальное количество детей в группе - 20 человек.
            </p>
            <p>
                Развивающая концепция данной группы построена с учетом возрастных особенностей дошкольников 4-5 лет.
            </p>
            <p>
                Педагоги группы помогают ребятам успешно осваивать развивающую программу, используя методы проектного обучения, информационно-коммуникационные технологии, организуя исследовательскую деятельность детей, а также активно сотрудничая с семьей и опираясь на знания индивидуальных способностей и потребностей каждого ребенка.
            </p>
        </li>
        <li> Лучики
            <p>
                В группе лучики у нас уже содержаться ребята возрастом от 5 до 6 лет. Дети в этом возрасте уже умеют прекрасно разговаривать, считать, а кто-то даже читать. Мы помогаем детям закрепить данные навыки и развить их критическое мышление!
            </p>
        </li>
        <li> Солнышки
            <p>
                Группа «Умнички» – подготовительная группа нашего детского сада, ее посещают дети 5-6,5 лет, которые готовятся к обучению в первом классе школы.
            </p>
            <p>
                Максимальное количество детей в группе - 20 человек.
            </p>
            <p>
                В подготовительной группе “Умнички” завершается дошкольный возраст. Происходит постепенный переход от игры как ведущей деятельности к обучению. Основное внимание педагогов направлено на эффективную организацию процесса обучения детей, а также формирование психологической готовности к школе.
            </p>
        </li>
    </ol>
    </p>
    <h2 id="Schedule"> Рассписание занятий в детском центре </h2>
    <table>
        <tr>
            <td></td>
            <td>Ягодки</td>
            <td>Птенчики</td>
            <td>Лучики</td>
            <td>Солнышки</td>
        </tr>
        <tr>
            <td>8:00</td>
            <td>Бассейн</td>
            <td>Метематика</td>
            <td>Английский</td>
            <td>Музыка</td>
        </tr>
        <tr>
            <td>10:00</td>
            <td>ИЗО</td>
            <td>Физкультура</td>
            <td>Английский</td>
            <td>Логопед</td>
        </tr>
        <tr>
            <td>11:30</td>
            <td>Прогулка</td>
            <td>Бассейн</td>
            <td>Психолог</td>
            <td>Математика</td>
        </tr>
        <tr>
            <td>12:30</td>
            <td>Сон-час</td>
            <td>Сон-час</td>
            <td>Сон-час</td>
            <td>Сон-час</td>
        </tr>
        <tr>
            <td>14:15</td>
            <td>Физкультура</td>
            <td>Английский</td>
            <td>Математика</td>
            <td>ИЗО</td>
        </tr>
        <tr>
            <td>18:10</td>
            <td>Прогулка</td>
            <td>Прогулка</td>
            <td>Прогулка</td>
            <td>Прогулка</td>
        </tr>
    </table>
</main>
<footer>
    <p id="contacts">
        Адрес: г. Екатеринбург, Кольцевая д.56
    </p>
    <p>
        Контактный телефон: +7 (982) 737-81-78
    </p>
</footer>
</body>
</html>
    """


# Обработчик для /suggest
@app.route('/suggest', methods=['GET'])
def suggest():
    prefix = request.args.get('w', '')
    # Список слов, которые будет использовать программа
    WORDS = generate_words(100, 9)
    suggestions = [word for word in WORDS if word.startswith(prefix)]
    #return '\n'.join(suggestions) + '\n'
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5031)
