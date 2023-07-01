// #5) Control Statements & loops in JavaScript:-               
    // 5.1 - If-Else Statement
    // The if statement executes a statement if a specified condition is truthy.
    // If the condition is falsy , another statement can be executed
    var developer = 'fullstack';
    if (developer == 'fullstack'){
        console.log("You can do both the work");
    }
    else{
        console.log("You have to select either one");    
    } 
    //You can do both the work
    var developer = 'frontend';
    if (developer == 'fullstack'){
        console.log("You can do both the work");
    }
    else{
        console.log("You have to select either one");    
    }
    //You have to select either one
    
    var year = 2016;
    if(year % 4 === 0){
        console.log("Then  year " + year + " is a leap year");
    }
    else{
        console.log("year " + year +  "not a leap year");
    }
    //Then  year 2016 is a leap year
    
    var year = 2017;
    if(year % 4 === 0){
        console.log("Then  year " + year + " is a leap year");
    }
    else{
        console.log("year " + year +  " not a leap year");
    }
    // year 2017 not a leap year
    
    // qun:- What is Truthy and Falsy Values in JS?
    
    // - in JS 5 falsy value exist :- 0,"",undefined,null,NaN,false**
    
    var Salary  
    if(Salary = 0){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    //YOu have to continue the job (Here condition is equal to 0 still result in the favour of else because of FALSY VALUES in JS  )
    if(Salary = 10){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    // You should leave the job
    if(0){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    //YOu have to continue the job
    if(undefined){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    //YOu have to continue the job
    if(null){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    //YOu have to continue the job
    if(""){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    //YOu have to continue the job
    if(NaN){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    //YOu have to continue the job
    if(false){
        console.log("You should leave the job");
    }
    else{
        console.log("YOu have to continue the job");
    }
    //YOu have to continue the job
    
    
    // 5.2 - Switch Statement
    // Evalutes an expression, matching the expression's value to a Case Clause, and executes statements associated with that case.
    
    var PI = 3.1412, l = 5, b = 6, r = 2;
    // var Area  = "Triangel"
    // if(Area == "Circle"){
    //     console.log("Then area is given is :  " + PI*r**2);
    // }
    // else if(Area == "Triangel"){
    //     console.log("Then area will represented as :  " + (l * b)/2);
    // }
    // else if(Area == "rectangle") {
    //     console.log("Then area is :  " + (l * b));
    // }
    // else{
    //     console.log("Ths is not valid");
    // }
    // Then area will represented as : - 15
    
    //  same Qun with the help of switch case statement
    var Area  = "Circle"
    switch(Area){
        case "Circle" : 
        console.log("Then area is given is :  " + PI*r**2);
        break;
        case "Triangel" :
        console.log("Then area will represented as :  " + (l * b)/2);
        break;
        case "rectangle" :
        console.log("Then area is :  " + (l * b));
        break;
        default :
        console.log("Ths is not valid");    
        //Then area is given is :  12.5648
    
    
    
    
    
    
    
    
    
    
    }
