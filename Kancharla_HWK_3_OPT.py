from __future__ import division
from pyomo.environ import *
from pyomo.opt import SolverFactory

## constants and assumptions

# capital costs for solar, and energy storage systems
solar_cap_cost = 800000000  # $/GW
wind_cap_cost  = 1200000000 # $/GW
ESS_p_cap_cost = 200000000  # $/GW
ESS_e_cap_cost = 150000000  # $/GWh

# energy storage operational assumptions
ESS_min_level = 0.20 # %, minimum level of discharge of the battery
ESS_eta_c = 0.95 # ESS charging efficiency, looses 5% when charging
ESS_eta_d = 0.9 # ESS discharging efficiency, looses 10% when discharging
ESS_p_var_cost = 5000 # ESS discharge cost $/GWh
#curtailment_cost = 0.001 # curtailment penalty $/kWh

