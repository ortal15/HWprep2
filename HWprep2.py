import sqlite3
from HWprep2_def import create_table

create_table()
conn = sqlite3.connect('prep2.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

'''a. הצג את רשימת הקורסים והמרצה המלמד בקורס, בהם יש מרצה המשובץ לקורס'''

cursor.execute('''SELECT course_name , first_name , last_name
FROM courses c 
JOIN lecturers l on l.lecturer_id = c.lecturer_id
WHERE l.lecturer_id = c.lecturer_id
''')

'''b. הצג את רשימת הקורסים בהם אין מרצה המשובץ ל קורס. רמז: NULL IS'''

cursor.execute('''SELECT course_name
FROM courses c
LEFT JOIN lecturers l on l.lecturer_id = c.lecturer_id
WHERE c.lecturer_id is NULL
''')

'''c. הצג את רשימת כל הקורסים והמרצה המשובץ )היכן שאין מרצה משובץ, יופיע NULL
בפרטי המרצה('''

cursor.execute('''SELECT * FROM courses c
LEFT JOIN lecturers l on l.lecturer_id = c.lecturer_id
ORDER by c.lecturer_id is NULL
''')

'''d. הצג את רשימת המרצים והקורס שאותם הם מלמדים, רק עבור מרצים המשובצים'''

cursor.execute('''SELECT first_name , last_name , course_name
FROM lecturers l
LEFT JOIN courses c on l.lecturer_id = c.lecturer_id
WHERE l.lecturer_id = c.lecturer_id
''')

'''e. הצג את רשימת המרצים שאינם משובצים לשום קורס. רמז: NULL IS'''

cursor.execute('''SELECT first_name , last_name
FROM lecturers l
LEFT JOIN courses c  on l.lecturer_id = c.lecturer_id
WHERE c.lecturer_id is NULL''')

'''f. הצג את רשימת כל המרצים והקורס שאותם הם מלמדים )היכן שהמרצה איננו משובץ
לאף קורס, יופיע NULL בפרטי הקורס('''

cursor.execute('''SELECT * FROM lecturers l
LEFT JOIN courses c on l.lecturer_id = c.lecturer_id
ORDER by l.lecturer_id is NULL''')

'''g. הצג את רשימת כל הקורסים והמרצה המשובץ )היכן שלא משובץ מרצה, יופיע NULL
בפרטי המרצה( ביחד עם כל המרצים והקורס שאותם הם מלמדים )היכן שהמרצה איננו
משובץ לקורס, יופיע NULL בפרטי הקורס( . רמז: JOIN FULL'''

cursor.execute('''SELECT * FROM courses c
FULL JOIN lecturers l on l.lecturer_id = c.lecturer_id
ORDER by c.lecturer_id is NULL''')

'''h. הצג רשימה בה כל מרצה מלמד את כל אחד מהקורסים . רמז: JOIN CROSS'''

cursor.execute('''SELECT first_name , course_name
FROM lecturers l 
CROSS JOIN courses c;
''')
