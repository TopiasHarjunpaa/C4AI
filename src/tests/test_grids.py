# Almost empty
G_AE1 = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]]

# Vertical win for player 1
G_VE1 = [[0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 2, 0, 0, 0],
         [0, 2, 0, 2, 0, 0, 0],
         [0, 1, 2, 2, 0, 0, 0]]

# Horizontal win for player 2
G_HO1 = [[0, 2, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 1, 0, 2, 0, 0, 0],
         [0, 2, 2, 2, 2, 0, 0],
         [0, 1, 2, 2, 1, 1, 1]]

# Increasing diagonal win for player 2
G_UD1 = [[0, 2, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 2, 1],
         [0, 1, 0, 2, 2, 0, 2],
         [0, 2, 2, 2, 1, 1, 2],
         [0, 1, 2, 2, 1, 1, 1]]

# Decreasing diagonal win for player 1
G_DD1 = [[0, 2, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 1, 0, 2, 1, 0, 2],
         [0, 2, 2, 2, 1, 1, 2],
         [0, 1, 2, 2, 1, 1, 1]]

# Semi-full grid without winner
G_SF1 = [[0, 2, 2, 0, 0, 2, 2],
         [0, 1, 1, 0, 0, 1, 1],
         [0, 1, 2, 1, 1, 1, 2],
         [0, 1, 1, 2, 2, 1, 2],
         [0, 2, 2, 2, 1, 2, 2],
         [0, 1, 2, 2, 1, 1, 1]]

# Full grid without winner
G_WO1 = [[1, 2, 2, 2, 1, 2, 2],
         [2, 1, 1, 1, 2, 1, 1],
         [2, 1, 2, 1, 1, 1, 2],
         [1, 1, 1, 2, 2, 1, 2],
         [1, 2, 2, 2, 1, 2, 2],
         [2, 1, 2, 2, 1, 1, 1]]