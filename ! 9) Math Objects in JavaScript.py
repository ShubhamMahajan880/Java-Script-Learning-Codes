/* 💁‍♂️Section - 9) Maths Objects In JavaScript
 The JavaScript Math Object allows you to perform mathematical task on numbers 
 */

/* 👉 1) Math.PI() Command :- 
 Command uses for get the value of PI at a time
*/
console.log(Math.PI); //  3.141592653589793


/* 👉 2) Math.round() Command :- 
return the value of x rounded to its nearest integer
*/
let number = 25.12369845;
console.log(Math.round(number)); // 25

let num = 25.5689;
console.log(Math.round(num)); // 26


/* 👉 3) Math.pow() Command :- 
Math.pow(x,y) return the value of x to the power of y
*/
console.log(Math.pow(2,4)); // 16
console.log(2**4); // 16


/* 👉 4) Math.sqrt() Command :- 
Math.sqrt(x) returns the squareroot of x
*/

console.log(Math.sqrt(25)); // 5
console.log(Math.sqrt(36)); // 6
console.log(Math.sqrt(6254)); // 79.08223567907018


/* 👉 5) Math.abs() Command :- 
Math.abs() returns the absolute(Possitive) value of x
*/

console.log(Math.abs(-899)); // 899
console.log(Math.abs(-55.5)); // 55.5
console.log(Math.abs(-0)); // 0
console.log(Math.abs(45-50)); // 5


/* 👉 6) Math.ceil() Command :- 
Math.ceil() returns the value of x rounded up to its nearest integer
*/

console.log(Math.ceil(4.51)); // 5  In case of Ceil We Will get Highest Number as ceiling(Roof)
console.log(Math.round(4.51)); // 5
console.log(Math.ceil(99.01)); // 100
console.log(Math.round(99.01));// 99 while in case of round we will get number according to roundoff rule , If num > 5 then round up with 1 and if num < 5 then round down (1) less 


/* 👉 7) Math.floor() Command :- 
Math.floor(x) returns the value of x rounded down to its nearest integer
*/

console.log(Math.floor(4.7)); // 4
console.log(Math.floor(101.5898978)); // 101


/* 👉 8) Math.min() Command :- 
Math.min() can be used to find the lowest value in a list of arguments 
*/

console.log(Math.min(0,150,-25,89,798,-2359)) // -2359


/* 👉 9) Math.max() Command :- 
Math.max() can be used to find the Highest value in a list of arguments 
*/

console.log(Math.max(890,230,5656,9000,2500)); // 9000


/* 👉 10) Math.random() Command :- 
Math.random() returns a random number between 0 (Inclusive), and 1 (Exclusive)
*/

console.log(Math.random()); // 0.13348396787496375
console.log(Math.random()); // 0.546483269728073
console.log(Math.random()); // 0.4557664970261328 By using this random we method we will always get a number between 0 to 1


/* 👉 11) Math.trunc() Command :- 
Math.trunc() method returns the integer part of a number. Decimal k pahle ka part jo bhi ho either it is possitive or negative it will return that part before Decimal
*/

console.log(Math.trunc(7.6)); // 7
console.log(Math.trunc(-11.56)); // -11 

 // Note :- If the argument is a possitive number, Math.trunc() is equivalent to Math.floor(), Otherwise Math.trunc() is equivalent to Math.ceil()
