from rich.console import Console as cl
from rich.progress import Progress
from .dots import Dots


class progressBar(Progress):
    def __init__(self, console=None,) -> None:
        super().__init__(console=console)

    def advancePrint(self, msg: str, *advance_args, **advance_kwargs):
        self.print(msg)
        self.advance(*advance_args, **advance_kwargs)


class Console(cl):
    dt = Dots()

    def beforeProgress(self, msg: str, *progress_args, **progress_kwargs):
        self.endLine(msg)
        self.progress(*progress_args, **progress_kwargs)

    def endLine(self, *msgs):
        self.print(*msgs, ' '*100)

    def progress(self, iteration, total, prefix='', suffix='', decimals=2, length=50, fill="━", printEnd="\r"):
        """Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\\r", "\\r\\n") (Str)
        """
        percent = ("{:.1f}").format(100 * (iteration / float(total)))
        filled = int(length * iteration // total)
        bar1 = (fill * filled)
        bar2 = ('━' * (length - filled))
        # print(fill*filled, '᠆'*(length - filled), "Yes")

        def final(e):
            self.print(
                f'\r{prefix} [#57ab5a]{bar1}[/][#da3f80]{bar2}[/] [#57ab5a]{percent}% {e}[/] [#30c5c4]{suffix}[/]', end=printEnd)

        endClean = ' '*30
        if iteration == total:
            printEnd = endClean+"\n"
            final('✓')
        else:
            printEnd = endClean+printEnd
            final(self.dt.dot("4thcircle"))
