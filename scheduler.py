from pulp import LpMaximize, LpProblem, LpVariable

def optimize_ess(solar_pred, load_pred):
    """ 간단한 ESS 스케줄링 (최적화 기반) """
    problem = LpProblem("ESS_Optimization", LpMaximize)
    
    charge = LpVariable("Charge", 0, 100)
    discharge = LpVariable("Discharge", 0, 100)

    # 목적 함수: ESS 활용 극대화
    problem += charge - discharge, "Maximize Storage Utilization"

    # 제약 조건
    problem += charge - discharge <= solar_pred - load_pred, "Balance Supply & Demand"
    
    problem.solve()
    
    return {"charge": charge.varValue, "discharge": discharge.varValue}
