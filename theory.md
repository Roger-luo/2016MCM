# 基本供求关系

## 定义

总量不好进行衡量，价格应与速率相关，所以主要以不同量变化的速率作为定价依据

- 当前储水总量 $W_s$ :当前该地区所能调用的水(不包括未来可能调用到的水所带来的收益)
- 水资源消耗速率 $W_c$：当前该地区耗水速率
- 政府基本定价 $P$：该地区的基本价格，可以作为政策调整的一个变量


$$
Ability = \beta\cdot e^{\frac{\alpha\cdot W_c-W_s}{W_0}} + Policy
$$

## 依赖关系

- $W_{ns}$: 自然水资源速率
- $W_{rs}$: 技术回收速率
- $W_{ps}$: 技术生产速率
- $W_{ic}$: 工业用水速率
- $W_{ac}$: 农业用水速率
- $W_{rc}$: 生活用水速率
- $P$: 人口

$$
W_s=W_{ns}+W_{rs}+W_{ps}\\
W_c=W_{fc}+W_{ac}+W_{rc}\\
W_{s}=W_{c}\\
W_{rs}(W_{ic},W_{rc},A) = \alpha_{ic}\cdot W_{ic}+\alpha_{rc}\cdot W_{rc}\\
W_{ps}(A) = const\\
W_{ns}(W) = \omega_{max}(1-e^{-\frac{W}{W_{0}}})\\
W_{ic}(P,A) = \alpha_{icp}\cdot P\\
W_{ac}(P,A) = \alpha_{acp}\cdot P\\
W_{rc}(P,A) = \alpha_{rcp}\cdot P\\
\frac{dP}{dt} = \lambda P(1-\frac{P}{K(1-e^{-\frac{A}{A_{0}}})})\\
\frac{dW}{dt}=ext-W_{ns}+\gamma\cdot W_{ac}\\
$$