-- Get project name
select distinct Project.ProjectName, Person.LastName, Person.FirstName
from Project join Involved join Person
where(Project.ProjectID = Involved.ProjectID) and (Involved.Login = Person.Login);


