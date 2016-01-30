"""
WaterCost(population::Real)

gross of water cost

parameter
---
- population
"""
function WaterCost(region::Region)
    return IndustCost(region)+AgriCost(region)+ResidentCost(region)
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
function IndustCost(region::Region;poprate = 0.001)
    return poprate*region.population
end

"""
```
AgriCost(population::Real;poprate = 1)
```

Agriculture water cost
"""
function AgriCost(region::Region;poprate = 0.001)
    return poprate*region.population
end

"""
```julia
ResidentCost(population::Real;poprate = 1)
```

Resident water cost
"""
function ResidentCost(region::Region;poprate = 0.001)
    return poprate*region.population
end