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


class Idea(Scene):
    def construct(self):
        solved_formula = MathTex(r"x^2 + x = x \cdot (x+1)", font_size=121).shift(UP)
        self.add(solved_formula)
        solved_formula_bracket = MathTex(r"\underbrace{x^2 + x}_{x \cdot x + 1 \cdot x} = x \cdot (x+1)", font_size=121)
        solved_formula_bracket.align_to(solved_formula, UP)
        solved_formula_bracket.align_to(solved_formula, RIGHT)
        self.play(
            FadeIn(solved_formula_bracket)
        )
        self.remove(solved_formula)
        self.wait()
        leftside = MathTex(r"x \cdot x + 1 \cdot x", font_size=121)
        leftside_col = MathTex(r"x \cdot x + 1 \cdot x", font_size=121, substrings_to_isolate="x")
        leftside_col.set_color_by_tex("x", YELLOW)
        self.play(Transform(solved_formula_bracket, leftside))
        self.play(FadeOut(leftside),
                  FadeIn(leftside_col))
        self.wait()


class Testing(Scene):
    def construct(self):
        factorized = MathTex(r"x \cdot x + 1 \cdot x = x \cdot (x+1)", font_size=121, substrings_to_isolate="x")
        factorized.set_color_by_tex("x", YELLOW)
        self.add(factorized)
        for fucker in factorized:
            self.play(fucker.animate.shift(UP))


class Factoring(Scene):
    def construct(self):
        leftside_col = MathTex(r"x \cdot x + 1 \cdot x", font_size=121, substrings_to_isolate="x")
        leftside_col.set_color_by_tex("x", YELLOW)
        factorized = MathTex(r"x \cdot x + 1 \cdot x = x \cdot (x+1)", font_size=121, substrings_to_isolate="x")
        factorized.set_color_by_tex("x", YELLOW)
        factorized.to_edge(LEFT)
        self.play(
            leftside_col.animate.to_edge(LEFT)
        )
        self.play(
            leftside_col[2].animate.shift(UP),
            leftside_col[-1].animate.shift(UP),
            *[
                Write(tex)
                for tex in (factorized[5], factorized[7:len(factorized)])
            ]
        )
        factorized[6].shift(UP)
        self.play(
            FadeIn(factorized[6]),
            FadeOut(leftside_col[2], target_position=factorized[6]),
            FadeOut(leftside_col[-1], target_position=factorized[6]),

        )
        self.play(
            factorized[6].animate.shift(DOWN),
        )
        self.wait(0.5)
        endformula = MathTex(r"x \cdot (x+1)", font_size=121)
        self.play(*[
                FadeOut(tex)
                for tex in (factorized[5], leftside_col[0:2], leftside_col[3])
            ])
        self.play(
            *[
                Transform(tex, endformula)
                for tex in factorized[6:len(factorized)]
            ]
        )
        self.wait()


class AlternativeExplanation(Scene):
    def construct(self):
        a_times_b = MathTex(r"a \cdot b", font_size=121)
        expanded_muliplication_1 = MathTex(r"a \cdot b = \underbrace{b + b + \cdots + b}_{a \text{ times}",
                                           font_size=121)
        expanded_muliplication_1.align_to(a_times_b, UP)
        self.add(a_times_b)
        self.play(a_times_b.animate.align_to(expanded_muliplication_1, LEFT))
        self.wait()
        self.play(Write(expanded_muliplication_1),
                  FadeOut(a_times_b))
        self.wait()
        expanded_muliplication_2 = MathTex(r"a \cdot b = \underbrace{a + a + \cdots + a}_{b \text{ times}",
                                           font_size=121)
        expanded_muliplication_2.shift(2*DOWN).align_to(expanded_muliplication_1, LEFT)
        self.play(expanded_muliplication_1.animate.shift(2.5*UP))
        self.play(Write(expanded_muliplication_2))
        self.wait()
