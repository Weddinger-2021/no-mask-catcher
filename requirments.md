
# Team name : Py-pandas
# Project name : Face mask detector system (FMDS)


# Vision: 

**What is the vision of this product?**

> *We aim that our product will increase people's awareness to follow safety rules and wearing their masks.*


**What pain point does this project solve?**

> *Because wearing a mask has become a necessity  to limit the spread of COVID-19, we will develop a python program to identify who is wearing a mask and who is not wearing a mask and alert the superviser about it.*


**Why should we care about your product?**

> *Our product is a full deticting system that will alert the poerson who is not wearing the mask and retrieve his/her information if they were found in the data-set to notify the authorities by sening an e-mail with his/her information.*


# Feature tasks(MVP): 

1. Scan a video to detect if the person is wearing a mask or not 

2. Take a screenshot if there's no mask!

3. If there's no mask , Alert the person with 10 seconds audio warning.("Please wear your mask").

4. If the person is in the dataset and is not wearing a mask retrieve his/her info.

5. Send an email notification with the retrieved info (Department , Job title, Job ID) + Date, Time, , Screenshot

6. If the person in not in the dataset , send an email notification with only Date , Time , Screenshot.


## Email format:

**For non-employee:**
*Dear esteemed security department, Our system detected a person who is not wearing a mask in `Date` at `time` , please check attached photo below.(`Screenshot`)*


**For employee:** 
*Dear esteemed security department, Our system detected the following person (Name: `name` , from Demaprtment:  `department` , job title: `jobtitle` with ID: `id`  is not wearing a mask in Date at time , please check attached photo below.(`Screenshot`)*
 

# User story : 
1. As a company management I'd like to have a video system that recognizes if a person is not wearing a mask

2. As a company management I'd like to take a screenshot of any person that is not wearing a mask from the video.

3. As a company management I'd like to alert immediately with a 10 seconds warning audio if any person is not wearing a mask(Was stretch)

4. As a compnay management I'd like to check if this person is in my dataset

5. If the person is in the dataset , I'd like to be notified with an email to the company's authority with these info:
	Data, Time , Screenshot , Name , Job title , Department , Job ID.

6. If the person is not in the dataset, I'd like to be notified with an email to the company's authority with only these info:
    Data , Time , Screenshot.

7. as a company management I'd like to cut off a certain amount from the salary(e.g: 20$) --> Stretch Goal

8. as a company management I'd like to inform that person with sms message with the amount of cut on his/her salary based on gender starting with(Mrs,Ms) -> Stretch Goal



# Software Requirements:

1. any OS(linux, Windows , Mac)

2. Python libraries needed(openCV, keras , tensorflow, tailwot ..etc) 

3. an access to a camera device.

4. an acess to an audio device.

5. any python IDE (Visual Studio)

6. Email API

## non-functional requirments:

* Data integrity.
* Portability.
* reliablity. 
* Security 
* Testability
* Accessibility
* Adaptability
* licensing




# Acceptance user tests: 
**Cases:**

* Check if there is anyone is waring a mask and expect nothing to happen.

* Check if there is anyone who is not wearing a mask and expect a 10 sec alert. 

* Check if the person is in our data-set and retrieve his/her information.

* Check if the person is not in our data-set and expect a message of 'this person is not recognized'.

* Check if the person didn't wear the mask expect an E-mail sent to authorities with the a valid information.


## DataSet:

1. Name  
2. Gender
3. Phone number
4. job title
5. Job Id
6. Salary
7. Department
8. photos --> 10 photos for each 

