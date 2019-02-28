
# coding: utf-8

# In[1]:


#Loading Required Libraries
import csv, pandas as pd


# In[2]:


train_file1 = open("./train/ball_by_ball_data.csv","r")


# In[3]:


index = {}
header = True
match_id = ""
batsman_stats = {}
batsman_stats["ball_faced"] = 0
batsman_stats["Total_runs"] = 0
batsman_stats["Total_extras"] = 0
batsman_stats["out_By"] = 0
batsman_stats["inning"] = 1
batsman_stats["Team"] = ""
batsman_stats["Against"] = ""

bowler_stats = {}
bowler_stats["balls"] = 0
bowler_stats["Total_runs_given"] = 0
bowler_stats["Total_extras_given"] = 0
bowler_stats["Wickets_taken"] = 0
bowler_stats["inning"] = 1
bowler_stats["Team"] = ""
bowler_stats["Team"] = ""

batsman_id = {}
bowler_id = {}
total_extras1 = 0
total_extras2 = 0
match_extras = 0
i =0


# In[4]:


output_file = open("./train/summary_data.csv","w") 
data_bbb = csv.reader(train_file1)
data_summary = csv.writer(output_file)
data_summary.writerow(["Unique_id","Team","Against","Player_ID","inning","batsman_runs","ball_faced","Strike_Rate","Total_extras","out_By","Total_Wickets","Balls","Total_extras_Given"])

