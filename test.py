import time
from src.logic.dots import Dots
from src.logic.console import progressBar
from rich.console import Console
import rich.progress as prog
console = Console()


def modulo(a, b):
    division = a / b
    print(division)


dt = Dots()


def ifel(a, b, c):
    return b if a else c


def progress(iteration, total, prefix='', suffix='', decimals=2, length=50, fill="━", printEnd="\r"):
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
        console.print(
            f'\r{prefix} [#57ab5a]{bar1}[/][#da3f80]{bar2}[/] [#57ab5a]{percent}% {e}[/] [#30c5c4]{suffix}[/]', end=printEnd)

    endClean = ' '*30
    if iteration == total:
        printEnd = endClean+"\n"
        final('✓')
    else:
        printEnd = endClean+printEnd
        final(dt.dot("4thcircle"))


ends = {
    # "period": "period",
    "4thcircle": "4thcircle",  # '◯',
    "classic": "classic",
    "o1": "o1",
    "o2": "o2",
    # "loadingdots": "loadingdots",
}


def func():
    Max = 24
    console.log("Writing to file:")
    for i in range(Max):
        progress(i, Max, prefix="-->", suffix=" Writing")
    progress(Max, Max, prefix="-->", suffix="Done")


# with prog.Progress(console=console) as thing:
#     t1 = thing.add_task("Making", True, 100, 0)
#     # t2 = thing.add_task("Creating", True, 100, 0)
#     while not thing.finished:
#         thing.print("OK")
#         thing.update(t1, advance=1)
#         # thing.update(t2, advance=0.5)
#         time.sleep(0.02)

with progressBar(console) as p:
    t = p.add_task("Creating", True, 100, 0)

    for i in range(1, 101):
        p.print("Hello")
        p.update(t, advance=1)
# for i in prog.track(range(9)):
#     console.print("Hello\n")
#     time.sleep(0.6)
