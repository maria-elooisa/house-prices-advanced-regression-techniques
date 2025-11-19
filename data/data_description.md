### 🏠 **MSSubClass** – Tipo de residência envolvida na venda

* 20: Casa térrea (pós-1946, todos os estilos)
* 30: Casa térrea (até 1945)
* 40: Térrea com sótão finalizado (todas idades)
* 45: 1,5 andares – sótão inacabado
* 50: 1,5 andares – sótão finalizado
* 60: 2 andares (pós-1946)
* 70: 2 andares (até 1945)
* 75: 2,5 andares (todas idades)
* 80: Casa dividida ou em múltiplos níveis
* 85: Split Foyer
* 90: Duplex (todos estilos e idades)
* 120: Térrea em condomínio planejado (pós-1946)
* 150: 1,5 andares em condomínio planejado
* 160: 2 andares em condomínio planejado (pós-1946)
* 180: Condomínio multi-nível
* 190: Conversão para duas famílias

---

### 🏘️ **MSZoning** – Zoneamento geral da propriedade

* A: Agrícola
* C: Comercial
* FV: Residencial em Vila Flutuante
* I: Industrial
* RH: Residencial alta densidade
* RL: Residencial baixa densidade
* RP: Residencial parque de baixa densidade
* RM: Residencial média densidade

---

### 📐 **Características do lote e acesso**

* **LotFrontage**: Metros lineares de frente para a rua
* **LotArea**: Tamanho do lote em pés²
* **Street**: Tipo de rua (Grvl = Cascalho, Pave = Asfalto)
* **Alley**: Tipo de acesso por beco (Grvl = Cascalho, Pave = Asfalto)
* **LotShape**: Formato do lote (Reg = Regular, IR1 a IR3 = Irregularidades)
* **LandContour**: Nível do terreno (Lvl = Plano, Bnk = Elevado, etc.)
* **Utilities**: Utilidades disponíveis (Ex: água, esgoto, eletricidade)
* **LotConfig**: Configuração do lote (Ex: esquina, cul-de-sac)
* **LandSlope**: Inclinação do terreno (Gtl = Leve, Mod = Moderada, Sev = Forte)

---

### 📍 **Localização e vizinhança**

* **Neighborhood**: Nome do bairro
* **Condition1/Condition2**: Proximidade com ruas, trilhos, parques, etc.

---

### 🧱 **Tipo e estilo da construção**

* **BldgType**: Tipo de edificação (Ex: Casa isolada, duplex, townhouse)
* **HouseStyle**: Estilo da casa (Ex: 1 and., 2 and., split level, etc.)
* **OverallQual/Cond**: Qualidade e condição geral da casa (1 = Muito ruim, 10 = Excelente)
* **YearBuilt / YearRemodAdd**: Ano de construção / reforma

---

### 🏠 **Cobertura e exterior**

* **RoofStyle**: Estilo do telhado
* **RoofMatl**: Material do telhado
* **Exterior1st / Exterior2nd**: Material de revestimento externo
* **MasVnrType / MasVnrArea**: Tipo e área da fachada de alvenaria
* **ExterQual / ExterCond**: Qualidade e condição do exterior

---

### 🏗️ **Fundação e porão (basement)**

* **Foundation**: Tipo de fundação
* **BsmtQual / BsmtCond**: Altura e condição do porão
* **BsmtExposure**: Exposição ao nível do solo
* **BsmtFinType1/2**: Tipo de área acabada do porão
* **BsmtFinSF1/2 / BsmtUnfSF / TotalBsmtSF**: Metros² de áreas acabadas/não-acabadas

---

### 🔥 **Aquecimento e elétrico**

* **Heating / HeatingQC**: Tipo e qualidade do aquecimento
* **CentralAir**: Ar condicionado central (Y/N)
* **Electrical**: Tipo de sistema elétrico

---

### 🧱 **Área útil**

* **1stFlrSF / 2ndFlrSF**: Área útil no primeiro e segundo andares
* **LowQualFinSF**: Área útil de baixa qualidade
* **GrLivArea**: Área total acima do solo (living area)

---

### 🚿 **Banheiros e quartos**

* **BsmtFullBath / BsmtHalfBath**: Banheiros no porão
* **FullBath / HalfBath**: Banheiros acima do solo
* **Bedroom / Kitchen**: Número de quartos e cozinhas
* **KitchenQual**: Qualidade da cozinha
* **TotRmsAbvGrd**: Total de cômodos acima do solo (exclui banheiros)

---

### 🛠️ **Funcionalidade e lareira**

* **Functional**: Funcionalidade geral da casa
* **Fireplaces / FireplaceQu**: Número e qualidade das lareiras

---

### 🚗 **Garagem**

* **GarageType / GarageYrBlt / F**: Tipo, ano e acabamento da garagem
* **GarageCars / GarageArea**: Capacidade e área da garagem
* **GarageQual / GarageCond**: Qualidade e condição da garagem
* **PavedDrive**: Entrada pavimentada (Y/P/N)

---

### 🛋️ **Áreas adicionais**

* **WoodDeckSF / OpenPorchSF / EnclosedPorch / 3SsnPorch / ScreenPorch**: Áreas de deck e varandas
* **PoolArea / PoolQC**: Área e qualidade da piscina
* **Fence**: Tipo de cerca
* **MiscFeature / MiscVal**: Outras estruturas (ex: galpão, quadra de tênis)

---

### 📅 **Venda**

* **MoSold / YrSold**: Mês e ano da venda
* **SaleType**: Tipo de venda (financiada, à vista, judicial etc.)
* **SaleCondition**: Condição da venda (normal, familiar, inacabada, etc.)
