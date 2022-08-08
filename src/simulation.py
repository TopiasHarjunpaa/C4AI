import time
from services.bitboard_service import BitboardService
from services.board_service import BoardService
from services.situation_service import SituationService
from services.ai_service import AiService
from tests.test_grids import G_1W1, G_1W2, G_AE1, G_AE2, G_AE3, G_AE4, G_EG1, G_MG1, G_MG2, G_SF1, G_SF2


def main():
    """Start game simulation
    """
    board = BoardService(640, 480)
    bitboard = BitboardService()
    situation_service = SituationService(board)
    ai_service = AiService(situation_service)
    grids = (G_1W1, G_1W2, G_AE1, G_AE2, G_AE3, G_AE4, G_SF1, G_SF2, G_EG1, G_MG1, G_MG2)
    
    #start_time = time.time()
    #print("Starting simulation Minimax simulation")
    #for grid in grids:
    #    ai_service.calculate_next_move_minimax(grid, 1, 7)
    #end_time = time.time()
    #print("Minimax simulation ended.")
    #print(f"Time spend for simulation {end_time - start_time}")

    #print("Starting id simulation with 10s timeout")
    #ai_service.calculate_next_move_id_minimax(situation_service.get_game_grid(), 1)
    ai_service.calculate_next_move_id_minimax(G_MG2, 1)
    #ai_service.calculate_next_move_id_minimax(G_1W1, 1)
    #ai_service.calculate_next_move_id_minimax(G_SF2, 1)
    #print("Simulation ended")

if __name__ == "__main__":
    main()
