# Project README

Speed_Detection_122024
Overview

This project is designed to analyze video footage and detect car speed based on both the road speed and the vehicle’s speed. The main functionality includes processing a video frame by frame, extracting relevant data such as speed from sensor logs (CAN, GPS, IMU), and sending notifications when the car is overspeeding.

Folder Structure
Data
This folder will contain the input images and videos.

Dataset Credits
This project utilizes the comma2k19 dataset for video data. The dataset is maintained and provided by comma.ai, and it is used to train and test various computer vision models for autonomous driving applications.

Dataset: comma2k19
License: The dataset is open for non-commercial use and is licensed under MIT License.
Source: https://github.com/commaai/comma2k19
	
Docs
The folder has all referenced thesis, articls and links to all other open source projects that was referred.

Src
This will have the source code and all other utility codes for the project.

Test
The folder will be divided into several iterations.Each iteration will have a test folder where the output images or videos will be saved.

Iteration 1: Basic Video Processing
Objective: Extract frames from the video at a fixed interval (e.g., every 5 seconds) and save them as images.
Output: Saved frames in the test/ folder within the iteration folder.
Structure: The images will be saved as .jpg files to reduce file size.