
--List all Female Members
SELECT * FROM members WHERE gender LIKE '%Female%';


--Show all Classess scheduled on Friday
SELECT * FROM classes where class_day LIKE '%Friday%';

--Find members whoe joined in April 2024
SELECT *
FROM members
WHERE join_date >= "2024-04-01" and join_date <= "2024-04-30";


-- Get the full Name of each members and the name of the class they enrooled in
SELECT members.first_name,members.last_name,classes.class_name
from members
join class_enrollments on class_enrollments.member_id = members.id
join classes on classes.id = class_enrollments.class_id;

-- list all trainers and the classess they teach
SELECT trainers.first_name,trainers.last_name,classes.class_name
from trainers
join classes on classes.trainer_id = trainers.id;

-- show each member's membership plan and price
SELECT 
	members.first_name,
	members.last_name,
	membership_plans.plan_name
from members
JOIN membership_plans on membership_plans.id = members.membership_id;

--- coint how many members aree enrolled in each class
SELECT count(*) as number_of_member,
	classes.class_name
FROM classes
JOIN class_enrollments on class_enrollments.class_id = classes.id
GROUP BY classes.class_name;


-- calculate the total payment recieved per membership plan
SELECT membership_plans.plan_name,SUM(payments.amount) as total
from members
JOIN payments ON payments.member_id = members.id
JOIN membership_plans on membership_plans.id = members.membership_id
GROUP BY membership_plans.plan_name;

SELECT 
	m.first_name,
	m.last_name,
	COUNT(*) as total_appearances
FROM members m
JOIN attendance a ON a.member_id = m.id
GROUP BY m.id, m.first_name, m.last_name
HAVING count(*) > 1;


--List Members who Enrolled in classes Taught by Carlos Diaz
SELECT 
    members.first_name,
    members.last_name,
	classes.class_name,
	trainers.first_name,
	trainers.last_name
FROM members
JOIN class_enrollments ON class_enrollments.member_id = members.id
JOIN classes on class_enrollments.class_id = classes.id
JOIN trainers on classes.trainer_id = trainers.id
Where trainers.first_name like "%Carlos";


--Show members who paid Excatly the price of thier membership plan
SELECT members.first_name,last_name,payments.amount,membership_plans.plan_name,membership_plans.price
FROM members
JOIN payments on payments.member_id = members.id
JOIN membership_plans on membership_plans.id = members.membership_id;
