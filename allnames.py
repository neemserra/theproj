import sqlite3
connection = sqlite3.connect("experiments.db")
cursor = connection.cursor()
cursor.execute("SELECT Project.ProjectName, sum(Experiment.NumInvolved) from Project join Experiment where Project.ProjectID = Experiment.ProjectID group by Project.ProjectID;")
results = cursor.fetchall();
for r in results:
    print r[0], r[1]
cursor.close();
connection.close();