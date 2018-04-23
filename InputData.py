
#           Well   Stroke  RIND   MildS  ModSevS   Dead
#
# Well    1 - sum   0.012    0      0       0        ?
# Stroke                   0.091  0.425   0.402    0.082
# RIND                      1.0
# MildS                            1.0
# ModSevS                                  1.0
# Dead                                              1.0

ALPHA = 0.05
DISCOUNT_RATE = 0.03
DELTA_T = 1
POP_SIZE = 10000
SIM_LENGTH = 35

TRANS_MATRIX_WARFARIN = [

]

TRANS_MATRIX_D110 = [

]

TRANS_MATRIX_D120 = [

]

# annual cost of medications
COST_WARFARIN = 474.55   # medication cost + 14 INR monitoring annually
COST_DABIGATRAN_110 = 3467.50
COST_DABIGATRAN_150 = 4745

# cost of events
COST_STROKE_TIA = 5780    # transient ischemic attack
COST_STROKE_M = 8769      # minor ischemic neurologic event
COST_STROKE_MS = 13020    # moderate to severe ischemic neurologic event

# annual cost
COST_STATE = [
    0,      # Well
    0,      # TIA
    0,      # Stroke
    0,      # RIND
    2350,   # Minor Stroke
    5120,   # Moderate to Severe Stroke
    0       # Stroke Death
]

UTILITIES_STATE = [
    0.998,   # Well
    0,       # TIA
    0,       # Stroke
    0.998,   # RIND
    0.75,    # Minor Stroke
    0.39,    # Moderate to Severe Stroke
    0        # Stroke Death
]

# NOTES: (1) Costs are in 2008 US dollars
