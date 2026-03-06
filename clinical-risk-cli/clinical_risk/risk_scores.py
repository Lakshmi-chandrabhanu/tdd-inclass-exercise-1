# TODO: First write the purpose, the ins and outs, and the placeholder function for the qSOFA score.
# The function name should be qsofa_score, and it should take the following parameters: rr (respiratory rate) (int),
# sbp (systolic blood pressure) (int), and ams (altered mental status) (bool).
# The function should return an int representing the qSOFA score (0-3).

# purpose: qsofa_score accepts respiratory rate, systolic blood pressure, and altered mental status as inputs and calculates the qSOFA score.
# ins & outs: rr (int), sbp (int), ams (bool) -> score (int)
def qsofa_score(rr:int, sbp:int, ams:bool) -> int:
    # Validate inputs
    if rr < 0:
        raise ValueError("Respiratory rate cannot be negative")
    if sbp < 0:
        raise ValueError("Systolic blood pressure cannot be negative")
    
    score = 0
    
    # Check if respiratory rate >= 22
    if rr >= 22:
        score += 1
    
    # Check if systolic blood pressure <= 100
    if sbp <= 100:
        score += 1
    
    # Check if altered mental status
    if ams:
        score += 1
    
    return score

# TODO: First write the purpose, the ins and outs, and the placeholder function for the CHA2DS2-VASc score.
# The function name should be cha2ds2_vasc_score, and it should take the following parameters: age (int), female (bool),
# chf (congestive heart failure) (bool), htn (hypertension) (bool), dm (diabetes) (bool), stroke (bool),
# vascular (bool).
# The function should return an int representing the CHA2DS2-VASc score.

# purpose: cha2ds2_vasc_score calculates the CHA2DS2-VASc score for atrial fibrillation stroke risk
# ins: age (int), female (bool), chf (bool), htn (bool), dm (bool), stroke (bool), vascular (bool)
# outs: score (int) representing CHA2DS2-VASc score
def cha2ds2_vasc_score(age: int, female: bool, chf: bool, htn: bool, dm: bool, stroke: bool, vascular: bool) -> int:
    # Validate inputs
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    score = 0
    
    # Age scoring
    if age >= 75:
        score += 2
    elif age >= 65:
        score += 1
    
    # Female sex
    if female:
        score += 1
    
    # Congestive heart failure
    if chf:
        score += 1
    
    # Hypertension
    if htn:
        score += 1
    
    # Diabetes mellitus
    if dm:
        score += 1
    
    # Stroke/TIA/thromboembolism (2 points)
    if stroke:
        score += 2
    
    # Vascular disease
    if vascular:
        score += 1
    
    return score
