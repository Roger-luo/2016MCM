const nature_maxrate = 1;

type Region
    population
    water
    α
    β
    C
end

function WaterCost(population)
    return IndustCost(population)+AgriCost(population)+ResidentCost(population)
end

function WaterStorage(W,population)
    return NaturalSource(W)+WaterRecycle(population)+WaterProduct()
end

function WaterRecycle(
    population;
    indrate = 0.2,#industrial water recycle rate
    resrate = 0.2#resident water recycle rate
    )
    return indrate*IndustCost(population)+resrate*ResidentCost(population)
end

function WaterProduct()
    return 2
end

function NaturalSource(W;Wo = 1)
    return nature_maxrate*(1-exp(-W/Wo))
end

function IndustCost(population;poprate = 1)
    return poprate*population
end

function AgriCost(population;poprate = 1)
    return poprate*population
end

function ResidentCost(population;poprate = 1)
    return poprate*population
end

function EvoPop(region::Region;PopulationIncreaseRate=1,dt=1,max=1)
    pop = region.population
    return pop+PopulationIncreaseRate*dt*pop*(1-pop/(max*(1-exp(-ability(region)/1))))
end

function EvoWater(curWater::Real,curpop::Real;dt=1,ext=100,γ=0.2)
    return curWater+dt*(ext-NaturalSource(curWater)+γ*AgriCost(curpop))
end

function ability(region::Region;α=1,β=1,C=1)
    Wco = 1;Wso = 1;
    return β*exp(α*WaterCost(region.population)/Wco-WaterStorage(region.water,region.population)/Wso)+C
end

testR = Region(100,10,1,2,3)

function EvoRegion(region::Region,time::Real;dt=1,max=100,PopulationIncreaseRate=0.5)
    p = region.population
    water = region.water

    #evolute the population
    for i=1:dt:time
        p = EvoPop(region,PopulationIncreaseRate=PopulationIncreaseRate,dt=dt,max=max)
        water = EvoWater(water,p,dt=dt)
    end

    region.population = p
    region.water = water

    return ability(region,α=region.α,β=region.β,C=region.C)
end

@show EvoRegion(testR,10)