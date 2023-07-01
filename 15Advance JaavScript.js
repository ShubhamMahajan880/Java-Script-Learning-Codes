/* 💁‍♂️Event Propogation :-
Higher Order Function :-
Callback Function :-

 👉🏻Hoisting in JavaScript :-
 Hoisting in JS is a mechanism where variables and function declaration are moved to the top of their scope befoe the code 
For Example :-
*/
console.log(myName);
var myName;
myName = "Shubham"; // undefined

// How it will be output during creation phase :-
var myName = undefined;
console.log(myName);
myName = "Shubham";

// Currying :- 
function sum(num1){
    console.log(num1);//5
}

sum(5)(3)(8);

function sum(num1){
    return function(num2){
        // console.log(num1,num2);//5 3
        return function(num3){
            console.log(num1,num2,num3);//5 3 8
        }

    }
}
// Single line code for such currying cases :- 
const add = (num1) => (num2) => (num3) => console.log(num1+num2+num3); // 16
add(5)(3)(8);

// 👉🏻Callback Hell :- 
setTimeout(() => {
    console.log("First Learn master a language");
    setTimeout(() => {
        console.log("Second, we have to practice some codes of that language on platforms");
        setTimeout(() => {
           console.log("THird, We have to solve problems on Coding Websitesd and get a rank") ;
           setTimeout(() => {
            console.log("Fourth, Last but not Least Practice as much as questions as possible");
           }, 1000);
        }, 1000);
    }, 1000);
}, 1000);

/*
First Learn master a language
Second, we have to practice some codes of that language on platforms
THird, We have to solve problems on Coding Websitesd and get a rank
Fourth, Last but not Least Practice as much as questions as possible

This is known as "Callback Hell" in which we use multiple times settimeout() function ander k ander again and again with similar timeinterval or different also
To avoding this effords we use another concept known as "Promises"
*/
