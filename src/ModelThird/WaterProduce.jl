function EvoWaterStorage(region::Region,time::Real,ExpectIncrease::Function;dt=1e-3)
    for i=0:dt:time
        WaterStorageNext(region,)
end

function IncreaseRate(region::Real,cost::Real,supply::Real)
    return (region.WaterStorage+supply-cost)/region.WaterStorage
end

function CostNext(region::Region,dt)
    return region.cost+region.cost*region.averagecost*deltaPop(region,dt)
end

function deltaPop(region::Region,dt::Real)
    return region.population*(region.birthrate*(1-region.population/PopCapacity(region))*dt+gamma*sqrt(dt)*randn())
end

function EvoPop(region::Region,initCapacity::Real,initWaterStorage::Real,dt::Real,gamma::Real)

function PopCapacity(region::Region)
    return region.initCapacity*exp((region.WaterStorage-Thirsty)/region.initWaterStorage)
end


function WaterStorageNext(region::Region,ExpectIncrease::Real,Risk::Real,dt)
    return region.WaterStorage+(ExpectIncrease*dt+Risk*sqrt(dt)*randn())*region.WaterStorage
end