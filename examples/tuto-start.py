from data import ALPHABET

from trame.app import TrameApp
from trame.ui.html import DivLayout
from trame.widgets import gofish


class TutoStart(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)
        self._build_ui()

    def _build_ui(self):
        with DivLayout(self.server) as self.ui, gofish.GoFishProvider():
            gofish.GoFishGraph(
                data=("dataset", ALPHABET),
                # update="console.log($event)",
                update="""({gf, data, el}) => (
                        gf.chart(data)
                        .flow(
                            gf.spread('letter', { dir: 'x' })
                        )
                        .mark(gf.rect({ h: 'frequency' }))
                        .render(el, {
                            w: 500,
                            h: 300,
                            axes: true,
                        }))""",
            )


def main():
    app = TutoStart()
    app.server.start()


if __name__ == "__main__":
    main()
