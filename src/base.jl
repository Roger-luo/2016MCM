const nature_maxrate = 1;

"""
Region descibe a region

parameters
---
- `population` current populatoin
- `water` current water storage
"""
type Region
    population::Real
    water::Real
    maxpop::Real
    α::Real
    β::Real
    C::Real
end