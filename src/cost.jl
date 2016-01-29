"""
WaterCost(population::Real)

gross of water cost

parameter
---
- population
"""
function WaterCost(region::Region,curability::Real)
    return IndustCost(region,curability)+AgriCost(region,curability)+ResidentCost(region,curability)
end



function gamma(region::Region,curability::Real)
    A = curability
    P = region.population
    maxpop = region.maxpop
    return (exp(A*P/maxpop)/A+exp(maxpop/(A*P))*P/maxpop)/(exp(A*P/maxpop)+exp(maxpop/(A*P)))
end

"""
```
IndustCost(population::Real;poprate = 1)
```

Industrial Cost
"""
function IndustCost(region::Region,curability::Real;poprate = 0.001)
    return poprate*gamma(region,curability)
end

"""
```
AgriCost(population::Real;poprate = 1)
```

Agriculture water cost
"""
function AgriCost(region::Region,curability::Real;poprate = 0.001)
    return poprate*gamma(region,curability)
end

"""
```julia
ResidentCost(population::Real;poprate = 1)
```

Resident water cost
"""
function ResidentCost(region::Region,curability::Real;poprate = 0.001)
    return poprate*gamma(region,curability)
end