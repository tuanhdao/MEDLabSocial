# The Revamped MED Lab Social Interaction Task

This repository houses the VP task, a social interaction task by Dr. Autumn Kujawa, Helen Zhang, & Anh Dao. This task builds on the https://github.com/Kodiologist/Survivor task. 


## Table of Contents
1. Downloading PsychoPy and Determining Parallel Port Address
2. Making Changes to the Task
3. Specifying the Correct Parallel Port Address in Builder 
4. Output Interpretation
5. Trigger Code List
6. Video of a Trial Run 
7. Summary of Changes from the Original Island Getaway Task

## 1.  Downloading PsychoPy and Determining Parallel Port Address

**Downloading PsychoPy:**

-   Use a Windows computer!
-   Download and install PsychoPy 2022.2.4 (choose this file StandalonePsychoPy-2022.2.4-win64.exe):  [https://github.com/psychopy/psychopy/releases?page=1](https://github.com/psychopy/psychopy/releases?page=7)

**REQUIRED: Install correct parallel port drivers:**

-   Download the inpout32.dll driver:  [http://www.highrez.co.uk/downloads/inpout32/](http://www.highrez.co.uk/downloads/inpout32/)  32 by clicking on "Binaries only - x86 & x64 DLLs and libs" under Downloads. (This file is needed to give Windows access to the parallel port installed in the display computer.)
-   Unzip the folder, and run “InstallDriver” which is found in the Win32 folder by clicking on the driver. When properly installed, you should get a confirmation message saying it’s done! Copy the inpout.dll file found in the Win32 folder to the following locations:
-   _Note: it’s possible that it is not required to place the file in all these locations. However, I did just to be safe!_

1.  C:\Program Files\PsychoPy
2.  C:\Program Files\Psychopy\DLLs
3.  The folder where your psychopy script is saved

**Get the parallel port address:**

-   Download the parallel port tester from:  [http://www.downtowndougbrown.com/2013/06/parallel-port-tester/](http://www.downtowndougbrown.com/2013/06/parallel-port-tester/)
-   Open the parallel port tester, and choose the parallel port you have installed on the display computer (bottom right corner). This should display the correct address to be used in your Psychopy code. (e.g. mine is a PCIe with address: 0x3FF8). This is the same address that shows up in device manager, if you are more familiar with that method of finding the address.
-   If you launch BrainVision Recorder on the acquisition computer, go to Amplifier > Digital Port Settings, you will have the parallel port installed on the display computer show up. By turning some pins from low to high (pins 2-9) you should see the pins change in the BrainVision recorder too. This confirms that the parallel port is indeed installed correctly and working ‘manually.’

## 2. Making Changes to the Task

 -  Watch tutorials on how to use PsychoPy if needed: https://youtube.com/playlist?list=PL6PJquR5BWXllUt585cRJWcRTly55iXTm
 
 - There are 2 ways to make changes in the task, but **I will only discuss changes made using the Builder** due to the following reasons:
	 - If you want to run the experiment using .PSYEXP files (not .PY) files YOU MUST make all changes using PsychoPy Builder. 
		 - This means a lot of clicking which can be time-consuming, but it is much easier to navigate. 
		 - You can add code snippets as needed in Builder - the only challenge of making changes using the Builder is that you need to pay attention to the order of each components, as well as where to add different code snippets (i.e., before experiment, begin routine, etc.). 
	 - However, if you are okay with running the task using a simple Python script, you can make changes to the task using the PsychoPy Coder. I would NOT recommend this as it will create a discrepancy between the .PSYEXP file and the .PY file.
	
 - A brief overview:
	- Note:
		- The .PSYEXP file is the file that contains the Builder version of the task. To run the task, you should open this file and click on "Run."
		- It is useful to also make sure to save the .PY file because these files will be able to be run using any version of PsychoPy3. Save these files to prevent losing the task due to corrupted .PSYEXP files. 
		- The second most important file is the Trials.xlsx file which contains all of the co-players' information. 
 -  If you open the file, you will see a number of columns. All of these columns can be altered, but **I would pay careful attention to altering cop_vote, which is a column that contains co-players' voting patterns, as well as co-player types.** 
 
	- **Changing co-players' pictures**:
		- *Method 1*: 
			- Crop co-player pictures to the correct size (144 x 216 px).
			- Overwrite the images that are in the "images" folder. In other words, you will retain the image names but change the image file.
		-  *Method 2*:
			- Crop co-player pictures to the correct size (144 x 216 px).
			- Change the file paths in the cop_photo column to include the correct file names. 
	
	- **Changing co-players' names, ages, hometowns, interests, schools and poll answers**: 
		- Simply change values in these columns with the new co-player profile information.
	- **Changing co-players' votes**:
		- The cop_vote column will have a list consisting of 0s (Dislike) and 1s (Like)  and the type of the co-player. 
			- The type of the co-player simple denotes the number times a co-player will "like" the participant. There are 4 types with 3 co-players assigned to each. 
				- Type 1: 3 peers - 4 reject votes, 1 accept across task.
				- Type 2: 3 peers - 3 reject votes, 2 accept across task.
				- Type 3: 3 peers - 2 reject votes, 3 accept across task.
				- Type 4: 3 peers - 1 reject votes, 4 accept across task.
		- Co-player votes are set up so that the participant gets 6 likes and 6 dislikes in each round. It is important to keep this ratio to be congruent with the Doors task and also to make the result of the game more ambiguous. 
		- You can make edits to the order of the 0s and 1s, but I would always make sure to double-check the ratio of likes/dislikes after making any edits. 
## 3. Specifying the Correct Parallel Port Address in Builder
 - Open PsychoPy Builder and then open the .PSYEXP version of the task which trigger codes enabled (File > Open > your file directory).  
 - In Hardware settings (File > Preferences > Hardware), add the correct parallel port address of your task computer (PsychoPy will likely have a list of existing addresses; you can just add a comma and the correct parallel port address of your task computer). 
 - If the address of your computer is already loaded in the parallel ports cell, you do not have to make any changes, so just click "OK" to close preferences. 
![image](https://user-images.githubusercontent.com/54826556/195232867-7f9c4dba-c546-4b79-ae96-1109bd72d97c.png)
 - Triggers will be sent in these instances:
	 - When participant votes in all 5 rounds.
		 - **For each round of real voting** (see loops that are called voting_1, voting_2, etc.): 
			 - Choose the Players_profiles_voting_style routine.
			 - Within this routine, click on the component named ptp_trigger (will have a suffix denoting round number) > Hardware > Choose the correct parallel port address in the drop-down menu.
	 - When participant receives a vote in all 5 rounds.
		 - **For each round of real voting,** (see loops that are called voting_1, voting_2, etc.):
			 - Choose the Cop_vote routine.
			 - Find the component (a code chunk) named thumb_trigger.
			 - In the Begin Routine tab, change the parallel port address to be the correct address for your task computer:
				 `coplayer_trigger_second = parallel.ParallelPort(address='0xE010')`
	 - The end of the task when the participant learns of the result of the game. 
		 - Find the Result routine.
		 - Within this routine, click on the component named result_trigger (will have a suffix denoting round number) > Hardware > Choose the correct parallel port address in the drop-down menu.
 - Once you complete all of these edits, run the task in its entirety to test it. 
 

## 4. Output Interpretation

 - The task will write data into an excel (.csv) file, a PSYDAT file and also a log file.
 - Only the .csv file is needed for data analysis purposes. The program removes participants' names but retains all other information (votes, poll responses, post-task questionnaires). 
 ## 5. Trigger Code List
 - 1: Participant likes a Co-player
 - 2: Participant dislikes a Co-player
 - 15: Type 1 Co-player likes participant
 - 16: Type 1 Co-player dislikes participant
 - 25: Type 2 Co-player likes participant
 - 26: Type 2 Co-player dislikes participant
 - 35: Type 3 Co-player likes participant
 - 36: Type 3 Co-player dislikes participant
 - 45: Type 4 Co-player likes participant
 - 46: Type 4 Co-player dislikes participant
 - 50: Participant is invited to party
 
 ## 6. Video of a Trial Run
 - See an example run of the whole task here: https://tinyurl.com/medlabvirtualparty
 
 ## 7. Summary of Changes from the Original Island Getaway Task
 - More accurate trigger timing (trigger timings tested using BrainVision photosensor). 
 - Removed binary gender. 
 - Updated storyline: The task simulates a social media platform with clear "likes" and "dislikes" to assess reactions to social acceptance/rejection.
 - Updated stimuli: Using blue and red thumb icons instead of red and green, and updated icons for practice co-player profiles. 
 - Text entry fields are built into the task window which resolves issues with previous pop-up text boxes.
 - Added more time for co-players to respond/vote to increase believability. 
 - Added a screen to inform participant that votes are being compiled and their feedback will be shown shortly. 
 - Co-players and rounds: 
 	- All co-player profile information is randomly assigned at each run of the task. 
 	- The new version of the task includes 12 co-players who are each assigned to a "type" rather than "mean" or "nice." There are 4 types of co-players with 3 co-players in each category (see above).
	- There are 5 rounds of voting.
	- All co-players remain in the game, so there are 60 voting trials. Instead of being kicked out, the co-players are either among the ones who got the most votes or the least votes. Co-player profiles are randomly assigned and then assigned a specific order. Most/least liked co-player's are chosen using a fixed order (i.e., the co-player who appears second in the initial profile viewing will be most liked in round 1, etc.) so that no most liked co-players end up least liked in other rounds and vice-versa. 
- Added PANAS questions to the post-task questionnaire and items about believability. 
- Output file includes a .CSV file that can easily be used to analyze behavioral data. 
	
## 8. Troubleshooting 
- Installing 2023.x.x versions of PsychoPy currently throws a fatal error of missing environmenttools. Only use 2022.x.x. versions to avoid this problem. 
			
