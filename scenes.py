from manimlib import *
import numpy as np
import random


class Grafentheorie(Scene):
    def construct(self):
        grafentheorie = Text("Grafentheorie").to_edge(UP * 1)
        self.play(Write(grafentheorie))

        self.wait(4)

        verbanden = Text("Verbanden aanbrengen").to_edge(UP * 4).scale(.7)
        self.play(Write(verbanden))

        self.wait(2)

        # Voorbeeld vrienden
        self.play(FadeOut(verbanden), FadeOut(grafentheorie))

        alice_circle = Circle(radius=.7).to_edge(LEFT * 1).to_edge(UP * 1)
        alice_circle.set_fill(BLUE, opacity=1)
        alice_circle.set_stroke(BLUE_E)
        alice_label = Text("Alice").scale(.5)
        alice_label.move_to(alice_circle)

        self.play(ShowCreation(alice_circle), Write(alice_label))

        bob_circle = Circle(radius=.7).to_edge(
            RIGHT * 1).to_edge(UP * 1).set_fill(GREEN, opacity=1).set_stroke(GREEN_E)
        bob_label = Text("Bob").scale(.5).move_to(bob_circle)

        self.play(ShowCreation(bob_circle), Write(bob_label))

        alice_bob = Line(alice_circle.get_edge_center(
            bob_circle.get_center() + DOWN * .75) + DOWN * .75, bob_circle.get_edge_center(
            alice_circle.get_center() + DOWN * .75) + DOWN * .75)
        self.play(ShowCreation(alice_bob))

        cindy_circle = Circle(radius=.7).to_edge(
            RIGHT * 1).to_edge(DOWN * 1).set_fill(RED, opacity=1).set_stroke(RED_E)
        cindy_label = Text("Cindy").scale(.5).move_to(cindy_circle)
        self.play(ShowCreation(cindy_circle), ShowCreation(cindy_label))

        bob_cindy = Line(bob_circle.get_edge_center(
            cindy_circle.get_center() + LEFT * .75) + LEFT * .75, cindy_circle.get_edge_center(
            bob_circle.get_center() + LEFT * .75) + LEFT * .75)
        self.play(ShowCreation(bob_cindy))

        david_circle = Circle(radius=.7).to_edge(
            LEFT * 1).to_edge(DOWN * 1).set_fill(YELLOW, opacity=1).set_stroke(YELLOW_E)
        david_label = Text("David").scale(.5).move_to(david_circle)
        self.play(ShowCreation(david_circle), ShowCreation(david_label))

        cindy_david = Line(cindy_circle.get_edge_center(
            david_circle.get_center() + UP * .75) + UP * .75, david_circle.get_edge_center(
            cindy_circle.get_center() + UP * .75) + UP * .75)
        self.play(ShowCreation(cindy_david))

        david_alice = Line(david_circle.get_edge_center(
            alice_circle.get_center() + RIGHT * .75) + RIGHT * .75, alice_circle.get_edge_center(
            david_circle.get_center() + RIGHT * .75) + RIGHT * .75)
        self.play(ShowCreation(david_alice))

        david_bob = Line(david_circle.get_center() + UP * .5 +
                         RIGHT * .5, bob_circle.get_center() + DOWN * .5 + LEFT * .5)
        self.play(ShowCreation(david_bob))


