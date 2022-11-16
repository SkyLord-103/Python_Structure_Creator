import time


class Dots:
    dots = {
        "period": ['.  ', '.  ', '.. ', '.. ', '...', '...'],
        "4thcircle": ['◜', '◝', '◞', '◟'],
        "classic": ['-', '\\', '|', '/'],
        "o1": ['Ooo', 'Ooo', 'OOo', 'OOo', 'OOO', 'OOO',
               'oOO', 'oOO', 'ooO', 'ooO'],
        "o2": ['O..', 'OO.', 'OOO', '.OO', '..O', '...'],
        "loadingdots": ['L.........', 'Lo........', 'Loa.......', 'Load......', 'Loadi.....', 'Loadin....', 'Loading...', '.oading...', '..ading...',
                        '...ding...', '....ing...', '.....ng...', '......g...', '..........'],
    }
    ends = {
        "period": 5,
        "4thcircle": '✓',  # '◯',
        "classic": 0,
        "o1": 4,
        "o2": 2,
        "loadingdots": 6,
    }
    # dots = ['-', '\\', '|', '/']
    # dots = ['O..', 'OO.', 'OOO', '.OO', '..O', '...']
    # dots = ['L.........', 'Lo........', 'Loa.......', 'Load......', 'Loadi.....', 'Loadin....', 'Loading...', '.oading...', '..ading...',
    #         '...ding...', '....ing...', '.....ng...', '......g...', '..........']
    current = 0

    def dot(self, style: str = "4thcircle"):
        if self.current > (len(self.dots[style])-1):
            self.current = 0
        self.current += 1
        time.sleep(0.1)
        return self.dots[style][self.current-1]

    def done(self, style: str = "4thcircle"):
        end = self.ends[style]
        if isinstance(end, str):
            return end
        return self.dots[style][end]
