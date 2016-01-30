module Modelone

include("base.jl")
include("source.jl")
include("cost.jl")


"""
```julia
EvoPop(region::Region;PopulationIncreaseRate=1,dt=1,max=1)
```

evolute population

parameters
---
- `region::Region` region object
- `PopulationIncreaseRate=1` population rate of pure increase
- `max=1` maximum population
"""
function EvoPop(region::Region;PopulationIncreaseRate=0.15,dt=0.01)
    pop = region.population
    maxpop = region.maxpop
    return pop+PopulationIncreaseRate*dt*pop*(1-pop/(maxpop*(1-exp(-ability(region)/1))))
end

"""
```
EvoWater(curWater::Real,curpop::Real;dt=1,ext=100,γ=0.2)
```

evolute water storage

parameter
---
- `curWater::Real` current water
- `curpop::Real` current population
- `dt=1` time step
- `ext=100` income water
- `γ=0.2` percent conversion of argriculture water
"""
function EvoWater(region::Region;dt=0.01,ext=0.1,γ=0.15)
    return region.water+dt*(ext-NaturalSource(region)+γ*AgriCost(region))
end

"""
```julia
ability(region::Region;α=1,β=1,C=1)
```

ability gives the evaluation of a given area

parameters
---
- `region::Region` region object
"""
function ability(region::Region)
    Wco = 1;Wso = 1;
    return region.β*exp((WaterStorage(region)/Wso)-(WaterCost(region)/Wco))+region.C
end

"""
```
EvoRegion(region::Region,time::Real;dt=1,maxpop=200,PopulationIncreaseRate=0.5)
```

evolute region

parameters
---
- `region::Region` region object
- `PopulationIncreaseRate=1` population rate of pure increase
- `time` object time
- `dt=1` time step
- `max=200` maximum population
"""
function EvoRegion(region::Region,time::Real;dt=1,PopulationIncreaseRate=0.15)
    pdata = Array(Float64,0)
    wdata = Array(Float64,0)

    push!(pdata,region.population)
    push!(wdata,region.water)
    #evolute the population
    for i=0:dt:time
        region.population = EvoPop(region;PopulationIncreaseRate=PopulationIncreaseRate,dt=dt)
        region.water = EvoWater(region;dt=dt)
        push!(pdata,region.population)
        push!(wdata,region.water)
    end
    return ability(region),pdata,wdata
end
export Region,
    nature_maxrate,
    WaterCost,
    WaterStorage,
    WaterRecycle,
    WaterProduct,
    NaturalSource,
    IndustCost,
    AgriCost,
    ResidentCost,
    EvoPop,
    EvoWater,
    ability,
    EvoRegion

end

using Modelone
using PyPlot

fig = figure(1)
testR = Region(300,1000,1000,1,1,0)

ability,pdata,wdata = EvoRegion(testR,3000,dt=1,PopulationIncreaseRate=0.15)

plot(pdata)
plot(wdata)
show()