for row in data_bbb:
    if header:
        for r in row:
            index[r] = i
            i+=1
        header = False
        continue
    else:
        if str(match_id) != str(row[index["match_id"]]):
            if match_id != "":
                for player_id in batsman_id:
                    if batsman_id[player_id]["inning"] == 1:
                        batsman_id[player_id]["Total_extras"] = total_extras1
                    else:
                        batsman_id[player_id]["Total_extras"] = total_extras2
                    if batsman_id[player_id]["ball_faced"] !=0:
                        strike_rate = float(float(batsman_id[player_id]["Total_runs"])/float(batsman_id[player_id]["ball_faced"]))
                    else:
                        strike_rate = 0.0
                    if player_id in bowler_id:
                        new_row = [match_id+"_"+player_id,batsman_id[player_id]["Team"],batsman_id[player_id]["Against"],player_id,batsman_id[player_id]["inning"],batsman_id[player_id]["Total_runs"],batsman_id[player_id]["ball_faced"],float(strike_rate),batsman_id[player_id]["Total_extras"],batsman_id[player_id]["out_By"],bowler_id[player_id]["Wickets_taken"],bowler_id[player_id]["balls"],bowler_id[player_id]["Total_extras_given"]]
                        data_summary.writerow(new_row)
                    else:
                        new_row = [match_id+"_"+player_id,batsman_id[player_id]["Team"],batsman_id[player_id]["Against"],player_id,batsman_id[player_id]["inning"],batsman_id[player_id]["Total_runs"],batsman_id[player_id]["ball_faced"],float(strike_rate),batsman_id[player_id]["Total_extras"],batsman_id[player_id]["out_By"],"0","0","0"]
                        data_summary.writerow(new_row)
                for player_id in bowler_id:
                    if player_id not in batsman_id:
                        if row[index["inning"]] == 2:
                            new_row = [match_id+"_"+player_id,bowling_id[player_id]["Team"],bowling_id[player_id]["Against"],player_id,bowler_id[player_id]["inning"],"0","0","0",total_extras1,"0",bowler_id[player_id]["Wickets_taken"],bowler_id[player_id]["balls"],bowler_id[player_id]["Total_extras_given"]]
                            data_summary.writerow(new_row)
                        else:
                            new_row = [match_id+"_"+player_id,bowler_id[player_id]["Team"],bowler_id[player_id]["Against"],player_id,bowler_id[player_id]["inning"],"0","0","0",total_extras2,"0",bowler_id[player_id]["Wickets_taken"],bowler_id[player_id]["balls"],bowler_id[player_id]["Total_extras_given"]]
                            data_summary.writerow(new_row)
                batsman_id.clear()
                bowler_id.clear()          
            match_id = row[index["match_id"]]
            batsman_stats = {}
            batsman_stats["ball_faced"] = 0
            batsman_stats["Total_runs"] = 0
            batsman_stats["Total_extras"] = 0
            batsman_stats["out_By"] = 0
            batsman_stats["inning"] = 1
            batsman_stats["Team"] = ""
            batsman_stats["Against"] = ""
            
            bowler_stats = {}
            bowler_stats["balls"] = 0
            bowler_stats["Total_runs_given"] = 0
            bowler_stats["Total_extras_given"] = 0
            bowler_stats["Wickets_taken"] = 0
            bowler_stats["inning"] = 1
            bowler_stats["Team"] = ""
            bowler_stats["Against"] = ""
            
            total_extras1 = 0
            total_extras2 = 0
            match_extras = 0
            
            batsman_id[row[index["batsman_id"]]] = batsman_stats
            bowler_id[row[index["bowler_id"]]] = bowler_stats
            batsman_id[row[index["batsman_id"]]]["Team"] = row[index["batting_team"]]
            batsman_id[row[index["batsman_id"]]]["Against"] = row[index["bowling_team"]]
            bowler_id[row[index["bowler_id"]]]["Team"] = row[index["bowling_team"]]
            bowler_id[row[index["bowler_id"]]]["Against"] = row[index["batting_team"]] 
            
            batsman_id[row[index["batsman_id"]]]["inning"] = int(row[index["inning"]])
            bowler_id[row[index["bowler_id"]]]["inning"] = 3-int(row[index["inning"]])
            batsman_id[row[index["batsman_id"]]]["Total_runs"] += int(row[index["batsman_runs"]])
            bowler_id[row[index["bowler_id"]]]["Total_runs_given"] += int(row[index["batsman_runs"]])
            if int(row[index["extra_runs"]]) != 0:
                batsman_id[row[index["batsman_id"]]]["ball_faced"]+=1
                bowler_id[row[index["bowler_id"]]]["balls"]+=1
            else:
                bowler_id[row[index["bowler_id"]]]["Total_extras_given"]+= int(row[index["extra_runs"]])
                if int(row[index["inning"]])==1:
                    total_extras1 += int(row[index["extra_runs"]])
                else:
                    total_extras2 += int(row[index["extra_runs"]])
                match_extras += int(row[index["extra_runs"]])
            if len(str(row[index["dismissal_kind"]]).strip()) > 0:
                    batsman_id[row[index["batsman_id"]]]["out_By"] = int(row[index["bowler_id"]])
                    bowler_id[row[index["bowler_id"]]]["Wickets_taken"] += 1
        else:
            try:
                batsman_id[row[index["batsman_id"]]]["Total_runs"]+=int(row[index["batsman_runs"]])
                batsman_id[row[index["batsman_id"]]]["inning"] = int(row[index["inning"]])
                if int(row[index["extra_runs"]]) == 0:
                    batsman_id[row[index["batsman_id"]]]["ball_faced"]+=1
                else:
                    if int(row[index["inning"]])==1:
                        total_extras1 += int(row[index["extra_runs"]])
                    else:
                        total_extras2 += int(row[index["extra_runs"]])
                    match_extras += int(row[index["extra_runs"]])
                if len(str(row[index["dismissal_kind"]]).strip()) > 0:
                    batsman_id[row[index["batsman_id"]]]["out_By"] = int(row[index["bowler_id"]])
            except KeyError:
                batsman_stats = {}
                batsman_stats["ball_faced"] = 0
                batsman_stats["Total_runs"] = 0
                batsman_stats["Total_extras"] = 0
                batsman_stats["out_By"] = 0
                batsman_stats["inning"] = int(row[index["inning"]])
                batsman_stats["Team"] = ""
                batsman_stats["Against"] = ""
                batsman_id[row[index["batsman_id"]]] = batsman_stats
                batsman_id[row[index["batsman_id"]]]["Team"] = row[index["batting_team"]]
                batsman_id[row[index["batsman_id"]]]["Against"] = row[index["bowling_team"]]
                batsman_id[row[index["batsman_id"]]]["Total_runs"]+=int(row[index["batsman_runs"]])
                if int(row[index["extra_runs"]]) == 0:
                    batsman_id[row[index["batsman_id"]]]["ball_faced"]+=1
                else:
                    if int(row[index["inning"]])==1:
                        total_extras1 += int(row[index["extra_runs"]])
                    else:
                        total_extras2 += int(row[index["extra_runs"]])
                    match_extras += int(row[index["extra_runs"]])
                if len(str(row[index["dismissal_kind"]]).strip()) > 0:
                    batsman_id[row[index["batsman_id"]]]["out_By"] = int(row[index["bowler_id"]])                    
            try:
                bowler_id[row[index["bowler_id"]]]["Total_runs_given"]+=int(row[index["batsman_runs"]])
                if int(row[index["extra_runs"]]) == 0:
                    bowler_id[row[index["bowler_id"]]]["balls"]+=1
                else:
                    bowler_id[row[index["bowler_id"]]]["Total_extras_given"]+=int(row[index["extra_runs"]])
                if len(str(row[index["dismissal_kind"]]).strip()) > 0:
                    bowler_id[row[index["bowler_id"]]]["Wickets_taken"] +=1
            except:
                bowler_stats = {}
                bowler_stats["balls"] = 0
                bowler_stats["Total_runs_given"] = 0
                bowler_stats["Total_extras_given"] = 0
                bowler_stats["Wickets_taken"] = 0
                bowler_stats["inning"] = 3-int(row[index["inning"]])
                bowler_id[row[index["bowler_id"]]] = bowler_stats
                bowler_id[row[index["bowler_id"]]]["Team"] = row[index["bowling_team"]]
                bowler_id[row[index["bowler_id"]]]["Against"] = row[index["batting_team"]]
                bowler_id[row[index["bowler_id"]]]["Total_runs_given"]+=int(row[index["batsman_runs"]])
                bowler_id[row[index["bowler_id"]]]["inning"] = 3-int(row[index["inning"]])
                if int(row[index["extra_runs"]]) == 0:
                    bowler_id[row[index["bowler_id"]]]["balls"]+=1
                else:
                    bowler_id[row[index["bowler_id"]]]["Total_extras_given"]+= int(row[index["extra_runs"]])
                if len(str(row[index["dismissal_kind"]]).strip()) > 0:
                    bowler_id[row[index["bowler_id"]]]["Wickets_taken"] +=1
                    
