from services.simulation_service import SimulationService


def main():
    """Start game simulation
    """

    simulation = SimulationService(7, 30)
    simulation.simulate_intermediate_vs_advanced()
    #simulation.simulate_advanced_vs_intermediate()
    #simulation.simulate_advanced_vs_advanced()

if __name__ == "__main__":
    main()
