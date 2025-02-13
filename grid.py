from constants import*

class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.columns = self.width // self.cell_size
        self.rows = self.height // self.cell_size
        # Opprett et grid (liste av lister) som definerer om cellene er blokkert eller ikke
        self.grid = [[False for _ in range(self.columns)] for _ in range(self.rows)]

    def is_blocked(self, x, y):
        # Finn ut hvilken celle spilleren er i
        col = int(x // self.cell_size)
        row = int(y // self.cell_size)
        # Returner om denne cellen er blokkert
        if 0 <= col < self.columns and 0 <= row < self.rows:
            return self.grid[row][col]
        return False

    def set_block(self, x, y, blocked):
        # Sett om en bestemt celle er blokkert eller ikke
        col = int(x // self.cell_size)
        row = int(y // self.cell_size)
        if 0 <= col < self.columns and 0 <= row < self.rows:
            self.grid[row][col] = blocked

# Opprett grid for hver bakgrunn
house_grid = Grid(WIDTH, HEIGHT, 90)  
coast_grid = Grid(WIDTH, HEIGHT, 90) # 90 x 90 tilsvarer 2 x 2 ruter på bildene 
camp_grid = Grid(WIDTH, HEIGHT, 90)
cave_grid = Grid(WIDTH, HEIGHT, 90)

# Eksempel på hvordan du setter celler som blokkert (kan endres dynamisk basert på bilder eller områder)
# house_grid.set_block(x = 100, y = 100, True)
# house_grid.set_block(100,100, True)  # Setter en celle som blokkert (x=100, y=100)
# coast_grid.set_block(200, 150, True)