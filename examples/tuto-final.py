import asyncio
import random

from data import SEAFOOD

from trame.app import TrameApp
from trame.ui.html import DivLayout
from trame.widgets import gofish, html


class TutoFinal(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)
        self.directions = [random.choice([-5, 5]) for _ in SEAFOOD]
        self.bounce_range = [1, 100]
        self.animation_tasks = set()
        self._build_ui()

    def _build_ui(self):
        self.state.setdefault("animate", False)
        with DivLayout(self.server) as self.ui:
            html.Button("{{ animate ? 'Stop' : 'Play' }}", click=self.toggle_animation)
            gofish.GoFishGraph(
                data=("dataset", SEAFOOD),
                update="""
                    ({ gf, data, el }) => (
                        gf.layer(
                            { coord: gf.clock() },
                            [
                              gf.chart(data)
                                .flow(
                                    gf.spread('lake', {
                                        dir: 'x',
                                        spacing: (2 * Math.PI) / 6,
                                        mode: 'center',
                                        y: 50,
                                        label: false,
                                    }),
                                    gf.derive((d) => gf.orderBy(d, 'count')),
                                    gf.stack('species', { dir: 'y', label: false })
                                )
                                .mark(gf.rect({ h: 'count', fill: 'species' }))
                                .as('bars'),
                              gf.chart(gf.select('bars'))
                                .flow(gf.group('species'))
                                .mark(gf.area({ opacity: 0.8 })),
                            ]
                        ).render(el, {
                            w: 500,
                            h: 300,
                            transform: { x: 250, y: 150 },
                            axes: true,
                        })
                    )
                    """,
            )

    def toggle_animation(self):
        self.state.animate = not self.state.animate
        if self.state.animate:
            task = asyncio.create_task(self._animate())
            self.animation_tasks.add(task)
            task.add_done_callback(self.animation_tasks.discard)

    def next(self):
        for idx, entry in enumerate(self.state.dataset):
            delta = self.directions[idx]
            if self.bounce_range[0] < entry["count"] < self.bounce_range[1]:
                entry["count"] += delta
            else:
                self.directions[idx] *= -1
                entry["count"] -= delta

        self.state.dirty("dataset")

    async def _animate(self):
        while self.state.animate:
            await asyncio.sleep(0.1)
            with self.state:
                self.next()


def main():
    app = TutoFinal()
    app.server.start()


if __name__ == "__main__":
    main()
