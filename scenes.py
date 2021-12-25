from manimlib import *
import numpy as np
import random


class Presentation(Scene):
    def construct(self):
        # Intro dingen
        title = Text(
            "Welkom bij onze presentatie over:").to_edge(UP)
        under_title = Text(
            "Profielwerkstuk roosteralgoritmiek").to_edge(UP * 2.3)
        self.play(Write(title), Write(under_title))
        # self.play(Write(under_title))

        by = Text("Door: Joep van Dijk en Sam Staijen").to_edge(
            UP * 6).scale(.6)
        # self.play(Write(by))

        mentor = Text("Begeleider: T. Nooijen").to_edge(UP * 7).scale(.5)
        # self.play(Write(mentor))

        subject = Text("Vak: wiskunde").to_edge(UP * 8).scale(.5)
        # self.play(Write(subject))

        self.play(Write(by), Write(mentor), Write(subject))

        self.wait(1)

        self.play(FadeOut(subject), FadeOut(mentor), FadeOut(
            by), FadeOut(under_title), FadeOut(title))

        # Wat is het roosterprobleem?
        osg = Group()
        title = Text("Wat is het roosterprobleem?").to_edge(UP)
        osg.add(title)
        self.play(Write(title))

        self.wait(11)
        docent_part_time = Text(
            "Docenten werken vaak part-time").to_edge(UP * 3).scale(.7)
        osg.add(docent_part_time)
        self.play(Write(docent_part_time))

        leerling_beschikbaar = Text(
            "Een leerling moet op dat moment nog geen les hebben").to_edge(UP * 5).scale(.7)
        osg.add(leerling_beschikbaar)
        self.play(Write(leerling_beschikbaar))

        self.wait(5)

        self.play(FadeOut(osg))

        # Draw a table
        rects = [[], [], [], [], []]

        for h in range(len(rects)):
            for i in range(0, 10):
                rect = Rectangle(1 * 1.25, .5 * 1.25).to_edge(BOTTOM *
                                                              (.1 + .25 * 1.25 * i)).to_edge(LEFT * (1 + 2.5 * h))
                rects[h].append(rect)

        rect_group = Group()
        table_group = Group()
        for day in rects:
            for rect in day:
                rect_group.add(rect)
        self.play(ShowCreation(rect_group))

        def text_rect(text: str, x, y, color="#ffffff") -> Text:
            return Text(text, color=color).to_edge(BOTTOM * (.15 + .25 * 1.25 * y)).to_edge(LEFT * (1.1 + 2.5 * x)).scale(.7)

        # ma = Text("Ma").to_edge(
        #     LEFT * 1.1).to_edge(BOTTOM * (.15 + .25 * 1.25 * 9)).scale(.7)
        ma = text_rect("Ma", 0, 9)
        di = text_rect("Di", 1, 9)
        wo = text_rect("Wo", 2, 9)
        do = text_rect("Do", 3, 9)
        vr = text_rect("Vr", 4, 9)

        days_group = Group()
        days_group.add(ma)
        days_group.add(di)
        days_group.add(wo)
        days_group.add(do)
        days_group.add(vr)

        self.play(Write(ma), Write(di), Write(wo), Write(do), Write(vr))

        # Start scheduling stuff

        ma_u1 = text_rect("Ned", 0, 8)
        ma_u2 = text_rect("Ned", 0, 7)
        ma_u3 = text_rect("Wisk", 0, 6)
        ma_u4 = text_rect("Fr", 0, 5)
        ma_u5 = text_rect("Nat", 0, 4)
        ma_u6 = text_rect("ML", 0, 3)

        table_group.add(ma_u1)
        table_group.add(ma_u2)
        table_group.add(ma_u3)
        table_group.add(ma_u4)
        table_group.add(ma_u5)
        table_group.add(ma_u6)

        self.play(Write(ma_u1), Write(ma_u2), Write(ma_u3),
                  Write(ma_u4), Write(ma_u5), Write(ma_u6))

        di_u1 = text_rect("Ak", 1, 8)
        di_u2 = text_rect("Ak", 1, 7)
        di_u3 = text_rect("Eng", 1, 6, color="#ff0000")

        table_group.add(di_u1)
        table_group.add(di_u2)
        # table_group.add(di_u3)

        self.play(Write(di_u1))
        self.play(Write(di_u2))
        self.play(Write(di_u3))

        foutmelding = Text(
            "Oh nee, de engels docent kan dinsdag het derde uur niet").to_edge(TOP * .1)
        self.play(Write(foutmelding))
        self.wait(1)
        self.play(FadeOut(foutmelding))
        foutmelding_2 = Text(
            "Dan maar het vierde uur Engels").to_edge(TOP * .1)
        self.play(Write(foutmelding_2))

        self.wait(1)

        self.play(FadeOut(di_u3))

        di_u4 = text_rect("Eng", 1, 5)

        table_group.add(di_u4)

        self.play(Write(di_u4), FadeOut(foutmelding_2))

        self.wait(.5)

        self.play(FadeOut(table_group), FadeOut(
            rect_group), FadeOut(days_group))

        self.wait(1)

        rooster_formula_1 = Tex(
            "\sum{hour \cdot scheduled \; | \; (hour, scheduled) \in lessons \; | \; lessons \in groups}").scale(.7)

        self.play(Write(rooster_formula_1))

        self.wait(1)

        self.play(FadeOut(rooster_formula_1))

        dot_group = Group()
        dots = []
        for i in range(300):
            x = (np.random.random() - .5) * 13
            y = (np.random.random() - .5) * 7
            def r(): return random.randint(0, 255)
            color = '#%02X%02X%02X' % (r(), r(), r())
            dot = Dot(np.array([x, y, 1]), color=color)
            dot_group.add(dot)
            dots.append(dot)

        self.play(ShowCreation(dot_group))

        self.wait(2)

        dot_group_2 = Group()
        dots_2 = []
        for i in range(300):
            x = (np.random.random() - .5) * 13
            y = (np.random.random() - .5) * 7
            def r(): return random.randint(0, 255)
            color = '#%02X%02X%02X' % (r(), r(), r())
            dot = Dot(np.array([x, y, 1]), color=color)
            dot_group_2.add(dot)
            dots_2.append(dot)

        self.play(FadeTransformPieces(dot_group, dot_group_2))

        self.wait(3)

        self.play(FadeOut(dot_group_2))

        voorkeuren = Text("Voorkeuren toevoegen").to_edge(UP * 1)
        self.play(Write(voorkeuren))

        voorkeuren_1 = Text(
            "Alfa-, beta- en gammavakken verspreiden over de week").to_edge(UP * 3).scale(.7)
        self.play(Write(voorkeuren_1))

        voorkeuren_strafpunten = Text(
            "Minimaliseren door middel van een strafpuntensysteem").to_edge(UP * 5).scale(.7)
        self.play(Write(voorkeuren_strafpunten))

        self.wait(2)

        self.play(FadeOut(voorkeuren), FadeOut(voorkeuren_1),
                  FadeOut(voorkeuren_strafpunten))

        # temp = Text(
        #     "Docenten en leerlingen moeten op hetzelfde moment beschikbaar zijn").to_edge(UP * 3).scale(.8)
        # self.play(Write(temp))
        # on_screen.append(temp)
        # self.wait(1)
        # temp = Text("Een klas moet per vak dezelfde docent hebben").to_edge(
        #     UP * 6).scale(.8)
        # self.play(Write(temp))
        # on_screen.append(temp)
        # self.wait(1)
        # temp = Text("Et cetera").to_edge(
        #     UP * 9).scale(.8)
        # self.play(Write(temp))
        # on_screen.append(temp)
        # self.wait(1)

        # for x in on_screen:
        #     self.play(FadeOut(x))

        # on_screen = []
        # timetable = Table([[]])

        # timetabling_problem = Text(
        #     "Een rooster moet aan een aantal eisen voldoen:").to_edge(UP * 2.3).scale(.9)
        # self.play(Write(timetabling_problem))
        # tp_1 = Text(
        #     "1. Alle lessen die een leerling hoort te krijgen moeten gegeven worden").to_edge(UP * 4).scale(.6).to_edge(LEFT)
        # self.play(Write(tp_1))
        # tp_2 = Text(
        #     "2. Een leerling of docent kan niet twee lessen tegelijk volgen/geven").to_edge(UP * 6).scale(.6).to_edge(LEFT)
        # self.play(Write(tp_2))
        # tp_3 = Text(
        #     "3. Veel docenten werken part-time").to_edge(UP * 8).scale(.6).to_edge(LEFT)
        # self.play(Write(tp_3))

        # self.wait(1)

        # timetabling_preferences = Text(
        #     "Daarnaast zullen er persoonlijke belangen zijn:").to_edge(UP * 2.3).scale(.9)
        # self.play(FadeOut(tp_1),
        #           FadeOut(tp_2), FadeOut(tp_3), FadeOut(timetabling_problem))
        # self.play(Write(timetabling_preferences))
        # tpr_1 = Text("1. Leerlingen en docenten zullen zelf voorkeuren hebben, zoals zo min mogelijk tussenuren").to_edge(
        #     UP * 4).scale(.6).to_edge(LEFT)
        # self.play(Write(tpr_1))
        # tpr_2 = Text("2. Leerlingen hebben liever dat de vakken verspreid zijn over de week, je wilt niet 4 uur Nederlands op één dag hebben").to_edge(
        #     UP * 6).scale(.6).to_edge(LEFT)
        # self.play(Write(tpr_2))


