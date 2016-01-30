module BlackSchole

function BlackScholeNext(S,r,σ;dt=1e-3)
    return S+(r*dt+σ*sqrt(dt)*randn())S
end

export BlackScholeNext

end

using BlackSchole
using PyPlot

figure(1)

data = Array(Float64,0)
S = 2
for i=1:100
    S = BlackScholeNext(S,2,0.3)
    push!(data,S)
end

plot(data)
show()