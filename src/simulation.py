import sys
from services.simulation_service import SimulationService


def simulate():
    """Simulates three different game scenarios between the different AI implementations:
    1.  intermediate AI vs advanced AI
    2.  advanced AI vs intermediate AI
    3.  advanced AI vs advanced AI
    Results will be plotted after each simulation. Arguments can be used to determine
    intermediate AI search depth and advanced AI timeout limit.
    """

    intermediate_depth = 7
    advanced_timeout = 30
    if len(sys.argv) == 3:
        intermediate_depth = float(sys.argv[1])
        advanced_timeout = float(sys.argv[2])
    simulation = SimulationService(intermediate_depth, advanced_timeout)
    simulation.simulate_intermediate_vs_advanced()
    simulation.simulate_advanced_vs_intermediate()
    simulation.simulate_advanced_vs_advanced()

if __name__ == "__main__":
    simulate()
