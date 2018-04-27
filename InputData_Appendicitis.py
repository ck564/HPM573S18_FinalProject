

ALPHA = 0.05
DISCOUNT_RATE = 0.03
DELTA_T = 1 / 52
POP_SIZE = 10000
SIM_LENGTH = 95


#                 Scrn   AppR   AppNR    AppRMD    Disc    Well    Cancer    Dead
#   Scrn            0      x      x         0        x       0        0        0
#   AppR            0      0      0         0        0       x        0        x
#   AppNR           0      0      0         0        0       x        0        x
#   AppRMD          0      0      0         0        0       x        0        x
#   Disc            0      0      0         x        0       x        0        0
#   Well            0      0      0         0        0       x     bg for US   bg
#   Cancer          0      0      0         0        0       0        x        x
#   Dead            0      0      0         0        0       0        0        1

# Female, US, average cancer, average death
MATRIX_F_US = [
    [0.00, .195, .309, 0.00, .496, 0.00, 0.00, 0.00],
    [0.00, 0.00, 0.00, 0.00, 0.00, .983, 0.00, .017],
    [0.00, 0.00, 0.00, 0.00, 0.00, .998, 0.00, .002],
    [0.00, 0.00, 0.00, 0.00, 0.00, .983, 0.00, .017],
    [0.00, 0.00, 0.00, .053, 0.00, .947, 0.00, 0.00],
    [0.00, 0.00, 0.00, 0.00, 0.00,     , .000261, bg ],
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00,           ],
    [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00]
]

COST_F_US = [
    342,    # US Scrn
    20072,  # Appendicitis Rupture
    10361,  # Appendicitis w/o Rupture
    20072,  # Appendicitis Rupture after Mis-diagnosis
    0,      # Discharge
    0,      # Well
    50857,  # Cancer
    0       # Dead
]

UTIL_F_US = [
    0.90,
    0.73,
    0.73,
    0.73,
    0.90,
    0.90,
    0.83,
    0
]


# Male, US, average cancer, average death
# Female, CT, average cancer, average death
# Male, CT, average cancer, average death
# Female, USCT, average cancer, average death
# Male, USCT, average cancer, average death


# What is our effectiveness measure?
# Have to factor in misdiagnosis because that increases cost of appendicitis
# Background death and background cancer
# Remission for cancer


# NOTES:
# 1. Weighed the cancer rates to get weights for average cost
# Female
#   Bladder = 0.153 * 89728
#   Breast = 0.084 * 78548
#   Colon = 0.167 * 46275
#   Leukemia = 0.084 * 48666
#   Lung = 0.253 * 45439
#   Stomach = 0.257 * 28088

# 2. Age depedent utilities were averaged









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