output_file.close()
        


# In[5]:


data_summary = pd.read_csv("./train/summary_data.csv")


# In[6]:


d1 = data_summary.groupby(["Team","Against","Player_ID"], as_index=False).mean()
d1 = d1[["Team","Against","Player_ID","batsman_runs","ball_faced","Total_Wickets","Total_extras_Given"]]
d1.columns = ["Team","Against","Player_ID","A_Avg_Runs","A_Avg_balls_Faced","A_Avg_Wickets","A_Avg_Extras"]


# In[7]:


d2 = data_summary.groupby(["Player_ID"], as_index=False).mean()
d2 = d2[["Player_ID","batsman_runs","ball_faced","Total_Wickets","Total_extras_Given"]]
d2.columns = ["Player_ID","O_Avg_Runs","O_Avg_balls_Faced","O_Avg_Wickets","O_Avg_Extras"]


# In[8]:


d4 = d1.merge(d2,how="left", on="Player_ID") 


# In[9]:


d5 = data_summary.merge(d4, how="left", on =["Team","Against","Player_ID"])
d6 = d5['Unique_id'].str.split('_', -1, expand=True)
d6['match_id'] = d6[[0,1]].apply(lambda x: '_'.join(x), axis=1)
d6 = d6[["match_id"]]
d7 = pd.merge(d6, d5, left_index=True, right_index=True)


# In[10]:


d7.to_csv("data_summary_new.csv", index=False)


# In[11]:


add_data = pd.read_csv("./train/match_data.csv")


# In[12]:


d8 = d7.merge(add_data, how ="left", on = "match_id")


# In[16]:


d8.to_csv("data_summary_final.csv", index=False)


# In[45]:


d9 = d8.groupby(["Team","Player_ID","season"], as_index=False).count()
d9 = d9[["Team","Player_ID","season","Unique_id"]]


# In[51]:


d10 = d8.drop_duplicates(subset=["match_id","Team"])
d10 = d10.groupby(["Team","season"], as_index=False).count()
d10 = d10[["Team","season","match_id"]]


# In[72]:


d11 = d9.merge(d10, how="left", on= ["Team", "season"])


# In[73]:


d11["Playing_Ratio"] = d11["Unique_id"]/d11["match_id"]
d12 = d11 
d12


# In[82]:


d11 = d11.groupby(["Team","Player_ID"], as_index=False).mean()
d12 = d12.groupby(["Player_ID"], as_index=False).mean()
d12.columns = ["Player_ID","season","Unique_id","match_id","Overall_Ratio"]
d11 = d11[["Team","Player_ID","Playing_Ratio"]]


# In[83]:


d11 = d11.merge(d12, how="left", on="Player_ID")
d11.to_csv("player_playing_stats.csv",index=False)


# In[ ]:


file1 = open("./final_final.csv","rb")
reader = csv.reader(file1)
file2 = open("./final_final_v1.csv","wb")
writer = csv.writer(file2)


# In[ ]:


index = {}
i = 0
header = True
team1 =0
team2 =0
inning=1
for row in reader:
    if header:
        for value in row:
            index[value]=i
            i+=1
        header = False
        writer.writerow(row)
        continue
    else:
        newrow = row[:]
        if team1==0:
            match_id = row[index["match_id"]]
            team1 = row[index["team_id"]]
            team2 = row[index["Against"]]
        if team1 != row[index["team_id"]]:
            inning = 3- inning
            team1 = row[index["team_id"]]
            team2 = row[index["Against"]]
        newrow[index["inning"]]=inning
        newrow[index["inning1"]]= 3- inning
    writer.writerow(newrow)
file1.close()
file2.close()

