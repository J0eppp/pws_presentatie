from manimlib import *


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

        timmerman_uitleg_2 = Text(
            "Een boekenkast kost 20 eenheden hout en 4 uur aan werktijd").to_edge(UP)

        self.play(FadeTransform(timmerman_uitleg_1, timmerman_uitleg_2))
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

        self.play(ShowCreation(axes))

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

        self.play(FadeTransform(graph1_text, graph2_text))

        graph2_formula = Tex("10 \cdot x + 20 \cdot y = 200").to_edge(UP * 3)
        self.play(ShowCreation(graph2), FadeTransform(
            graph1_formula, graph2_formula))

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