class Presentation(Scene):
    def construct(self):
        title = Text(
            "Welkom bij onze presentatie over:").to_edge(UP)
        under_title = Text(
            "Profielwerkstuk roosteralgoritmiek").to_edge(UP * 2.3)

        self.play(Write(title), Write(under_title))
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

        self.wait(1)

        self.play(FadeOut(dot_group_2))

        voorkeuren = Text("Voorkeuren toevoegen").to_edge(UP * 1)
        self.play(Write(voorkeuren))

        voorkeuren_1 = Text(
            "Alfa-, beta- en gammavakken verspreiden over de week").to_edge(UP * 3).scale(.7)
        self.play(Write(voorkeuren_1))

        voorkeuren_strafpunten = Text(
            "Minimaliseren door middel van een strafpuntensysteem").to_edge(UP * 5).scale(.7)
        self.play(Write(voorkeuren_strafpunten))

        self.wait(4)

        self.play(FadeOut(voorkeuren), FadeOut(voorkeuren_1),
                  FadeOut(voorkeuren_strafpunten))

        # Wat wij hebben gedaan
        afhankelijke_factoren = Text(
            "Onderzoeken afhankelijke factoren").to_edge(UP * 1)
        self.play(Write(afhankelijke_factoren))

        self.wait(2)

        eigen_algoritme = Text(
            "Ontwerpen eigen algoritme").to_edge(UP * 4).scale(.7)
        self.play(Write(eigen_algoritme))

        self.wait(4)
        self.play(FadeOut(afhankelijke_factoren), FadeOut(
            eigen_algoritme))

        roostermachine = Text("Roostermachine").to_edge(UP * 1)
        self.play(Write(roostermachine))

        self.wait(3)

        graventheorie = Text("1. Grafentheorie").to_edge(UP * 4).scale(.7)
        self.play(Write(graventheorie))

        lineair_programmeren = Text(
            "2. Lineair programmeren").to_edge(UP * 6).scale(.7)
        self.play(Write(lineair_programmeren))

        self.wait(2)

        self.play(FadeOut(roostermachine), FadeOut(
            graventheorie), FadeOut(lineair_programmeren))

        grafentheorie = Text("Grafentheorie").to_edge(UP * 1)
        self.play(Write(grafentheorie))

        self.wait(4)

        verbanden = Text("Verbanden aanbrengen").to_edge(UP * 4).scale(.7)
        self.play(Write(verbanden))

        self.wait(4)

        # Voorbeeld vrienden
        self.play(FadeOut(verbanden), FadeOut(grafentheorie))

        alice_circle = Circle(radius=.7).to_edge(LEFT * 1).to_edge(UP * 1)
        alice_circle.set_fill(BLUE, opacity=1)
        alice_circle.set_stroke(BLUE_E)
        alice_label = Text("Alice").scale(.5)
        alice_label.move_to(alice_circle)

        self.play(ShowCreation(alice_circle), Write(alice_label))

        bob_circle = Circle(radius=.7).to_edge(
            RIGHT * 1).to_edge(UP * 1).set_fill(GREEN, opacity=1).set_stroke(GREEN_E)
        bob_label = Text("Bob").scale(.5).move_to(bob_circle)

        self.play(ShowCreation(bob_circle), Write(bob_label))

        alice_bob = Line(alice_circle.get_edge_center(
            bob_circle.get_center() + DOWN * .75) + DOWN * .75, bob_circle.get_edge_center(
            alice_circle.get_center() + DOWN * .75) + DOWN * .75)
        self.play(ShowCreation(alice_bob))

        cindy_circle = Circle(radius=.7).to_edge(
            RIGHT * 1).to_edge(DOWN * 1).set_fill(RED, opacity=1).set_stroke(RED_E)
        cindy_label = Text("Cindy").scale(.5).move_to(cindy_circle)
        self.play(ShowCreation(cindy_circle), ShowCreation(cindy_label))

        bob_cindy = Line(bob_circle.get_edge_center(
            cindy_circle.get_center() + LEFT * .75) + LEFT * .75, cindy_circle.get_edge_center(
            bob_circle.get_center() + LEFT * .75) + LEFT * .75)
        self.play(ShowCreation(bob_cindy))

        david_circle = Circle(radius=.7).to_edge(
            LEFT * 1).to_edge(DOWN * 1).set_fill(YELLOW, opacity=1).set_stroke(YELLOW_E)
        david_label = Text("David").scale(.5).move_to(david_circle)
        self.play(ShowCreation(david_circle), ShowCreation(david_label))

        cindy_david = Line(cindy_circle.get_edge_center(
            david_circle.get_center() + UP * .75) + UP * .75, david_circle.get_edge_center(
            cindy_circle.get_center() + UP * .75) + UP * .75)
        self.play(ShowCreation(cindy_david))

        self.wait(.5)

        david_alice = Line(david_circle.get_edge_center(
            alice_circle.get_center() + RIGHT * .75) + RIGHT * .75, alice_circle.get_edge_center(
            david_circle.get_center() + RIGHT * .75) + RIGHT * .75)
        self.play(ShowCreation(david_alice))

        david_bob = Line(david_circle.get_center() + UP * .5 +
                         RIGHT * .5, bob_circle.get_center() + DOWN * .5 + LEFT * .5)
        self.play(ShowCreation(david_bob))

        self.wait(4)

        cindy_alice_no = DashedLine(cindy_circle.get_center(
        ) + UP * .5 + LEFT * .5, alice_circle.get_center() + DOWN * .5 + RIGHT * .5, color=RED_E)
        self.play(ShowCreation(cindy_alice_no))

        self.wait(7)

        self.play(FadeOut(cindy_alice_no))

        cindy_david_purple = cindy_david.set_color(PURPLE)
        self.play(ShowCreation(cindy_david_purple))
        david_alice_purple = david_alice.set_color(PURPLE)
        self.play(ShowCreation(david_alice_purple))

        self.wait(5)

        self.play(FadeOut(alice_circle), FadeOut(alice_label), FadeOut(bob_circle), FadeOut(bob_label), FadeOut(cindy_circle), FadeOut(
            cindy_label), FadeOut(david_circle), FadeOut(david_label), FadeOut(alice_bob), FadeOut(bob_cindy), FadeOut(cindy_david), FadeOut(david_alice), FadeOut(david_bob))

        grafentheorie_bij_roosteren = Text(
            "Graftentheorie bij roosteren").to_edge(UP)
        self.play(Write(grafentheorie_bij_roosteren))

        self.wait(1)

        lessen_verbinden = Text(
            "Lessen met dezelfde docent of leerling verbinden").scale(.7).to_edge(UP * 4)
        self.play(Write(lessen_verbinden))

        self.wait(1)

        lessen_kleuren = Text(
            "Lessen die niet verbonden met elkaar zijn krijgen dezelfde kleur").scale(.7).to_edge(UP * 6)
        self.play(Write(lessen_kleuren))

        self.wait(3)

        kleuren_minimaliseren = Text(
            "Kleuren minimaliseren").scale(.7).to_edge(UP * 9)
        self.play(Write(kleuren_minimaliseren))

        self.wait(3)

        roosteren = Text(
            "Alle lessen met dezelfde kleur kunnen op hetzelfde moment ingeroosterd worden").scale(.7).to_edge(UP * 11)
        self.play(Write(roosteren))

        self.wait(6.5)

        self.play(FadeOut(grafentheorie_bij_roosteren), FadeOut(lessen_verbinden), FadeOut(
            lessen_kleuren), FadeOut(kleuren_minimaliseren), FadeOut(roosteren))

        lineair_programmeren = Text("Lineair programmeren").to_edge(UP)
        self.play(Write(lineair_programmeren))

        self.wait(2)

        min_max = Text(
            "Minimaliseren of maximaliseren doelfunctie").scale(.7).to_edge(UP * 4)
        self.play(Write(min_max))

        self.wait(3)

        voorwaarden_in_acht_nemen = Text(
            "Voorwaarden in acht nemen").scale(.7).to_edge(UP * 6)
        self.play(Write(voorwaarden_in_acht_nemen))

        self.wait(4)

        self.play(FadeOut(lineair_programmeren), FadeOut(
            min_max), FadeOut(voorwaarden_in_acht_nemen))

        timmerman = Text("Timmermanprobleem").to_edge(UP)
        self.play(Write(timmerman))

        self.wait(3)

        timmerman_uitleg_1 = Text(
            "Een timmerman kan tafels voor 180 euro verkopen en boekenkasten voor 200 euro")

        timmerman_uitleg_1.to_edge(UP)

        self.play(FadeTransform(timmerman, timmerman_uitleg_1))
        self.wait(13)

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

        self.wait(7)

        self.remove(*timmerman_obj_func)
        self.remove(*timmerman_obj_func_expl)
        self.play(FadeOut(timmerman_obj_func),
                  FadeOut(timmerman_obj_func_expl))

        vier_voorwaarden = Text("Vier voorwaarden").to_edge(UP)

        self.play(FadeTransform(timmerman_obj_func_text, vier_voorwaarden))

        self.wait(2)

        voorwaarde_1 = Text(
            "De timmerman mag 80 uur werken\nEen tafel kost 5 uur om te maken en een boekenkast 4 uur").scale(.7).to_edge(UP * 4)
        self.play(Write(voorwaarde_1))

        self.wait(9)

        voorwaarde_1_formula = Tex(
            "5 \cdot x + 4 \cdot y \leq 80").to_edge(UP * 7)

        self.play(Write(voorwaarde_1_formula))

        self.wait(6)

        self.play(FadeOut(voorwaarde_1), FadeOut(voorwaarde_1_formula))

        voorwaarde_2 = Text(
            "De timmerman mag maar 200 eenheden hout gebruiken\nEen tafel kost 10 eenheden hout en een boekenkast kost 20 eenheden hout").scale(.7).to_edge(UP * 4)
        self.play(Write(voorwaarde_2))

        self.wait(13)

        voorwaarde_2_formula = Tex(
            "10 \cdot x + 20 \cdot y \leq 200").to_edge(UP * 7)
        self.play(Write(voorwaarde_2_formula))

        self.wait(5)

        self.play(FadeOut(voorwaarde_2), FadeOut(voorwaarde_2_formula))

        voorwaarde_3_4 = Text(
            "De oplossing kan alleen bestaan uit positieve gehele getallen").scale(.7).to_edge(UP * 4)
        self.play(Write(voorwaarde_3_4))

        self.wait(5)

        voorwaarde_3_4_formula_1 = Tex(
            "x \in \mathbf{N}").to_edge(UP * 7)
        self.play(Write(voorwaarde_3_4_formula_1))
        voorwaarde_3_4_formula_2 = Tex("y \in \mathbf{N}").to_edge(UP * 9)
        self.play(Write(voorwaarde_3_4_formula_2))

        self.wait(3)

        self.play(FadeOut(voorwaarde_3_4), FadeOut(
            voorwaarde_3_4_formula_1), FadeOut(voorwaarde_3_4_formula_2), FadeOut(vier_voorwaarden))

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
        # self.wait(2)

        self.play(ShowCreation(axes))

        graph1_formula = Tex("5 \cdot x + 4 \cdot y = 80").to_edge(UP * 3)

        self.play(Write(graph1_formula))
        # self.wait(2)

        self.play(ShowCreation(graph1))

        self.wait(1)

        # 10x + 20y = 200
        # 20y = 200 - 10x
        # 2y = 20 - x
        # y = 10 - 1/2 x
        graph2 = axes.get_graph(lambda x: 10 - 0.5 * x,
                                x_range=[0, 20], color=RED)
        graph2_formula = Tex("10 \cdot x + 20 \cdot y = 200").to_edge(UP * 3)

        self.play(FadeOut(graph1_formula))
        self.play(Write(graph2_formula))

        # self.wait(1)

        self.play(ShowCreation(graph2))

        self.wait(1)

        solution = Dot(color=YELLOW_E).move_to(
            axes.coords_to_point(12, 4)).scale(.7)
        solution_label = Tex("(12, 4)").scale(.5)
        solution_label.move_to(solution.get_center() + 0.5 * UP)
        self.play(ShowCreation(solution), ShowCreation(solution_label))

        self.wait(1)

        self.play(FadeOut(axes), FadeOut(solution), FadeOut(solution_label), FadeOut(
            graph2), FadeOut(graph2_formula), FadeOut(graph1))

        self.wait(3)

        roostermachine = Text("Roostermachine").to_edge(UP)
        self.play(Write(roostermachine))

        self.wait(1)

        rm_lp = Text("Lineair programmeren").scale(.7).to_edge(UP * 4)
        self.play(Write(rm_lp))

        self.wait(2)

        rm_voorwaarde_2_lessen = Text(
            "Eén les tegelijk").scale(.7).to_edge(UP * 6)
        self.play(Write(rm_voorwaarde_2_lessen))

        self.wait(2)

        rm_voorwaarde_alle_lessen = Text(
            "Alle lessen moeten gegeven worden").scale(.7).to_edge(UP * 8)
        self.play(Write(rm_voorwaarde_alle_lessen))

        self.wait(3)

        rm_doelfunctie = Text(
            "Totale uurwaarde minimaliseren").scale(.8).to_edge(UP * 10)
        self.play(Write(rm_doelfunctie))

        self.wait(7)

        self.play(FadeOut(rm_lp), FadeOut(rm_voorwaarde_2_lessen), FadeOut(
            rm_voorwaarde_alle_lessen), FadeOut(rm_doelfunctie))

        doel = Text(
            "Leerlingen zijn zo vroeg mogelijk uit en hebben indirect zo min mogelijk tussenuren").scale(.8).to_edge(UP * 4)
        self.play(Write(doel))

        self.wait(7)

        self.play(FadeOut(roostermachine), FadeOut(doel))

        resultaten = Text("Resultaten").to_edge(UP * 1)
        self.play(Write(resultaten))
        self.wait(1)

        conclusie_1 = Text(
            "Aantal tussenuren bij 2 docenten per vak").to_edge(UP * 3).scale(.7)
        self.play(Write(conclusie_1))

        staafdiagram1 = [0.88, 5.75, 3.00, 8.75, 2.67, 7.33]
        inhoudstaafdiagram1 = [
            "RS klas 1",
            "LP klas 1",
            "RS klas 2",
            "LP klas 2",
            "RS klas 3",
            "LP klas 3",
        ]
        colors = ["#003f5c", "#58508d", "#003f5c",
                  "#58508d", "#003f5c", "#58508d", ]

        bar = BarChart(
            staafdiagram1,
            max_value=max(staafdiagram1),
            bar_colors=colors,
            bar_names=inhoudstaafdiagram1,
            bar_label_scale_val=.4,
        ).to_edge(UP * 6).scale(1)
        bar_title = Text("Tussenuren bij 2 docenten per vak")
        self.play(ShowCreation(bar))

        self.wait(6)

        self.play(FadeOut(conclusie_1), FadeOut(bar))

        conclusie_2 = Text(
            "Aantal negende uren bij 2 docenten per vak").to_edge(UP * 3).scale(.7)
        self.play(Write(conclusie_2))

        staafdiagram2 = [3.0, 0.63, 2.75, 2.50, 3.00, 1.17]
        inhoudstaafdiagram2 = [
            "RS klas 1",
            "LP klas 1",
            "RS klas 2",
            "LP klas 2",
            "RS klas 3",
            "LP klas 3",
        ]
        colors = ["#003f5c", "#58508d", "#003f5c",
                  "#58508d", "#003f5c", "#58508d", ]

        bar2 = BarChart(
            staafdiagram2,
            max_value=max(staafdiagram2),
            bar_colors=colors,
            bar_names=inhoudstaafdiagram2,
            bar_label_scale_val=.4,
        ).to_edge(UP * 6).scale(1)
        bar2_title = Text("Negende uren bij 2 docenten per vak")
        self.play(ShowCreation(bar2))

        self.wait(3)
        self.play(FadeOut(conclusie_2), FadeOut(bar2))

        conclusie_3 = Text(
            "Aantal tussenuren bij 3 docenten per vak").to_edge(UP * 3).scale(.7)
        self.play(Write(conclusie_3))

        staafdiagram3 = [0.38, 0.38, 1.75, 0.38, 3.00, 0.17]
        inhoudstaafdiagram3 = [
            "RS klas 1",
            "LP klas 1",
            "RS klas 2",
            "LP klas 2",
            "RS klas 3",
            "LP klas 3",
        ]
        colors = ["#003f5c", "#58508d", "#003f5c",
                  "#58508d", "#003f5c", "#58508d", ]

        bar3 = BarChart(
            staafdiagram3,
            max_value=max(staafdiagram3),
            bar_colors=colors,
            bar_names=inhoudstaafdiagram3,
            bar_label_scale_val=.4,
        ).to_edge(UP * 6).scale(1)
        bar3_title = Text("Tussenuren bij 3 docenten per vak")
        self.play(ShowCreation(bar3))

        self.wait(14)

        self.play(FadeOut(conclusie_3), FadeOut(bar3))

        conclusie_4 = Text(
            "Aantal negende uren bij 3 docenten per vak").to_edge(UP * 3).scale(.7)
        self.play(Write(conclusie_4))

        self.wait(2)

        staafdiagram4 = [3.00, 0.00, 2.88, 0.00, 2.67, 0.00]
        inhoudstaafdiagram4 = [
            "RS klas 1",
            "LP klas 1",
            "RS klas 2",
            "LP klas 2",
            "RS klas 3",
            "LP klas 3",
        ]
        colors = ["#003f5c", "#58508d", "#003f5c",
                  "#58508d", "#003f5c", "#58508d", ]

        bar4 = BarChart(
            staafdiagram4,
            max_value=max(staafdiagram4),
            bar_colors=colors,
            bar_names=inhoudstaafdiagram4,
            bar_label_scale_val=.4,
            bar_title="Bar4",
        ).to_edge(UP * 6).scale(1)
        bar4_title = Text("Negende uren bij 3 docenten per vak")
        self.play(ShowCreation(bar4))

        self.wait(14)

        self.play(FadeOut(resultaten), FadeOut(conclusie_4), FadeOut(bar4))

        discussie = Text("Discussie").to_edge(UP * 1)
        self.play(Write(discussie))
        self.wait(3)

        discussie_1 = Text(
            "Maatschappelijk relevant, niet heel significante toevoeging").to_edge(UP * 3).scale(.7)
        self.play(Write(discussie_1))
        self.wait(22)

        discussie_2 = Text(
            "Niet goed geweten wat te doen, indien betere inlezing mogelijk meer resultaat").to_edge(UP * 5).scale(.7)
        self.play(Write(discussie_2))
        self.wait(25)

        discussie_3 = Text(
            "Alleen onderbouw, geen bovenbouw. Geen lokalen").to_edge(UP * 8).scale(.7)
        self.play(Write(discussie_3))
        self.wait(20)

        discussie_4 = Text(
            "Aanname docent is fulltimer en mag elk werkuur lesgeven").to_edge(UP * 10).scale(.7)
        self.play(Write(discussie_4))
        self.wait(5)

        discussie_5 = Text(
            "Maar 2 leerlingen voor voorkeur leerling").to_edge(UP * 13).scale(.8)
        self.play(Write(discussie_5))

        self.wait(12)

        self.play(FadeOut(discussie), FadeOut(discussie_1), FadeOut(
            discussie_2), FadeOut(discussie_3), FadeOut(discussie_4), FadeOut(discussie_5))

        conclusie = Text("Conclusie").to_edge(UP * 1)
        self.play(Write(conclusie))

        self.play(ShowCreation(bar.scale(.6).to_edge(UP * 2).to_edge(LEFT)),
                  ShowCreation(bar2.scale(.6).to_edge(UP * 2).to_edge(
                      RIGHT)), ShowCreation(bar3.scale(.6).to_edge(DOWN * 1).to_edge(LEFT)),
                  ShowCreation(bar4.scale(.6).to_edge(
                      DOWN * 1).to_edge(RIGHT)),
                  Write(bar_title.scale(.5).to_edge(UP).to_edge(LEFT)),
                  Write(bar2_title.scale(.5).to_edge(UP).to_edge(RIGHT)),
                  Write(bar3_title.scale(.5).to_edge(DOWN * 7).to_edge(LEFT)),
                  Write(bar4_title.scale(.5).to_edge(DOWN * 7).to_edge(RIGHT)))

        self.wait(47)
        self.play(FadeOut(conclusie), FadeOut(bar.scale(.6).to_edge(UP * 2).to_edge(LEFT)),
                  FadeOut(bar2.scale(.6).to_edge(UP * 2).to_edge(
                      RIGHT)), FadeOut(bar3.scale(.6).to_edge(DOWN * 1).to_edge(LEFT)),
                  FadeOut(bar4.scale(.6).to_edge(DOWN * 1).to_edge(RIGHT)),
                  FadeOut(bar_title.scale(.5).to_edge(UP).to_edge(LEFT)),
                  FadeOut(bar2_title.scale(.5).to_edge(UP).to_edge(RIGHT)),
                  FadeOut(bar3_title.scale(.5).to_edge(
                      DOWN * 7).to_edge(LEFT)),
                  FadeOut(bar4_title.scale(.5).to_edge(DOWN * 7).to_edge(RIGHT)))

        terugkoppeling_hoofdvraag = Text(
            "Terugkoppeling hoofdvraag").to_edge(UP * 1)
        self.play(Write(terugkoppeling_hoofdvraag))
        self.wait(3)
        jamaar = Text("Ja, dit kan, maar complex").to_edge(
            UP * 6).scale(.8)
        self.play(Write(jamaar))
        jamaardiscussie = Text("Discussiepunten (niet de volle 1000 mans school), desalniettemin aangetoont hoe het zou kunnen").to_edge(
            UP * 10).scale(.8)
        self.play(Write(jamaardiscussie))
        self.wait(12)

        self.play(FadeOut(terugkoppeling_hoofdvraag),
                  FadeOut(jamaar), FadeOut(jamaardiscussie))

        bedankt = Text("Bedankt voor het kijken").scale(1.5)
        self.play(Write(bedankt))

        self.wait(5)

        self.play(FadeOut(bedankt))
