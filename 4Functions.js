// 6 - Function Definition
// A function declaration OR function definition OR Function statement , consist of function keyword, followed by :- 

// The name of the function 
// A list of parameters to the function, enclosed in paranthesis and seperated by commas.
// The javascript statements that define the function, enclosed in curly brackets, {...}.

var a = 10;
var b = 20;
var sum = a + b;
console.log(sum);//30

function addition(){
    var a = 10;
    var b = 45;
    var total = a + b;
    console.log(total);//55
}

// Calling of Functions 
//Defining a function does not execute it.
// A javascript fnction is executed when someone call it.

addition();

// Function Parameter and Function Argument :- 
//1) Function Parameters are the names listed in function's Definition
//2) Function Arguuments are the real values passed to the function

function Add(a,b){
    var total = a + b;
    console.log(total);
}
Add()//NaN
Add(20,30);//50
Add(50,12);//62

// INTERVIEW QUESTIONS :- 
// Why Functions ?

// U can reuse the code : Define the code once and use this code as many times
// U can use the same code many times with different Arguments,
OR
// A function is a group of reusable code which can be called Anywhere
// This eliminates the writting of same code again and again

//Function Expression :- 

var funExp = function(a,b){
    return total = a + b;
}
var sum = funExp(15,15);
var sum = funExp(20,15);
console.log(sum);



