from abc import ABC, abstractmethod
import numpy as np
import math
from typing import List


class BaseSolver(ABC):
    def __init__(self, locations, capacities, origins, destination=0):
        self.num_locations = len(locations[0])
        self.distance_matrix = np.zeros((self.num_locations, self.num_locations))
        self.capacities = capacities
        self.origins = origins
        self.destination = destination

        for i in range(self.num_locations):
            for j in range(i):
                self.distance_matrix[i][j] = \
                    math.sqrt((locations[0][i] - locations[0][j]) ** 2 + (locations[1][i] - locations[1][j]) ** 2)
                self.distance_matrix[j][i] = self.distance_matrix[i][j]

    @abstractmethod
    def solve(self) -> List[List[int]]:
        return NotImplemented
