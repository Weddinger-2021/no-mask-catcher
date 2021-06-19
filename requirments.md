
# Team name : Py-pandas
# Project name : No-Mask-Catcher

# Vision: 

**What is the vision of this product?**

> *We aim that our product will increase people's awareness to follow safety rules and wearing their masks.*


**What pain point does this project solve?**

> *Because wearing a mask has become a necessity  to limit the spread of COVID-19, we will develop a python program to identify who is wearing a mask and who is not wearing a mask and alert the superviser about it.*


**Why should we care about your product?**

> *Our product is a full deticting system that will alert the poerson who is not wearing the mask and retrieve his/her information if they were found in the data-set to notify the authorities by sening an e-mail with his/her information.*

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


## Email format:

**For non-employee:**
*Dear esteemed security department, Our system detected a person who is not wearing a mask in `Date` at `time` , please check attached photo below.(`Screenshot`)*


**For employee:** 
*Dear esteemed security department, Our system detected the following person (Name: `name` , from Demaprtment:  `department` , job title: `jobtitle` with ID: `id`  is not wearing a mask in Date at time , please check attached photo below.(`Screenshot`)*
 


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







# Installation 

## Linux ubuntu deb: 

1. `pip install CMake` OR `brew install CMake` *for local installation*

2. `Clone Repository` 

3. `poetry install`

## Windows:

> **You should use `pip install poetry` to contuniue with poetry.**

1. **download python 3.8 from** [python organaization](https://www.python.org./downloads/) *(3.8.5 is recommended)* 

2. [CMake](https://cmake.org/download/) *install Cmake required for your OS, extract the folder anywhere on your machine*

3. *Set the path for the bin sub-folder inside the extracted folder in your system environmental variables.* 

4. `pip install cmake` 

5. **clone this repo** [dlib GitHub Repo](https://github.com/RvTechiNNovate/face_recog_dlib_file)

6. **Inside above directory run:** `pip install dlib-19.19.0-cp38-cp38-win_amd64.whl`

7. **clone our Repo.**

8. `pip install`, *for all libraries in pyproject.toml.*

9. `peotry install`







## MacOS:

1. `brew install cmake`

2. `pip install poetry`

2. `Clone Repository` 

3. `poetry install`

