import time
from services.board_service import BoardService
from services.situation_service import SituationService
from services.ai_service import AiService
from tests.test_grids import (G_1W1, G_1W2, G_AE1, G_AE2, G_AE3, G_AE4,
                                G_EG1, G_MG1, G_MG2, G_SF1, G_SF2)


def main():
    """Start game simulation
    """
    board = BoardService(640, 480)
    situation_service = SituationService(board)
    ai_service = AiService(situation_service)
    empty = situation_service.get_game_grid()
    grids = [empty, G_1W1, G_1W2, G_AE1, G_AE2, G_AE3, G_AE4, G_EG1, G_MG1, G_MG2, G_SF1, G_SF2]

    many_simulations(ai_service, grids, 7, 5)
    deep_simulation(ai_service, [empty, G_MG2], 8, 5)

def many_simulations(ai_service, grids, depth, timeout):
    ai_service.printer = False
    id_results = []
    mm_results = []
    print(f"Starting multiple iterative deepening with max depth {depth} and timeout {timeout}s")
    start_time = time.time()
    for grid in grids:
        res = ai_service.calculate_next_move_id_minimax(grid, 1, timeout, depth)
        id_results.append(res)
    print(f"total time spend: {time.time() - start_time} s")
    print("-------------------")
    print("")
    print(f"Starting multiple Minimax with depth {depth}")
    start_time = time.time()
    for grid in grids:
        res = ai_service.calculate_next_move_minimax(grid, 1, depth)
        mm_results.append(res)
    print(f"total time spend: {time.time() - start_time} s")
    print(f"id results: {id_results}")
    print(f"mm results: {mm_results}")
    print("-------------------")
    print("")

def deep_simulation(ai_service, grids, depth, timeout):
    ai_service.printer = True
    print(f"starting Early-game iterative deepening with max depth {depth} and timeout {timeout}s")
    eg_id = ai_service.calculate_next_move_id_minimax(grids[0], 1, timeout, depth)
    print(f"starting Early-game Minimax with depth {depth}")
    eg_mm = ai_service.calculate_next_move_minimax(grids[0], 1, depth)
    print(f"id result: {eg_id} | mm result: {eg_mm}")
    print("")
    print(f"starting Mid-game iterative deepening with max depth {depth} and timeout {timeout}s")
    mg_id = ai_service.calculate_next_move_id_minimax(grids[1], 1, timeout, depth + 2)
    print(f"starting Mid-game Minimax with depth {depth + 2}")
    mg_mm= ai_service.calculate_next_move_minimax(grids[1], 1, depth + 2)
    print(f"id result: {mg_id} | mm result: {mg_mm}")
    print("")

if __name__ == "__main__":
    main()
