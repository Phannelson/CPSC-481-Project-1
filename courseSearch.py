courses = {
    #lower division core (18 units)
    "CPSC 120" : { "units" : 3, "prereq" : [] },                                            #intro to programming
    "CPSC 121" : { "units" : 3, "prereq" : ["CPSC 120"] },                                  #Object oriented programming
    "CPSC 131" : { "units" : 3, "prereq" : ["CPSC 121"] },                                  #Data Structure
    "CPSC 223" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #C/Java/C#/Python/Swift programming
    "CPSC 240" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 170A"] },                     #Computer organization and Assembly
    "CPSC 253" : { "units" : 3, "prereq" : [] },                                            #Cybersecurity foundations and principles
    #upper division core (30 units)
    "CPSC 315" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Professional Ethics in Computing
    "CPSC 323" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Compilers and Languages
    "CPSC 332" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #File Structures & Dataabases
    "CPSC 335" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 170A", "MATH 150A"] },        #Algorithm Engineering
    "CPSC 351" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Operating System Concepts
    "CPSC 362" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Foundations of Software Engineering
    "CPSC 471" : { "units" : 3, "prereq" : ["CPSC 351"] },                                  #Computer Communications
    "CPSC 481" : { "units" : 3, "prereq" : ["CPSC 335", "MATH 338"] },                      #Artificial Intelligence
    "CPSC 490" : { "units" : 3, "prereq" : ["CPSC 362"] },                                  #Undergraduate Seminar in CS
    "CPSC 491" : { "units" : 3, "prereq" : ["CPSC 490"] },                                  #Senior Capstone Project in CS
    #Math Requirements (18 units)
    "MATH 150A" : { "units" : 4, "prereq" : [] },                                           #Calculus 1
    "MATH 150B" : { "units" : 4, "prereq" : ["MATH 150A"] },                                #Calculus 2
    "MATH 170A" : { "units" : 3, "prereq" : [] },                                           #Math Structures 1
    "MATH 170B" : { "units" : 3, "prereq" : ["MATH 170A"] },                                #Math Structures 2
    "MATH 338" : { "units" : 4, "prereq" : ["MATH 150B"] },                                 #Statistics Applied to Natural Sciences
    #CS Electives (15 units)
    "CPSC 254" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Software Development With Open Source Systems
    "CPSC 349" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Web Front-end Engineering
    "CPSC 352/452" : { "units" : 3, "prereq" : ["MATH 170B, CPSC 131", "CPSC 253"] },       #Cryptography
    "CPSC 375" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 338"] },                      #Intro to Data Science and Big Data
    "CPSC 386" : { "units" : 3, "prereq" : ["CPSC 121"] },                                  #Intro to Game Design and Production
    "CPSC 411" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Mobile Device Application Programming (IOS)
    "CPSC 411A" : { "units" : 3, "prereq" : ["CPSC 131"] },                                 #Moblie Device App Programming for Android
    "CPSC 431" : { "units" : 3, "prereq" : ["CPSC 332"] },                                  #Database and Applications
    "CPSC 439" : { "units" : 3, "prereq" : ["CPSC 121", "MATH 170B"] },                     #theory of computation
    "CPSC 440" : { "units" : 3, "prereq" : ["CPSC 240"] },                                  #computer system architecture
    "CPSC 449" : { "units" : 3, "prereq" : ["CPSC 332"] },                                  #Web Back-end Engineering
    "CPSC 454" : { "units" : 3, "prereq" : ["CPSC 351", "CPSC 253"] },                      #Cloud Computing and Security
    "CPSC 455" : { "units" : 3, "prereq" : ["CPSC 351", "CPSC353"] },   #or                 #Web Security
    "CPSC 456" : { "units" : 3, "prereq" : ["CPSC 351"] },                                  #Network Security Fundamentals
    "CPSC 458" : { "units" : 3, "prereq" : ["CPSC 351"] },                                  #Malware Analysis
    "CPSC 459" : { "units" : 3, "prereq" : ["CPSC 351", "CPSC 352", "CPSC 353"] }, #or      #Block Chain Technologies
    "CPSC 462" : { "units" : 3, "prereq" : ["CPSC 362"] },                                  #software Design
    "CPSC 463" : { "units" : 3, "prereq" : ["CPSC 362"] },                                  #Software Testing
    "CPSC 464" : { "units" : 3, "prereq" : ["CPSC 362"] },                                  #Software Architecture
    "CPSC 466" : { "units" : 3, "prereq" : ["CPSC 362"] },                                  #Software Process
    "CPSC 474" : { "units" : 3, "prereq" : ["CPSC 351"] },                                  #Parallel & Distributed Computing
    "CPSC 479" : { "units" : 3, "prereq" : ["CPSC 362"] },                                  #Intro to High performance computing
    "CPSC 483" : { "units" : 3, "prereq" : ["CPSC 335, MATH 338"] },                        #Intro to Machine Learning
    "CPSC 484" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 150B", "MATH 170B"] }, #j/s   #Principles of Computer Graphics
    "CPSC 485" : { "units" : 3, "prereq" : ["CPSC 131"] },                                  #Computational Bioinformatics
    "CPSC 486" : { "units" : 3, "prereq" : ["CPSC 386", "CPSC 484"] },                      #Game Programming
    "CPSC 489" : { "units" : 3, "prereq" : ["CPSC 486"] },                                  #Game Development Project
    "CPSC 499" : { "units" : 3, "prereq" : [] }, #can be repeated                           #Independent study 
    "EGGN 495" : { "units" : 3, "prereq" : [] }, #j/s                                       #Professional Practice (internship)


    #j/s = need junior/senior standing probably have a JS_check that does that
    #or  = they can take either or prereqs
    #can be repeated = special case where the class can be repeated up to 3 times for 9 credits
}