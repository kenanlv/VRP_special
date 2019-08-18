from src.solver_google import GoogleLocalSearchSolver, GoogleFirstSolutionSolver
from src.solver_notGoogle import SolverNotGoogle
import json
import matplotlib.pyplot as plt
import numpy as np
from os import listdir

problems = [file.replace(".json", "") for file in listdir('test') if 'json' in file]
Solvers = [GoogleLocalSearchSolver, GoogleFirstSolutionSolver, SolverNotGoogle]
for Solver in Solvers:
    for problem in problems:
        print(f"======{problem}======")
        with open(f"test/{problem}.json") as file:
            data = json.loads(file.read())
        solver = Solver(data["locations"], data["capacities"], data["origins"])
        solution = solver.solve()
        locations = np.array(data["locations"])
        num_locations = len(locations[0])
        num_origins = len(data["origins"])
        plt.plot(locations[0,0:num_origins + 1], locations[1,0:num_origins + 1], 'ro')
        plt.plot(locations[0,num_origins + 1:num_locations + 1], locations[1,num_origins + 1:num_locations + 1], 'kx')
        plt.plot(locations[0][0], locations[1][0], 'bp')
        for path in solution:
            plt.plot(locations[0, path], locations[1, path])
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        plt.savefig(f"test/{problem}_{Solver.__name__}.png", dpi=300)
        plt.clf()

