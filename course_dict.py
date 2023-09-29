


courses = {
    #lower division core (18 units)
    #lower


    #value 0
    "CPSC 120" : { "units" : 3, "prereq" : [], "value" : 0},
    "CPSC 253" : { "units" : 3, "prereq" : [] ,"value": 0},     
    "MATH 170A" : { "units" : 3, "prereq" : [], "value" : 0 },
    "MATH 150A" : { "units" : 4, "prereq" : [], "value" : 0 },                                    

    #value 1                                           
    "CPSC 121" : { "units" : 3, "prereq" : ["CPSC 120"] , "value" : 1},
    "MATH 150B" : { "units" : 4, "prereq" : ["MATH 150A"] , "value" : 1},                                                                           
    "MATH 170B" : { "units" : 3, "prereq" : ["MATH 170A"] , "value" : 1}, 

    #value 2                               
    "CPSC 131" : { "units" : 3, "prereq" : ["CPSC 121"] , "value" : 2},
    "CPSC 386" : { "units" : 3, "prereq" : ["CPSC 121"] , "value" : 2}, 
    "MATH 338" : { "units" : 4, "prereq" : ["MATH 150B"] , "value" : 2},

    #value 3                                
    "CPSC 223" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},                               
    "CPSC 315" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},                               
    "CPSC 323" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},                                
    "CPSC 332" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},                                 
    "CPSC 351" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},                                 
    "CPSC 362" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3}, 
    "CPSC 485" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3}, 
    "CPSC 254" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},
    "CPSC 411A" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},
    "CPSC 411" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3}, 
    "CPSC 349" : { "units" : 3, "prereq" : ["CPSC 131"] , "value" : 3},
    "CPSC 352/452" : { "units" : 3, "prereq" : ["MATH 170B, CPSC 131", "CPSC 253"] , "value" :  3},       
    "CPSC 375" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 338"], "value" :  3 },
    "CPSC 240" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 170A"], "value" : 3 },
    "CPSC 335" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 170A", "MATH 150A"] , "value" : 3},
    #value 4                              
    "CPSC 471" : { "units" : 3, "prereq" : ["CPSC 351"] , "value" : 4},   
    "CPSC 458" : { "units" : 3, "prereq" : ["CPSC 351"] , "value" : 4},                                      
    "CPSC 474" : { "units" : 3, "prereq" : ["CPSC 351"] , "value" : 4},  
    "CPSC 456" : { "units" : 3, "prereq" : ["CPSC 351"] , "value" : 4}, 
    "CPSC 431" : { "units" : 3, "prereq" : ["CPSC 332"] , "value" : 4},                                  
    "CPSC 440" : { "units" : 3, "prereq" : ["CPSC 240"] , "value" : 4},                                  
    "CPSC 449" : { "units" : 3, "prereq" : ["CPSC 332"] , "value" : 4},
    "CPSC 454" : { "units" : 3, "prereq" : ["CPSC 351", "CPSC 253"], "value" : 4 },                      
    "CPSC 455" : { "units" : 3, "prereq" : ["CPSC 351", "CPSC 253"], "value" : 4 },
    "CPSC 459" : { "units" : 3, "prereq" : ["CPSC 351", "CPSC 352", "CPSC 253"] , "value" : 4}, #or                                                                   
    "CPSC 483" : { "units" : 3, "prereq" : ["CPSC 335, MATH 338"] , "value" : 4},
    "CPSC 481" : { "units" : 3, "prereq" : ["CPSC 335", "MATH 338"] , "value" : 4},
    "CPSC 439" : { "units" : 3, "prereq" : ["CPSC 121", "MATH 170B"], "value" : 4 },
      
    #value 5
    "CPSC 490" : { "units" : 3, "prereq" : ["CPSC 362"] , "value" : 5},
    "CPSC 462" : { "units" : 3, "prereq" : ["CPSC 362"] , "value" : 5},  
    "CPSC 463" : { "units" : 3, "prereq" : ["CPSC 362"] , "value" : 5},
    "CPSC 464" : { "units" : 3, "prereq" : ["CPSC 362"] , "value" : 5},
    "CPSC 466" : { "units" : 3, "prereq" : ["CPSC 362"] , "value" : 5},
    "CPSC 479" : { "units" : 3, "prereq" : ["CPSC 362"] , "value" : 5},
    "CPSC 484" : { "units" : 3, "prereq" : ["CPSC 131", "MATH 150B", "MATH 170B"] , "value" : 5}, #j/s
    #value 6
    "CPSC 491" : { "units" : 3, "prereq" : ["CPSC 490"], "value" : 6 },   
    "CPSC 486" : { "units" : 3, "prereq" : ["CPSC 386", "CPSC 484"] , "value" : 6},                               
                                                                                                                                                          
    #value 7                                                                                                                                                                   
    "CPSC 489" : { "units" : 3, "prereq" : ["CPSC 486"] , "value" : 7},  

    "CPSC 499" : { "units" : 3, "prereq" : [] , "value" : 0}, #can be repeated                           
    "EGGN 495" : { "units" : 3, "prereq" : [] , "value" : 0}, #j/s
                              
                    

 #j/s                                       


    #j/s = need junior/senior standing probably have a JS_check that does that
    #or  = they can take either or prereqs
    #can be repeated = special case where the class can be repeated up to 3 times for 9 credits




}
