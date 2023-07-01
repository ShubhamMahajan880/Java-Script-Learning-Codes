// 💁‍♂️ Creating Date & Time :- 
/* - JavaScript Date Objects represents a single moment in time in a platform-independent format. 
- Date Objects contain a number that represents milliseconds since 1 january 1970 UTC.
- Creating Date Objects :- there are 4 ways to create a new date object:
*/

// new Date()
// new Date(year,month,day,hours,minutes,seconds,millisenconds)  (It takes 7 Arguements)
// new Date(milliseconds) {We cannot avoid month section}
// 👉

let currDate = new Date();
console.log(currDate);//2023-06-25T17:07:58.423Z
console.log(new Date());

console.log(new Date().toLocaleString());//6/25/2023, 10:41:49 PM

console.log(new Date().toString());//Sun Jun 25 2023 22:42:48 GMT+0530 (India Standard Time)


// 👉Date.now()
// Returns the numeric value corresponding to the current time the number of milliseconds eclapsed since January 1,1970 00:00:00 UTC

console.log(Date.now());//1687713580183

//  new Date(year,month....)
// - 7 numbers specify year,month,day,hour,minute,seconds,millisenconds
// Note :- jAVASCRIPT counts months from 0 to 11
// - January is 0 and December is 11.

var D = new Date(2023,5,25,55,10,5);
console.log(D.toLocaleString());// 6/27/2023, 7:10:05 AM

// new Date(dateString)
// new Date(dateString) creates a new date object from a date string
var d = new Date("June 25, 2023 11:03");
console.log(d);//2023-06-25T05:33:00.000Z
console.log(d.toLocaleString());//6/25/2023, 11:03:00 AM

var d = new Date(0);
console.log(d);//1970-01-01T00:00:00.000Z

var d = new Date(1687713580183);
console.log(d);//2023-06-25T17:19:40.183Z


// 👉 Dates Methods :-
const curDate = new Date();

//How to get the individual dATE  and every time ASPECT using "GET"

console.log(curDate.toLocaleString());// 6/25/2023, 11:14:55 PM
console.log(curDate.getFullYear());// 2023
console.log(curDate.getMonth());// 5
console.log(curDate.getDate());// 25
console.log(curDate.getDay());// 0

// 👉🏻 How to SET individual Dates using "SET" Method :-

const currentdate = new Date();
console.log(currentdate.setFullYear(2022));//1656180738838
// The setFullYear() method can optionally set month and day
console.log(currentdate.setFullYear(2022,10,5));//1667671938838
// let setmonth = currentdate.setmonth(10);
// console.log(setmonth);
console.log(currentdate.setMonth(6));
console.log(currentdate.toLocaleString());//11/5/2022, 11:42:18 PM


//👉Time Methods :- get the time using "GET" Method 
const curTime = new Date();

// How to get the individual Time 

console.log(curTime.getTime());//1687717157007

// The getTime() method returns the number of milliseconds since january 1,1970

console.log(curTime.getHours());//23

// The gethours() method return the houra of a date as a number 

console.log(curTime.getMinutes());//49
console.log(curTime.getSeconds());//17
console.log(curTime.getMilliseconds());//7


// 👉🏻How to set the individual time using "Set" Method:- 
let currentTime = new Date();
console.log(currentTime.setHours(12));//1687761932451
console.log(currentTime.setMinutes(10));//1687761932451
console.log(currentTime.setSeconds (5));//1687761932451
console.log(currentTime.setUTCMilliseconds(1));//1687761605001

/*  Timer Clock COde

(function(){
    setInterval(() => {
        var d = new Date().toLocaleTimeString();
        document.getElementById("demo").innerHTML = d;
    },1000)
})();
*/

// 👉🏻Important Learning :- 

// 1) For getting Only time

new Date().toLocaleTimeString();


// 2) For getting Only Date

new Date().toLocaleDateString();

// 3) For getting  time & Date both parallely

new Date().toLocaleString();




