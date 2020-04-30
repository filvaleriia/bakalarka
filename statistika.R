table<-read.csv("/home/valeriia/bakalarka/bakalarka/table_for_R.csv", header = T)

table['MCC.cl.']
table['MCC.reg..']

summary(table)
boxplot(table['MCC.cl.'])
boxplot(table['MCC.reg..'])

t.test(table['MCC.cl.'],table['MCC.reg..'], alternative = "two.sided",conf.level=0.95)