from manim import *


class Intro(Scene):
    def construct(self):
        title = Tex(r"Can you simplify this?")
        formula = MathTex(r"x^2 + x = \text{?}")
        self.play(
            Write(title, run_time=0.75),
            title.animate.shift(UP)
        )
        self.play(
            Write(formula, run_time=1.25)
        )
        self.wait()
        solved_formula = MathTex(r"x^2 + x = x \cdot (x+1)", font_size=121)
        self.play(
            FadeOut(title),
            Transform(formula, solved_formula)
        )
