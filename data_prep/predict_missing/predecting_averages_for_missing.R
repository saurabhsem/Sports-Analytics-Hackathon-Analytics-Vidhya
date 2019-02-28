tw=read.csv("2018_no_missing.csv")
avg_runs<-tw[,c(5,6,16,17,18,19,12)]
avg_balls<-tw[,c(5,6,16,17,18,19,13)]
avg_wickets<-tw[,c(5,6,16,17,18,19,14)]
avg_xtras<-tw[,c(5,6,16,17,18,19,15)]

classifier = svm(formula = avg_runs$A_Avg_Runs ~ .,
                 data = avg_runs,
                 type = 'nu-regression',
                 kernel = 'polynomial'
)


#finding missing
avg_mis=read.csv("find_a.csv")
#avg_runs
runs=avg_mis[,c(4,5,17,18,19,20,12)]
#avg_balls
balls=avg_mis[,c(4,5,17,18,19,20,13)]
#avg_wickets
wickets=avg_mis[,c(4,5,17,18,19,20,14)]
#avg_xtras
xtras=avg_mis[,c(4,5,17,18,19,20,15)]

pred_runs=predict(runs_1,newdata = runs)
pred_balls=predict(runs_1,newdata = balls)
pred_wickets=predict(runs_1,newdata = wickets)
pred_xtras=predict(runs_1,newdata = xtras)


