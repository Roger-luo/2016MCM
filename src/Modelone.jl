module Modelone

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
    α::Real
    β::Real
    C::Real
end

"""
WaterCost(population::Real)

gross of water cost

parameter
---
- population
"""
function WaterCost(population::Real)
    return IndustCost(population)+AgriCost(population)+ResidentCost(population)
end

"""
`WaterStorage(W::Real,population::Real)`

water storage

parameter
---
- `W::Real` current water
- `population` population
"""
function WaterStorage(W::Real,population::Real)
    return NaturalSource(W)+WaterRecycle(population)+WaterProduct()
end

"""
```julia
WaterRecycle(
    population::Real;
    indrate = 0.2,#industrial water recycle rate
    resrate = 0.2#resident water recycle rate
    )
```

water recycle rate

parameter
---
- `population` population
- `indrate` rate of industrial water recycle
- `resrate` rate of resident  water recycle
"""
function WaterRecycle(
    population::Real;
    indrate = 0.2,#industrial water recycle rate
    resrate = 0.2#resident water recycle rate
    )
    return indrate*IndustCost(population)+resrate*ResidentCost(population)
end

"""
```WaterProduct()```

water produce
"""
function WaterProduct()
    return 2
end

"""
```julia
NaturalSource(W::Real;Wo = 1)
```
natural source
"""
function NaturalSource(W::Real;Wo = 1e4)
    return nature_maxrate*(1-exp(-W/Wo))
end

"""
```
IndustCost(population::Real;poprate = 1)
```

Industrial Cost
"""
function IndustCost(population::Real;poprate = 1)
    return poprate*population
end

"""
```
AgriCost(population::Real;poprate = 1)
```

Agriculture water cost
"""
function AgriCost(population::Real;poprate = 1)
    return poprate*population
end

"""
```julia
ResidentCost(population::Real;poprate = 1)
```

Resident water cost
"""
function ResidentCost(population::Real;poprate = 1)
    return poprate*population
end

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
function EvoPop(region::Region;PopulationIncreaseRate=0.05,dt=1,max=1)
    pop = region.population
    return pop+PopulationIncreaseRate*dt*pop*(1-pop/(max*(1-exp(-ability(region)/1))))
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
function EvoWater(curWater::Real,curpop::Real;dt=1,ext=100,γ=0.2)
    temp = dt*(ext-NaturalSource(curWater)+γ*AgriCost(curpop))
    @show NaturalSource(curWater)
    return curWater+temp
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
function ability(region::Region;α=1,β=1,C=1)
    Wco = 100;Wso = 100;
    return β*exp(α*WaterCost(region.population)/Wco-WaterStorage(region.water,region.population)/Wso)+C
end

"""
```
EvoRegion(region::Region,time::Real;dt=1,max=200,PopulationIncreaseRate=0.5)
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
function EvoRegion(region::Region,time::Real;dt=0.1,max=200,PopulationIncreaseRate=0.5)
    p = region.population
    water = region.water

    pdata = Array(Float64,0)
    wdata = Array(Float64,0)

    push!(pdata,p)
    push!(wdata,water)
    #evolute the population
    for i=1:dt:time
        p = EvoPop(region,PopulationIncreaseRate=PopulationIncreaseRate,dt=dt,max=max)
        water = EvoWater(water,p,dt=dt)
        push!(pdata,p)
        push!(wdata,water)
    end

    region.population = p
    region.water = water

    return ability(region,α=region.α,β=region.β,C=region.C),pdata,wdata
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
testR = Region(10,10,1,2,3)

ability,pdata,wdata = EvoRegion(testR,100,dt=0.1,PopulationIncreaseRate=0.05,max=400)

plot(wdata)
show()