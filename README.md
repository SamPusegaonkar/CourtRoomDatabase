# CourtRoomDatabase


**Description**: This repo consits of a courtroom database management system.  <br/>
  
  **Required Libraries**:     
  
    * Tkinter-pip install tkinter 
    * PyMySQL-pip install pymysql 
    * Install XAMPP
                     
  **Instructions**: 
  
    1. Start MYSQL using XAMPP. 
    2. Create the following tables: judge, victim, suspect and verdict.
    3. Run GUI.py
    4. Done Diddly do. EZ. 
 
 
**Victim Table:**

| Field         | Type        | Null | Key | Default | Extra |
| ------------- |-----------  |----- | --- |-------- |-------|
| f_name        | varchar(40) | YES  |     | NULL    |       |
| l_name        | varchar(40) | YES  |     | NULL    |       |
| phone_nummber | varchar(40) | YES  |     | NULL    |       |
| case_number   | int(10)     | YES  |     | NULL    |       |
| address       | varchar(40) | YES  |     | NULL    |       |

**Judge Table:**

| Field         | Type        | Null | Key | Default | Extra |
|---------------|-------------|------|-----|---------|-------|
| f_name        | varchar(40) | YES  |     | NULL    |       |
| l_name        | varchar(40) | YES  |     | NULL    |       |
| street        | varchar(40) | YES  |     | NULL    |       |
| area          | varchar(40) | YES  |     | NULL    |       |
| qualification | varchar(40) | YES  |     | NULL    |       |
| dob           | varchar(40) | YES  |     | NULL    |       |
| age           | varchar(40) | YES  |     | NULL    |       |
| salary        | varchar(40) | YES  |     | NULL    |       |
| case_number   | varchar(40) | YES  |     | NULL    |       |
| id            | varchar(40) | NO   | PRI | NULL    |       |

**Suspect Table:**

| Field         | Type        | Null | Key | Default | Extra |
| --------------|-------------|------|-----|---------|-------|
| f_name        | varchar(40) | YES  |     | NULL    |       |
| l_name        | varchar(40) | YES  |     | NULL    |       |
| phone_nummber | varchar(40) | YES  |     | NULL    |       |
| case_number   | int(10)     | YES  |     | NULL    |       |
| address       | varchar(40) | YES  |     | NULL    |       |

**Verdict Table:**

| Field       | Type        | Null | Key | Default | Extra |
| ----------- | ----------- |----- |---- |-------- | ----- |
| judgement   | varchar(40) | YES  |     | NULL    |       |
| case_number | varchar(40) | YES  |     | NULL    |       |
| IPC         | varchar(40) | YES  |     | NULL    |       |



![capture](https://user-images.githubusercontent.com/12711480/52521708-111d4b00-2ca1-11e9-9a97-5b824f1e0f93.PNG)

![cap4](https://user-images.githubusercontent.com/12711480/52521727-65c0c600-2ca1-11e9-8fe1-2b37ecec17c1.PNG)

![cap3](https://user-images.githubusercontent.com/12711480/52521729-7a04c300-2ca1-11e9-95b3-1569aef734bb.PNG)


PS: Dumb school project


tweet @sampusegaonkar
