"""Practice class writing for QZ03."""

class ChristmasTreeFarm:

    plots: list[int]

    def __intit__(self, plots: int, initial_plant: int):
        
        self.plots = []
        i: int = 0
        while (i < initial_plant):
            self.plots.append(1)
            i += 1
        while (i < plots):
            self.plots.append(0)
            i += 1
    
    def plant(self, plot_index: int):
        self.plots[plot_index] = 1
    
    def growth(self):

        for item in self.plots:
            if item != 0:
                self.plots[item] += 1
    
    def harvest(self, replant: bool) -> int:
        
        harvested: int = 0
        for item in self.plots:
            if item >= 5:
                if replant:
                    self.plots[item] = 0
                    harvested += 1
                else:
                    self.plots[item] = 1
                    harvested += 1
        return harvested
    
    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        trees: int = 0

        for item in self.plots:
            if item > 0:
                trees += 1
        for item in rhs.plots:
            if item > 0:
                trees += 1
        
        return ChristmasTreeFarm(len(self.plots) + len(rhs.plots), trees)


class Course:

    name: str
    level: int
    prerequisites: list[str]
    
    def is_valid_course(self, prereq: str) -> bool:

        take: bool = False
        if (self.level >= 400 and self.prerequisites == prereq):
            take = True
        return take


def find_courses(courses: list[Course], prereq: str) -> list[str]:
    cour: list[str] = []

    i: int = 0

    while (i < len(courses)):

        if (courses[i].level >= 400 and courses[i].prerequisites == prereq):
            cour.append(courses[i].name)
        i += 1
    return cour
