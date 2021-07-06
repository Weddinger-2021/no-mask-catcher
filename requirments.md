# Requirements:  

____
____
____

# User story :

1. As a company management I'd like to have a video system that recognizes if a person is not wearing a mask

2. As a company management I'd like to take a screenshot of any person that is not wearing a mask from the video.

3. As a company management I'd like to alert immediately with a 10 seconds warning audio if any person is not wearing a mask(Was stretch)

4. As a compnay management I'd like to check if this person is in my dataset

5. If the person is in the dataset , I'd like to be notified with an email to the company's authority with these info:
	Data, Time , Screenshot , Name , Job title , Department , Job ID.

6. If the person is not in the dataset, I'd like to be notified with an email to the company's authority with only these info:
    Data , Time , Screenshot.

7. **Stretch Goal** As a company management I'd like to cut off a certain amount from the salary(e.g: 20$)

8. **Stretch Goal** As a company management I'd like to inform that person with sms message with the amount of cut on his/her salary based on gender starting with(Mrs,Ms)




# Features: 

1. Scan a video to detect if the person is wearing a mask or not 

2. Take a screenshot if there's no mask!

3. If there's no mask , Alert the person with 10 seconds audio warning.("Please wear your mask").

4. If the person is in the dataset and is not wearing a mask retrieve his/her info.

5. Send an email notification with the retrieved info (Department , Job title, Job ID) + Date, Time, , Screenshot

6. If the person in not in the dataset , send an email notification with only Date , Time , Screenshot.


___


## Email format:

**For non-employee:**
*Dear esteemed security department, Our system detected a person who is not wearing a mask in `Date` at `time` , please check attached photo below.(`Screenshot`)*


**For employee:** 
*Dear esteemed security department, Our system detected the following person (Name: `name` , from Demaprtment:  `department` , job title: `jobtitle` with ID: `id`  is not wearing a mask in Date at time , please check attached photo below.(`Screenshot`)*
 

____



# Acceptance user tests: 
**Cases:**

* Check if there is anyone is waring a mask and expect nothing to happen.

* Check if there is anyone who is not wearing a mask and expect a 10 sec alert. 

* Check if the person is in our data-set and retrieve his/her information.

* Check if the person is not in our data-set and expect a message of 'this person is not recognized'.

* Check if the person didn't wear the mask expect an E-mail sent to authorities with the a valid information.


## Domain Model:
![domain model](https://github.com/organs-2021/no-mask-catcher/blob/main/D_Model_second.png)


## Work flow: 
![work flow](https://github.com/organs-2021/no-mask-catcher/blob/main/D_Model_first.png)


## Data-set Diagram: 
![data-set diagram](https://github.com/organs-2021/no-mask-catcher/blob/main/D_Model_third.png)


## Employees DataSet:

1. Name  
2. Gender
3. Phone number
4. Job_title
5. Job_Id
6. Salary
7. Department
8. Photo

## model DataSet:

1. with mask
2. without mask


## Project Managment Tool:

[Trello Board](https://trello.com/b/Ou9hyUbw/pypandas)