class SimplexExplanation(Scene):
    def construct(self):
        intro = Text("Het simplexalgoritme\nMet het timmermanprobleem")

        intro.to_edge(UP)

        self.play(Write(intro))
        self.wait(2)

        timmerman_uitleg_1 = Text(
            "Een timmerman kan tafels voor 180 euro verkopen en boekenkasten voor 200 euro")

        timmerman_uitleg_1.to_edge(UP)

        self.play(FadeTransform(intro, timmerman_uitleg_1))
        self.wait(2)

        timmerman_obj_func_text = Text(
            "Dit kunnen we formuleren in de volgende formule:").to_edge(UP)
        self.play(FadeTransform(timmerman_uitleg_1, timmerman_obj_func_text))
        self.wait(1)

        timmerman_obj_func = Tex(
            "f(x, y) = 180 \cdot x + 200 \cdot y").to_edge(UP * 3)
        timmerman_obj_func_expl = Text(
            "Waarbij x het aantal tafels is en y het aantal boekenkasten").to_edge(UP * 5).scale(0.8)
        self.play(ShowCreation(timmerman_obj_func))
        self.play(ShowCreation(timmerman_obj_func_expl))

        self.wait(2)

        # self.remove(*timmerman_obj_func_text)
        self.remove(*timmerman_obj_func)
        self.remove(*timmerman_obj_func_expl)
        self.play(FadeOut(timmerman_obj_func),
                  FadeOut(timmerman_obj_func_expl))

        timmerman_uitleg_2 = Text(
            "Een boekenkast kost 20 eenheden hout en 4 uur aan werktijd").to_edge(UP)

        self.play(FadeTransform(timmerman_obj_func_text, timmerman_uitleg_2))
        self.wait(2)

        timmerman_uitleg_3 = Text(
            "Een tafel kost 10 eenheden hout en 5 uur aan werktijd").to_edge(UP)

        self.play(FadeTransform(timmerman_uitleg_2, timmerman_uitleg_3))
        self.wait(2)

        # Create graph
        axes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 25, 5],
            axis_config={"color": BLUE,
                         "include_numbers": True}
        )

        # 5x + 4y = 80
        # 4y = 80 - 5x
        # y = 20 - 5/4 x
        graph1 = axes.get_graph(lambda x: 20 - 1.25 * x,
                                color=WHITE, x_range=[0, 16])
        graph1_text = Text(
            "De timmerman mag niet meer dan 80 uur werken", ).to_edge(UP)
        graph1_text.scale(0.8)
        self.play(FadeTransform(timmerman_uitleg_3, graph1_text))
        self.wait(2)

        self.play(ShowCreation(axes))

        graph1_formula = Tex("5 \cdot x + 4 \cdot y = 80").to_edge(UP * 3)

        self.play(ShowCreation(graph1_formula))
        self.wait(2)

        self.play(ShowCreation(graph1))

        self.wait(2)

        # 10x + 20y = 200
        # 20y = 200 - 10x
        # 2y = 20 - x
        # y = 10 - 1/2 x
        graph2 = axes.get_graph(lambda x: 10 - 0.5 * x,
                                x_range=[0, 20], color=RED)
        graph2_text = Text(
            "De timmerman mag niet teveel hout gebruiken", ).to_edge(UP).scale(0.8)
        graph2_formula = Tex("10 \cdot x + 20 \cdot y = 200").to_edge(UP * 3)

        self.play(FadeTransform(graph1_text, graph2_text), FadeTransform(
            graph1_formula, graph2_formula))

        self.wait(1)

        self.play(ShowCreation(graph2))

        self.wait(2)

        point0 = Dot(color=YELLOW).move_to(
            axes.coords_to_point(0, 0)).scale(0.5)
        point1 = Dot(color=YELLOW).move_to(
            axes.coords_to_point(13 + 1/3, 3 + 1/3)).scale(0.5)
        point2 = Dot(color=YELLOW).move_to(
            axes.coords_to_point(0, 10)).scale(0.5)
        point3 = Dot(color=YELLOW).move_to(
            axes.coords_to_point(0, 20)).scale(0.5)
        point4 = Dot(color=YELLOW).move_to(
            axes.coords_to_point(16, 0)).scale(0.5)
        point5 = Dot(color=YELLOW).move_to(
            axes.coords_to_point(20, 0)).scale(0.5)

        self.play(ShowCreation(point0), ShowCreation(point1), ShowCreation(
            point2), ShowCreation(point3), ShowCreation(point4), ShowCreation(point5))

        dots_text = Text("Een van deze punten zal de maximale waarde zijn")

        self.wait(2)
