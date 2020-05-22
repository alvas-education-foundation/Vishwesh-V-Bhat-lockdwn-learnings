genreads={"day before": 8.7,"yesterday": 7.7,"today": 7.9}
conreads={"day before": 10.3,"yesterday": 8.7,"today": 9.6}
conreads.update(tom=9)
gensum=sum(genreads.values())
genlen=len(genreads.values())
genmean=gensum/genlen
consum=sum(conreads.values())
conlen=len(conreads.values())
conmean=consum/conlen
exval= conmean-genmean
print("Consumption exceeds generation by - ".upper(),exval)
print("Three days of generation = ".upper(),genreads)
print("Three days of consumption = ".upper(),conreads)
x=("The mean of three days solar generation readings - ").upper()
y=("The mean of three days power consumption readings - ").upper()
print(x,genmean)
print(y,conmean)