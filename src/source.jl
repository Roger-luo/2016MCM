"""
`WaterStorage(W::Real,population::Real)`

water storage

parameter
---
- `W::Real` current water
- `population` population
"""
function WaterStorage(region::Region)
    return NaturalSource(region)+WaterRecycle(region)+WaterProduct(region)
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
    region::Region;
    indrate = 0.15,#industrial water recycle rate
    resrate = 0.15#resident water recycle rate
    )
    return indrate*IndustCost(region)+resrate*ResidentCost(region)
end

"""
```WaterProduct()```

water produce
"""
function WaterProduct(region::Region)
    return 0.1
end

"""
```julia
NaturalSource(W::Real;Wo = 1)
```
natural source
"""
function NaturalSource(region::Region;Wo = 1e2)
    return nature_maxrate*(1-exp(-region.water/Wo))
end