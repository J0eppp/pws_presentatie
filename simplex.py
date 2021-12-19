from manimgl import Scene, Text, UP, Write


class SimplexExample(Scene):
    def construct(self):
        """The function that does shit"""
        intro = Text("Een voorbeeld van het simplex algoritme")

        intro.to_edge(UP)

        self.play(Write(intro))
