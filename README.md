# Introducing Arike

**"Arike"** is a Malayalam word that roughly translates to "Alongside" or "Besides" in English. The project caters to a system of specialized medical staff tending to patients under palliative care.

Unlike most of us who need medical care rarely and visit hospitals when required, there are thousands of people who need constant or specialized medical care. Keeping these folks in the hospital is not a viable idea since it bogs down our hospital capacity and also makes their life more difficult. These patients fall under palliative care.

In India, palliative care is provided by a specially trained team of nurses who visit the patients under their Panchayat/Municipality/Corporation directly to relieve their suffering and give them and their families the best possible quality of life. At present, many states have their own palliative care systems in place.

The treatment under palliative care is an extremely complex process, and it's mostly paperbound, which makes it inefficient and error bound. Our capstone project is to build a system that makes the process more efficient and automated. There are a lot more nuances to this project, which we will get to step by step.

## Basics of Arike

Generally, in palliative care, there are “Primary Health Centers” (PHC) and “Community Health Centers”(CHC). Each of these resides in a ward that belongs to one of the many LSGs (Local Self-Government) in a district. In every PHC, there are primary nurses whose job is to visit patients locality-wise every month, go through their case sheets, and provide them with the care they need. If a particular patient needs expert care, they are referred to a specialist nurse who comes from the CHC. Now, there are a lot of disadvantages in the current system, and you would be surprised to see how much paperwork is involved in such critical matters of life!

The main users for Arike are:

- **Primary Nurse:** This user persona is responsible for maintaining all the health records for a particular patient under their PHC.

- **Secondary Nurse:** This user persona belongs only to a CHC and is the specialist nurse that provides special care for a patient when referred by a primary nurse.

- **District Admin:** This user persona has access to records under the user’s district. This user will be given full access to the data and should be able to create and delete Primary or Secondary nurses.

## Main Enitities
- **Facility:** It can be a PHC or CHC.
- **Patient:** In our system, a patient is an object whose data we are dealing with, and they never get to use the software. A patient is registered in a PHC and is only referred to a CHC.

<!--### Expected Wireframe:
https://www.figma.com/file/kgOXmtptNxJUvkJ2qjeyzA/Django-201-Capstone?node-id=3%3A1146-->

## Login Details:
A user with the following usernames can login in the system:

```
Username: distadmin 
Password: distadmin
UserType: District Admin

Username: primarynurse
Password: primarynurse
UserType: Primary Nurse

Username: secondarynurse
Password: secondarynurse
UserType: Secondary Nurse
```
