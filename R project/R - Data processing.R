
dane = read.table('http://theta.edu.pl/wp-content/uploads/2023/10/anemiaMale.csv',header=TRUE,sep=';',dec=',')
head(dane)
#czyste wczytanie danych 

dane$City[dane$City == '-9'] = NA
dane$Hemoglobin[dane$Hemoglobin == 0] = NA
summary(dane$Hemoglobin)


dane2=dane[c(42:103),c(2:8,10)]


#WYZNACZENIE ŚREDNIEGO POZIOMU HEMOGLOBINY W KAŻDYM Z MIAST I PŁCI
a1=aggregate(dane$Hemoglobin, by=list(dane$City, dane$Sex), FUN='mean', na.rm = TRUE)
a2 =aggregate(dane$Hemoglobin, by=list(dane$City), FUN='mean', na.rm = TRUE)


#POŁĄCZENIE DANYCH W JEDNĄ RAMKĘ
merge(a1,a2, by='Group.1')



hist(dane$Height)

hist(dane$Height, xlab='wzrost', ylab='ilość osób', main='Histogram wzrostu')


?cor

#WYZNACZENIE WSPÓŁCZYNNIKA KORELACJI I JEGO WARTOŚCI 
a=cor.test(dane$VitB12, dane$Hemoglobin, use='complete.obs', method='pearson')
summary(a)

