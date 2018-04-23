from enum import Enum
import InputData as Data


class HealthStates(Enum):
    """Health states of patients with AF"""
    Well = 0
    TIA = 1         # transient ischemic attack; temporary state
    STROKE = 2      # stroke event; temporary state
    RIND = 3        # reversible ischemic neurologic event
    MSTROKE = 4     # mild stroke
    SSTROKE = 5     # moderate to severe stroke
    DEAD = 6        # dead


class Treatment(Enum):
    WARFARIN = 0
    DABIGATRAN_110 = 1
    DABIGATRAN_150 = 2


class ParametersFixed:
    def __init__(self, treatment):

        self._treatment = treatment  # selected treatment option
        self._delta_t = Data.DELTA_T  # simulation time step
        self._initialHealthState = HealthStates.Well  # initial patient health state

        # transition probability matrix of selected treatment
        self._prob_matrix = []

        # calculate transition probabilities depending on selected treatment
        if treatment == Treatment.WARFARIN:
            self._prob_matrix = Data.TRANS_MATRIX_WARFARIN
        elif treatment == Treatment.DABIGATRAN_110:
            self._prob_matrix = Data.TRANS_MATRIX_D110
        else:
            self._prob_matrix = Data.TRANS_MATRIX_D120

        # annual state costs and utilities
        self._annualStateCosts = Data.COST_STATE
        self._annualStateUtilities = Data.UTILITIES_STATE

        # annual treatment cost
        if self._treatment == Treatment.WARFARIN:
            self._annualTreatmentCost = Data.COST_WARFARIN
        elif self._treatment == Treatment.DABIGATRAN_110:
            self._annualTreatmentCost = Data.COST_DABIGATRAN_110
        else:
            self._treatment = Data.COST_DABIGATRAN_150

        # adjusted discount rate
        self._adjDiscountRate = Data.DISCOUNT_RATE * Data.DELTA_T

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
            return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
            return self._annualStateUtilities[state.value]

    def get_annual_treatment_cost(self):
        return self._annualTreatmentCost

    def get_adj_discount_rate(self):
        return self._adjDiscountRate





