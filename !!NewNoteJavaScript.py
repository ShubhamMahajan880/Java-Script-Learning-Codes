   ## . 2 Remem=ber :-
- jb 2 strings ko substract kiya jaata h to NaN(Not a Number) output milta h
- In case of double equal to (==) it always checks values only while in case of tripple equal to (===) it checks value as well as Datatype also
- in JS 5 falsy value exist :- 0,"",undefined,null,NaN,false**

#1) About Alert & Condole msg printing :-
1) alert('Shubham')
2) condole.log("Shubham is good boy)



#2) Values & variables:-
var myName = 'Shubham is sexy';
console.log(myName); //Shubham is sexy

var myAge = 21;
console.log(myAge);

var _myChest = 24;
console.log(_myChest);

var _1my__Name = 'BooBs';
console.log(_1my__Name);

var $myArmy = "MahajanConsultancy";
console.log($myArmy);


               
#3) DataTypes in JavaScript :-                
var myName = 'Shubham is sexy';
console.log(myName);

// type of Operator
console.log(typeof(myName));//string

var myAge = 21;
console.log(myAge);
console.log(typeof(myAge));//number

var iAmShubham = true;
console.log(iAmShubham);//true
console.log(typeof(iAmShubham));//boolean

// var Shubham = false;
console.log(typeof(Shubham));//undefined

console.log(10 + "20");//1020 (number and String cannot be add it can be concatinated as different different datatyeps)
console.log(9 - "5");// 4 (Here is a "BUG" because in case of substraction it is performing between number & string )
console.log("Java" + "Script"); //JavaScript
console.log("" + "");//<empty string>
console.log(" " + " ");//  Printing vacant space due to space between appostrophies. Appostrophies k pehle ya bich me space he to vo space print bhi hogi
console.log(" " + 0);//0
console.log("Shubham" - "Mahajan"); //NaN (Not a Number)
console.log("true" + "true");//truetrue

/* In JavaScript :- 
   1 - True
   0 - False
*/
console.log(true + true); //2
console.log(true + false);// 1
console.log(false + true);// 1
console.log(false - true);// -1


               
#4) Expressions & Operators in JavaScript:-

    // 4.1 - Assignment Operator:- 
    // An assignment operator assign a value to its left operand
    // Based on the value of its right operand
    // The Simple Assignment Operator is equal

    var x = 5;
    var y = 5;

    console.log("is both the x and y are equal or not" + x == y );//false
    console.log( x == y );//true
    
    // 4.2 - Arithmatic Operator:- 
    // An Arithmatic operator takes numerical values
    // either (Literal or Variable) as their operand
    // Returns a sigle numerical value 
    console.log(3+3); // 6
    console.log(10-5);// 5
    console.log(20/5);// 4
    console.log(5*6);// 3
    console.log(" Remainder Operator " + 81%8 );// 1

    // Increment & Decrement Operators:- 
    // Operator: X++ or ++X or X-- or --X
    // If used postfix, with operator after operand (ex:-, x++),
    // the increment operator increments and returns the value before incrementing
    // if used prefix, with operator before operand (for example, ++x)
    // the increment operator increments and returns the value after incrementing 

    var num = 45;
    var newnum = num++;     
    console.log(num);// 46
    console.log(newnum++);// 45

    var newnum0 = newnum0++ + 5;// (num0 + 5) 
    console.log(newnum0);
// postfix :- x ++ (Jo hoga vaad me dekha jayga abhi to jo give value h vhi consider kro)
var num1 = 15;
var newnum1 = ++num1;
console.log(num1);//16
console.log(newnum1);//16
var newnum2 = ++num1 + 5;
console.log(newnum2);

    // 4.3 - Comparision Operator:- 
    // a comparision operator compares its operand and returns a logical value based on wheather the comparision is true

    var a = 30;
    var b = 10;
    //Equal Operator (==)
    console.log(a == b);// false

    //not equal to (!=)
    console.log(a != b);//true

    //Greater than (>)
    console.log(a > b)//true

    //Greater than or equal to (>=)
    console.log(a >= b);//true

    //Less than (<)
    console.log(a < b );// false

    // Less than or equal to (<=)
    console.log(a <= b);// false


    // 4.4 - Logical Operator:- 
    // Logical Operators are typically used with Boolean (Logical) values;
    // when they are, they return a Boolean value .

    var c = 30;
    var d = -20;

    
    
    //Logical AND (&&)
    // The logical AND (&&) operator (logical Conjuction) for a
    // set of operands is true if and only if all of its operands are true
    
    console.log(c>d && d>0 && d<0);//false

    // Logical OR (||)
    // The logical OR (||) operator (logical Disjunction) for a
    // set of operands is true if and only if one or more  of its operand are true.

    console.log((c>d) || (d>0) || (d<0));//true

     // Logical NOT (!)
    // The logical NOT (!) operator (logical complement,negation) 
    // It takes truth to falsity and take vice versa.

    console.log(((a>0) || (b>0)))//true
    console.log(!((a>0) || (b>0)))//false

    console.log(false)//false
    console.log(!false)//true

    console.log(true);//true
    console.log(!true);//false

// 4.5 - String Concatenation Operator:- 
    // The Concatenation Operators (+) concatenates two string values together
    // returning another string that is the union of the two operand String 

    console.log("Hii Shubham");//Hii Shubham
    console.log("Hii" + "Shubh");//HiiShubh
    console.log("Hii " + "Shubh");//Hii Shubh

    var myName = "Vitthal";
    console.log(myName + " Girdhar" + " Mahajan");//Vitthal Girdhar Mahajan

//4.6 - Conditional (Ternary) Operator:- 
// The Conditional (Ternary) Operator is the only javascript operator that takes three operand

var umr = 17;
if(umr >= 18){
    console.log("Then you can give vote");
}
else{
    console.log("You are not eligible for voting");
}
//You are not eligible for voting

var age  = 21;
console.log((age >= 18) ? "You can vote bro" : "You cannot give vote as your not eligible for voting");
// You can vote bro               


#5) Control Statements & loops in JavaScript:-

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
 // 5.3 - While Loop
// The while statement creates a loop that executes a specified statement
// as long as the test condition evalutes to true.
var Number = 0;
while(Number <= 100){
    console.log(Number);
    Number++;
}

// 5.4 - Do-while Loop Statement
var Number = 0;

do{
    console.log(Number);
    Number++;
}while(Number <= 100); // In do while loop chahe condition satiesfied ho ya na ho hme output milta hi milta h


// 5.5 - For Loop Statement
for(var num = 1; num<= 10; num++) {
    // debugger;
    console.log(num);
}

for(var num1 = 2; num1 <= 20; num1+=2){
    console.log(num1);
}
var number8 = 8;
while(number8 <= 80){
    console.log(number8);
    number8 += 8;
}

var m,n
for(n = 1; n = 10; m = 10*n){
    console.log(m);
}

// 6 - Function Definition
// A function declaration OR function definition OR Function statement , consist of function keyword, followed by :- 

// The name of the function 
// A list of parameters to the function, enclosed in paranthesis and seperated by commas.
// The javascript statements that define the function, enclosed in curly brackets, {...}.

#Syntax of Function :- 
function functionName()
{
    //Statement
}

var a = 10;
var b = 20;
var sum = a + b;
console.log(sum);

function addition(){
    var a = 10;
    var b = 45;
    var total = a + b;
    console.log(total);
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
Add()
Add(20,30);
Add(50,12);














## BUGS in JavaScript:-
1) console.log(9 - "5");// 4 (Here is a "BUG" because in case of substraction it is performing between number & string )

2) var iAmUseless = null;
   console.log(iAmUseless);// null
   console.log(typeof(iAmUseless));// object (There is no any datatype names as OBEJCT , so there is 2nd "BUG" in javaScript)




##Interview Questions in JavaScript:-
Que. 1) Difference between null and undefined ?
Que. 2) What is NaN ?
Ans:- NaN is a property of the global Object. In other words, it is a variable in global scope, 
Que. 3) What is Difference between double(==) and tripple equl to (===)
Ans:- In case of double equal to (==) it always checks values only while in case of tripple equal to (===) it checks value as well as Datatype also

