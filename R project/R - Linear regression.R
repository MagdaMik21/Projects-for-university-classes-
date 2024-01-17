

install.packages("data.table")
library(data.table)
dane=fread("http://theta.edu.pl/wp-content/uploads/2023/10/anemiaMale.csv")

dane[is.na(dane)] <- NA


dane <- dane[complete.cases(dane), ]


head(dane)

nowe = dane$Weight / ((dane$Height/100 )^2)
head(nowe)




cor(dane$age, dane$Creatinine) 




#MODEL REGRESJI LINIOWEJ

reg = lm(Creatinine~age, data=dane)
reg


#OCENA DOPASOWANIA MODELU 

summary(lm(Creatinine~age, data=dane))

AIC(reg)
#wartość - 101.8141 

BIC(reg)
#wartość - 109.9155


#SPRAWDZENIE ROZKŁADU NORMALNEGO 

hist(reg$residuals)

shapiro.test(reg$residuals)

#WIZUALIZACJA ZALEŻNOŚCI MIĘDZY DANYMI 

plot(dane$age, dane$Creatinine)

abline(reg, lwd=2, col='red')

reg2 = lm(Creatinine~age+Hemoglobin, data=dane)
reg2
#Creat = -0.391081  + 0.019430*age - 0.006349*Hemoglobin

summary(reg2)


hist(reg2$residuals)
shapiro.test(reg2$residuals)

#Creat = -0.391081  + 0.019430*age - 0.006349*Hemoglobin = 1.294512

