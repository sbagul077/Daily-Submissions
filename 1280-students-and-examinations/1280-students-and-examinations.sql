# Write your MySQL query statement below
select st.student_id, st.student_name, subs.subject_name, count(ex.subject_name) as attended_exams
from Students st
cross join Subjects subs
left join Examinations ex
on st.student_id = ex.student_id and ex.subject_name = subs.subject_name
group by st.student_id, st.student_name, subs.subject_name
order by st.student_id, subs.subject_name


-- SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.subject_name) AS attended_exams
-- FROM Students
-- CROSS JOIN Subjects
-- LEFT JOIN Examinations
-- ON Students.student_id = Examinations.student_id AND Subjects.subject_name = Examinations.subject_name
-- GROUP BY student_id, student_name, subject_name
-- ORDER BY student_id,subject_name


# Write your MySQL query statement below

# select t1.student_id , t1.student_name , t3.subject_name , count(t2.subject_name) as 'attended_exams'
# from Students as t1 
# left join Examinations as t2
# cross join Subjects as t3
# on t1.student_id = t2.student_id and t2.subject_name = t3.subject_name
# group by t1.student_id, t1.student_name, t2.subject_name
# # having attended_exams <> 0
# order by t1.student_id, t3.subject_name;

-- SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.subject_name) AS attended_exams
-- FROM Students
-- CROSS JOIN Subjects
-- LEFT JOIN Examinations
-- ON Students.student_id = Examinations.student_id AND Subjects.subject_name = Examinations.subject_name
-- GROUP BY student_id, student_name, subject_name
-- ORDER BY student_id,subject_name


# SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.subject_name) AS attended_exams
# FROM Students
# CROSS JOIN Subjects
# LEFT JOIN Examinations
# ON Students.student_id = Examinations.student_id AND Subjects.subject_name = Examinations.subject_name
# GROUP BY student_id, student_name, subject_name
# ORDER BY student_id, student_name
# # {"headers": ["student_id", "student_name", "subject_name", "attended_exams"], "values": [[2, "Bob", "Physics", 0], [6, "Alex", "Programming", 0], [1, "Alice", "Math", 3], [1, "Alice", "Physics", 2], [1, "Alice", "Programming", 1], [2, "Bob", "Math", 1], [2, "Bob", "Programming", 1], [13, "John", "Math", 1], [13, "John", "Physics", 1], [13, "John", "Programming", 1]]}

# # {"headers": ["student_id", "student_name", "subject_name", "attended_exams"], "values": [[1, "Alice", "Math", 3], [1, "Alice", "Physics", 2], [1, "Alice", "Programming", 1], [2, "Bob", "Math", 1], [2, "Bob", "Physics", 0], [2, "Bob", "Programming", 1], [6, "Alex", "Math", 0], [6, "Alex", "Physics", 0], [6, "Alex", "Programming", 0], [13, "John", "Math", 1], [13, "John", "Physics", 1], [13, "John", "Programming", 1]]}