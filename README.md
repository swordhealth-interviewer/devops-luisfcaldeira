# SWORDHEALTH

- [ ] Primeiro problema

About once every two weeks, SWORD asks its patients how much they would
recommend its therapy to someone they know on a scale from 0 to 10. Assume you have a
table called Scores having a json string containing (among other things) the satisfaction
scores of SWORD’s patients along with the corresponding date, as follows:
| id  | patient_id  |  scores                                       |  date       |
|:---:| :----:      |     :---------:                               | :-----:     |
| 1   | 1323        | {‘satisfaction’: 9, ‘pain’: 2, ‘fatigue’: 2}  |  2020-06-25 |
| 2   | 9032        | {‘satisfaction’: 2, ‘pain’: 7, ‘fatigue’: 5}  |  2020-06-30 |
| 3   | 2331        | {‘satisfaction’: 7, ‘pain’: 1, ‘fatigue’: 1}  |  2020-07-05 |
| 4   | 2303        | {‘satisfaction’: 8, ‘pain’: 9, ‘fatigue’: 0}  |  2020-07-12 |
| 5   | 1323        | {‘satisfaction’: 10, ‘pain’: 0, ‘fatigue’: 0} |  2020-07-09 |
| 6   | 2331        | {‘satisfaction’: 8, ‘pain’: 9, ‘fatigue’: 5}  |  2020-07-20 |

One of our most important metrics is the NPS (Net Promoter Score) which is calculated with the following formula:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;{\color{Gray}NPS=\frac{numberOfPromoters-numberOfDetractors}{numberOfPatients}" />


Patients are classified in the following groups according to their most recent satisfaction
report:
* \> 8 is a promoter
* < 7 is a detractor

Write a SQL query to calculate SWORD’s Digital Therapist NPS for each month. E.g.:

| month   | NPS|
| ---     | ---|
| January | 50 |
| February| 45 |
| March   | 53 |
| ...     | ...|





# - [ ] Segundo problema

Write a python program that takes as input the name of a txt file and creates another file
having the number of occurrences of each word in the original file in descending order. E.g.:

the 563

of 431

to 320

it 210

that 109

...


Your program should distribute the computation by having 10 worker threads simultaneously
building the resulting list.
