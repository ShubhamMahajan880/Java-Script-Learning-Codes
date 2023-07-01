/* Array CRUD(Create,Read,Update and Delete) Performance
 "Array.prototype.push()"
The Push() method adds one or more elements to the array
Element will be added at the END of an array and it returns the new length of the array.
*/

const Shubham = ['FrontEnd','BackEnd','Artificial Intelligence','FullyStacked'];
Shubham.push('WordpressDeveloper');
console.log(Shubham);
Shubham.push('Software Developers');
console.log(Shubham);




/* "Array.prototype.unshift()"
The unshift() method adds one or more elements to the array
Element will be added at the BEGINNING of an array and it returns the new length of the array.
*/

Shubham.unshift('GATE Aspirant');
console.log(Shubham);



/* "Array.prototype.pop()"
The Pop() method removes the LAST ELEMENT of an array and returns that element 
this method changes the length of an array
*/
const Vitthal = ['10th','12th','Graduation','PostGraduation','Placed'];
console.log(Vitthal);
console.log(Vitthal.pop());
console.log(Vitthal);


/* "Array.prototype.shift()"
The shift() method removes the FIRST ELEMENT of an array and returns that element
this method changes the length of an array
*/
Vitthal.shift();
console.log(Vitthal);

/*Splice Method 
"Array.prototype.splice()"
It Adds and/or removes elements from an array from the middle, Top or Bottom any where
*/
const months = ['Jan','March','April','June','July'];
// Ques. - 1 :- Add Dec month in the array ? SOLUTION :-
const newMonth = months.splice(5,0,'Dec');
console.log(months);
//  In case when I don't know what is the length of string and I have to add a element at last then use NAMEOFARRAY.LENGTH 
// const newmonth = months.splice(months.length,0,Hackober);
console.log(months);

// Ques. - 2 :- What is the Retunrn Method of Splice Method:-
console.log(newMonth);//[]

const updatemonth = months.splice(1,1,'March'); // In splice method first index is uses for edit at that place and second index is uses for delete at that place and third is that keyword which we have to use
console.log(months);//[ 'Jan', 'March', 'April', 'June', 'July', 'Dec' ]


/*
Flat Array function :- Aerrow Function
const Array;
let NAMEOFARRAY = Array.map/filter/reduce(() => {
    return NAMEOFARRAY.(ALONG WITH FUNCTION);
})
*/


/* Map & Reduce Method in Array
"Array.prototype.map()"
let newArray = arr.map(callback(currentvalue[,index[,array]])){
    return element for newArray, after executing something
}[,thisArg]);
Returns a new array containing the result of calling a function on every element in this array
*/

// Understanding of MAP METHOD :-- 

const array1 = [1,4,9,16,25];
//I want all the numbers>9
let newArr = array1.map( (cuurentElemnent,index,array) => {
    return cuurentElemnent > 9;
})
console.log(array1);//[ 1, 4, 9, 16, 25 ]
console.log(newArr);//[ false, false, false, true, true ]

const array2 = [36,49,64,81,100];
//I want all the numbers greater than 64
let latestarray = array2.map((crntelement,index,arrayFROMWHICHITBELONGS) => {
    return `Index no = ${index} and the value is ${crntelement} belongs to ${arrayFROMWHICHITBELONGS} `
})
console.log(array2);//[ 36, 49, 64, 81, 100 ]
console.log(latestarray); 
/*
[
  'Index no = 0 and the value is 36 belongs to 36,49,64,81,100 ',
  'Index no = 1 and the value is 49 belongs to 36,49,64,81,100 ',
  'Index no = 2 and the value is 64 belongs to 36,49,64,81,100 ',
  'Index no = 3 and the value is 81 belongs to 36,49,64,81,100 ',
  'Index no = 4 and the value is 100 belongs to 36,49,64,81,100 '
]
*/
// Beauty of MAP Method is "It returns new array without mutating the Original Array "

// challenge Time :- Que.1) Find the squareroot of given array [25,36,49,64,81,100]
let array = [25,36,49,64,81,100];
let arraysquareroot = array.map((crrntelement) => {
    // return crrntelement;
    return Math.sqrt(crrntelement);
})
// console.log(arraysquareroot);//[ 25, 36, 49, 64, 81, 100 ]
console.log(arraysquareroot);//[ 5, 6, 7, 8, 9, 10 ]

// Understanding of FILTER METHOD :- 

// challenge Time :- Que.2) Multiply those elements by 2 and return only that element  which are greater than 10
let learningarray = [2,3,4,6,8];
let calculatedarray = learningarray.map((currentelement) => {
    return currentelement * 2;
}).filter((currentelement) => {
    return currentelement > 10;
})
// console.log(calculatedarray);//[ 4, 6, 8, 12, 16 ]
console.log(calculatedarray);//[ 12, 16 ]

//  Same Concept by CHAINING METHOD :- uses for single line of code instead of using return 

let againarray = [5,10,15,20,25]
let newarray = againarray.map((pursuingelement) => pursuingelement * 2 ).filter((pursuingelement) => pursuingelement > 10);
console.log(newarray) // [ 20, 30, 40, 50 ]


/* "Reduce method in Array"
Flatten an array means to convert the 3d array to 2d array into a single dimensional array

The reeduce() method executes a reducer function (that you provide)
On each element of the array, resulting in single output value.

The reducer function takes four arguments :
1) Accumulator
2) Current Value
3) Current Index
4) Source Array  

In my words :- Reduce method tb use kiya jaata h jb multiple numbers ka + krna ho, multiple numbers ka % nikalna ho becuase inka answer ek single value hi aati h which can be find by using reducer function
    In previous map method we use three parameters (currentelement,index,nameofarray) but in reduce  method we use 4 parametes along with this 3 parameters 4th one is accumulator ((accumulator,currentelement,index,nameofarray)) 
    Accumulator stands for "jma krna" 
*/

let arr = [5,6,2];

let sum = arr.reduce((accumulator, currentelement, index,sourceNMEofArray) => {
    return accumulator += currentelement
})
console.log(sum);//13

// In terms of Chaining Process :- 
let ourarray = [5,10,20,30,50];

let yoarray = ourarray.map((element) => element * 2).filter((element) => element>10).reduce((accumulator,element) => {
    return accumulator += element;
});
console.log(yoarray);

let tryingarray = [10,5,2];
let multiplication = tryingarray.reduce((accumulator,currentelement,index,nameofarray) => {
    return accumulator *= currentelement
})
console.log(multiplication);//100

// How to flattern an array 
// Converting 2D array to 3D array into one Dimensional array

const arrey = [
    ['zone_1','Zone_2'],
    ['zone_3','Zone_4'],
    ['zone_5','Zone_6'],
    ['zone_7','Zone_8']
];
let flatarr = arrey.reduce((accumulator,currentelement) => {
    return accumulator.concat(currentelement);
})
console.log(flatarr);
/*
[
  'zone_1', 'Zone_2',
  'zone_3', 'Zone_4',
  'zone_5', 'Zone_6',
  'zone_7', 'Zone_8'
]
*/


const arre = [
    ['zone_1','Zone_2'],
    ['zone_3','Zone_4'],
    ['zone_5','Zone_6'],
    ['zone_7',['zone_7','Zone_8']]
];
let flattenarr = arre.reduce((accumulator,currentelement) => {
    return accumulator.concat(currentelement);
})
console.log(flattenarr);
/*
[
  'zone_1',
  'Zone_2',
  'zone_3',
  'Zone_4',
  'zone_5',
  'Zone_6',
  'zone_7',
  [ 'zone_7', 'Zone_8' ]
]
*/
