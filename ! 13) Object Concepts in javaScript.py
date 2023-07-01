/*💁‍♂️Section - 12) OPS in JavaScript :- 

1️⃣ What is Object Literal?
Ans :- Object literal is simply a key:value pair Data Struture. Storing variables and functiond together in one container.

object = Mobile

How to create an Object ?
1st way :-
*/
let myinformation = "Shubham Mahajan";
console.log(myinformation);
// Another way :- 
let mydetails = {
    myname : "Shubh",
    myAge : 21,
    getData : function(){
        console.log(`my name is ${mydetails.myname} and along with my age is ${mydetails.myAge}`)
    }

}
mydetails.getData();//my name is Shubh and along with my age is 21


// 2nd way) No need to write function after es6

let info = {
    myname : "Shubh",
    myAge : 21,
    getData (){
        console.log(`my name is ${info.myname} and along with my age is ${info.myAge}`)
    }

}
info.getData();//my name is Shubh and along with my age is 21

// 👉What if we want object as a value inside an Object
let information = {
    myname : {
      NAME : "Shubh",
      hobby : "Web Development"
    },
 myumr : 21,
 getData(){
    console.log(`name is ${information.myname} and age is ${information.myumr}`);
}
}
console.log(information.myname.hobby);//Web Development

/*2️⃣ What  is this object ?
The This object can have different values depending on where it is placed.
Example :- 1)
*/
console.log(this);//{}
// console.log(this.alert('Ultimate')); // Ultimate in alert tab

// Example - 2 :-
function myname(){
    console.log(this);
}
myname();
/*
<ref *1> Object [global] {
  global: [Circular *1],
  queueMicrotask: [Function: queueMicrotask],
  clearImmediate: [Function: clearImmediate],
  setImmediate: [Function: setImmediate] {
    [Symbol(nodejs.util.promisify.custom)]: [Getter]
  },
  structuredClone: [Getter/Setter],
  clearInterval: [Function: clearInterval],
  clearTimeout: [Function: clearTimeout],
  setInterval: [Function: setInterval],
  setTimeout: [Function: setTimeout] {
    [Symbol(nodejs.util.promisify.custom)]: [Getter]
  },
  atob: [Getter/Setter],
  btoa: [Getter/Setter],
  performance: [Getter/Setter],
  fetch: [AsyncFunction: fetch],
  crypto: [Getter]
}
*/
// // Example 3 :-
// let myname = 'Shubh';
// function myname() {
//     console.log(this.myname);
// }
// myname();


// 7️⃣Spread Operator :- 

const colors = ['red','Green','blue','yellow','Pink',];

const mycolor = ['red','Green','blue','Black','Violet','yellow','White','Pink',];

// 2nd time add one more color on top and tell we need to write it again
// on mycolor array too

const mylovelycolors = [...colors,'Brown','Mehroon','Kesariya'];
console.log(mylovelycolors);
/*
[
  'red',     'Green',
  'blue',    'yellow',
  'Pink',    'Brown',
  'Mehroon', 'Kesariya'
]
This is all about Spread Operator, if one Array has been declared and we have to add some more element in another array with similar elements and adding more elements then instead of writing all elements we use seperate operator and write new names
*/



