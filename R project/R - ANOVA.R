
install.packages('data.table')
library(data.table)
dane = fread('http://theta.edu.pl/wp-content/uploads/2020/10/genomes.csv')
head(dane)

dane$habitat[dane$habitat == ''] = NA
length(dane$habitat)

length(na.omit(dane$habitat))

dane = na.omit(dane)
dim(dane)
dane$GC[dane$GC == 0] = NA
dane$size[dane$size == '.'] = NA
dane$size = as.numeric(dane$size)
#trzeba było zmienić na wartości liczbowe elementy z tej kolumny 
dane$size[is.na(dane$size)] <- mean(dane$size, na.rm=TRUE)
head(dane)

dane$group <- as.factor(dane$group)
dane$habitat <- as.factor(dane$habitat)

x=boxplot(dane$size~dane$habitat)

#SPRAWDZENIE ZAŁOŻEŃ O JEDNORODNOŚCI WARIANCJI POMIĘDZY GRUPAMI 

install.packages("car")
library(car)
leveneTest(dane$size~dane$habitat)

model1 = aov(GC~habitat, data=dane)
summary(model1)
model2 = aov(GC~habitat+group, data = dane)
summary(model2)
model3 = aov(GC~habitat*group, data = dane)
summary(model3)

shapiro.test(model1$residuals)
shapiro.test(model2$residuals)
shapiro.test(model3$residuals)

TukeyHSD(model1)

ph_2 <- TukeyHSD(model2)
ph_2$habitat
ph_2$group

ph_1 <- TukeyHSD(model1)
plot(ph_1)


AIC(model1)
AIC(model2)
AIC(model3)
