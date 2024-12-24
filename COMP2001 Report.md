# COMP2001 Report

## Introduction


This report outlines the design, implementation, and assessment of the TrailService micro-service, which is an essential element of a well-being trail application.
 The primary objective of this application is to motivate users to explore outdoor trails, thereby improving their well-being through a systematic approach to discovering new locations. 
 The TrailService microservice facilitates the management of trail data, allowing users to create, read, update, and delete trails, while ensuring compliance with privacy, security, and RESTful API standards. 
The report commences with an overview of the TrailService as part of the larger Trail Application, subsequently detailing the service’s technical architecture through the use of ERD and UML models. 
It addresses significant LESP factors to illustrate the commitment to data security and integrity. 
The implementation section delineates the APU endpoints, the structure of the code, and the integration with the Plymouth Authenticator API, emphasizing CRUD operation and user authentication processes. In conclusion, the report assesses the service’s performance through testing, consider possible enhancements, and identifies opportunities for future development. 


[**_Web Server_**]()

[**_GitHub Repo_**](https://github.com/Ali34f/COMP2001--Trail-Service-)



## Background

The TrailService micro-service is an integral component of a well- being trail application aimed at promoting outdoor exploration for both mental and physical health advantages. 
This application primarily serves to provide users with a systematic approach to discovering  and navigating trails across diverse locations, thereby strengthening their bond with nature and fostering overall well- being. 
It designed in accordance with the user narrative that facilitates individuals in exploring outdoor environments via a user-friendly, data-oriented platform.
The TrailService micro-service is dedicated to the management of trail data storage and retrieval. 
In this context, trails are defined as a sequence of location points that direct user along designated routes. Each trail is associated with a registered user, and modifications can only be made by authorized users who own the trails. 
All users, however, have the ability to view trails, albeit with restricted information. This functionality is facilitated through CRUD (Create, Read, Update, Delete) operations on the trail data, thereby ensuring both accessibility and security. 
In order to manage user authentication and ensure data privacy, the TrailService utilizes the Plymouth Authenticator API, this integration confirms that only authorized users can access or modify sensitive information. 
Additionally, the TrailService complies with RESTful API principles, which promote efficient communication and interaction with the application. The service also adopts security best practices to safeguard user date, focusing on critical issues related to information privacy, integrity, and preservation. 


## Design

## LSEP

## Implementation

## Evaluation

# BELOW ARE THE THINGS I NEED TO WRITE

### Introduction

Provides an introduction to the document and signposts the reader to what they will find in the document.
GitHub link provided. GitHub repo in the correct place (GitHub classroom provided for module).
Link provide to web.socem deployment of micro-service.

### Background

Outline provided for the micro-service. 4
Design Appropriate UML diagrams used.
Clear demonstration of understanding how to design micro-service in place.
Design clearly shows progression of understanding through high level overview through to detail.

### LSEP

Literature used to justify appropriate for information security, privacy, integrity and preservation.
Literature provided using Harvard style referencing.
Appropriate approaches used to meet requirements for a secure, private application.
Data items designed in a way that enforces integrity, privacy and security.

### Implementation

Implementation discussed at appropriate level in report.
Implementation matches code in GitHub classroom and provided design diagrams.
Implementation meets requirements alluded to above (CRUD)
Implementation is RESTful API
Endpoints appropriately represented in documentation, design and implementation.

### Evaluation

Clear evidence of testing provided.
Reflection provided on further work.
Honest reflection provided on weak areas of implementation.

OWASP top 10?
