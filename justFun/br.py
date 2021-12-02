from manim import *


class BrIntro(Scene):
    def construct(self):
        br_name = Tex(r"BattleRush", font_size=121)
        slogan = Tex(r"Rushing Battles.Always.", font_size=64)
        self.play(FadeIn(br_name))
        self.wait(0.5)
        self.play(br_name.animate.shift(UP))
        self.wait(0.25)
        self.play(Write(slogan))
