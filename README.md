# Optimizing COVID-19 Triage System (Submission to Sheffield HackMed2020 Hackathon)

## Problem Statement

The COVID-19 pandemic put an unprecedented amount of pressure on the National Health Services. The current triage system for COVID-19 relies heavily on phone calls (patients with COVID-19 symptoms can call the triage system to decide whether they need to seek urgent medical attentions). Patients often face delays due to high call volumes. Another aspect of the triage system that is overwhelmed is the interpretation of chest X-rays (CXRs). As there are increased number of CXR being done and may not be interpreted in time, leading to delay in the patient being traiged. 

## Our Solution

We developed a web platform mirroring the phone triage process, enabling public access online. Additionally, we trained a Convolutional Neural Network (CNN) to classify CXRs for pneumonia, accelerating triage for affected patients.

## Technologies

Keras: CXR Image Classification CNN for pneumonia detection.
Django: for web-based triage system and landing page to upload CXR.

## Learning Points

Problem Identification: Guided the team in understanding healthcare bottlenecks.
Technical Skill Development: Learned Django to create an efficient web-based triage solution during the hackathon.
