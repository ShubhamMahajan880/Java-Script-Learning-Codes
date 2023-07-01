// 👉🏻Es-7 EcmaScript 2016-17  Properties :- 
// 1 : Array Include  "includes" is a method in Array in which we can have the information about perticular element which is included or not.
const colors = ['red','Green','Blue','Yellow','White'];
const isPresent = colors.includes('White');
console.log(isPresent);// true

const isAvailable = colors.includes('Purple');
console.log(isAvailable);//false

// 2 :- ** Operators
console.log(2**3);//8
console.log(3**3);//27



// 👉🏻Es - 8 (2017-18) Features :-
// 1) padStart :- padStart is a command uses for get the string along with blanck space(From 0 indexing or left to right) according to inserted indexing. 
let name = "Shubham";
name.padStart(5)//"Shubham"
name.padStart(8);//" Shubham"
name.padStart(15);//"        Shubham"

// 2) padEnd :- padEnd is a command uses for get the string along with blanck space(From right to left ) according to inserted indexing. 
let naam = "Vitthal";
name.padEnd(5);//Vitthal
name.padEnd(15);//"Vitthal        " 

//3) Object.value() :-  is a command introduced in Ecma Script 8 according to that we can print any values like Array,For at a sigle time
//4) Object.entries() :- is a command used for get the Key & value both pair

const person = {name : 'Shubh', age : 21};
console.log(Object.values(person)); // [ 'Shubh', 21 ]
console.log(Object.entries(person));// [ [ 'name', 'Shubh' ], [ 'age', 21 ] ]



//👉🏻 Es - 2018
//  In this edition of EcmaScript there is a new option for names as "Spread Operator"
const men = {name : "Vitthal", Hobby : "Web Development"};

const women =  { ...men };

console.log(men); // { name: 'Vitthal', Hobby: 'Web Development' }
console.log(women); // { name: 'Vitthal', Hobby: 'Web Development' }
// By using this spread Operator data will updated Automatically on manipulation



//👉🏻 Es 2019 feature :- 
// How to flatten an array :- Converting 2d and 3d array into dimensional array

const arr = [
    ['zone_1','zone_2'],
    ['zone_3','zone_4'],
    ['zone_5','zone_6'],
    ['zone_7','zone_8'],
];
// Normal Method :- 
let flattenarray = arr.reduce((accumulator, currval) => {
    return accumulator.concat(currval);
} )
console.log(arr.flat());

/*
[
  'zone_1', 'zone_2',
  'zone_3', 'zone_4',
  'zone_5', 'zone_6',
  'zone_7', 'zone_8'
]
*/
// Shortcut Way after Es - 2019
const array = [
    ['Value_1','Value_2'],
    ['Value_3','Value_4'],
    ['Value_5','Value_6'],
    ['Value_7','Value_8'],
];
console.log(array.flat());

/*
[
  'Value_1', 'Value_2',
  'Value_3', 'Value_4',
  'Value_5', 'Value_6',
  'Value_7', 'Value_8'
]
*/
// In case of multilevel array :- We can use flat(infinity) method easily
const arrey = [
    ['Kimat_1','Kimat_2'],
    ['Kimat_3','Kimat_4'],
    ['Kimat_5','Kimat_6'],
    ['Kimat_7','Kimat_8',['Kimat_9','Kimat_10']],
];
console.log(arrey.flat(Infinity));
/*
[
  'Kimat_1', 'Kimat_2',
  'Kimat_3', 'Kimat_4',
  'Kimat_5', 'Kimat_6',
  'Kimat_7', 'Kimat_8',
  'Kimat_9', 'Kimat_10'
]
*/
// Array.prototype.{flat,flatMap}
// Object.fromEntries()


//👉🏻 Es 2020 :- 
// #1 : BigInt
let oldNum = Number.MAX_SAFE_INTEGER;
console.log(oldNum); // 9007199254740991

//👉🏻 Es 2014 :- 

x = 3.1416; // Here we are not declaring x but still  we are getting value of x 
console.log(x); // 3.1416

// "Use Strict"  :- But in case of use strict mode the actions will be "Strict" and we can't use x without declaring it using let or var or any other method

"use strict"

let y = "9826410840";
console.log(y);

