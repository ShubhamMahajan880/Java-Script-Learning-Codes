/*
"Strinhgs in JavaScript"
1) A javascript String is zero or more characters written inside quotes
2) Javascript Strings are used for storing and manipulating text.
3) You can use single or Double Quotes
4) Strings can be created as primitives from string literals, or as objects, using the string() constructor
*/

let myName = "Shubham Mahajan";
let myProfession = "FullStack Developer";

let myfathersName = new String('Girdhar Mahajan');
console.log(myName); // Shubham Mahajan
console.log(myProfession);//FullStack Developer
console.log(myfathersName);//[String: 'Girdhar Mahajan']

/* 💁‍♂️ How to find the length of String
"String.prototype.length" Command shows the length of String
*/
console.log(myProfession.length);//19

// 👉Escape Characters in JavaScript :-
let sentence = "Shubham mahajan is going to become a \"FullStack Developer\" and will earn in Crores";
console.log(sentence);//Shubham mahajan is going to become a "FullStack Developer" and will earn in Crores

let anothersentence = "Shubham Mahajan is also a \'FrontEND Engineer\' and Freelancing in $'s";
console.log(anothersentence);//Shubham Mahajan is also a 'FrontEND Engineer' and Freelancing in $'s


/*👉Finding a String in String 
String.prototype.indexof()
- The indexof() method return the index of (the possition of) the first occurence of a specified text in a string
- Javascript counts possition from zero . 0 is the first possition in a string,1 is a second possition and 2 is a third possition and similarlly.......
- indexof always checks from Left to Right   -->
*/

const mydetails = 'Myy Self Shubham mahajan the Smart Boy';
console.log(mydetails.indexOf("Smart"));//29
console.log(mydetails.indexOf("handsome"));// -1   We know from Array in case when data is not found then it return "-1" instead of showing "ERROR"
console.log(mydetails.indexOf("a",12));// 14      By using this command it will search a string "a" after the indexing 12

/*👉"String.Prototype.lastIndexof()"
- It returns the index within the calling string object of the last occurence of Searchvalue, or -1 if not found
- LastIndexof always check from Right to Left  <-- 
*/
console.log(mydetails.lastIndexOf("Boy"));//35
console.log(mydetails.indexOf("a",12)); 

/*👉Searching for a String in String 
"String.prototype.search()"
- The Search method() seaarches a string for a specified value and return the possition of the matching
- The Search method cannot take a second start position argument
*/

const myvision = "I want to be a billinior after 2025";

console.log(myvision.search("billinior"));//15

console.log(myvision.search("Billinior"));// -1  So similarly in case of String also if data is not found it is showing -1 


/*💁‍♂️ Extracting String Parts
- There are 3 methods for extracting a part of a string
1) slice(Start,end)
2) Substring(Start,end)
3) substr(Start,length)
*/

// 1️⃣- The slice method extracts a part of a string and return the extracted part in a new string.
// - The method takes 2 parameters: the start possition, and the end possition (END not included) 

var Developer = "Frontend,Backend,FullStack"
let office = Developer.slice(0,7);
console.log(office);//Fronten

// The Slice method selects the elements starting at the given start argument, and ends at,but does not include, the given end arguemnt.
// Note :- The Original array will not be changes 

let Home = Developer.slice(7,-2);
console.log(Home);//d,Backend,FullSta

/*⏲️Challenge Time :- 
Display Only 35 Characters of a string like the one used in twitter ?
*/
let mytext = "I am Shubham Mahajan , I am a frontEnd Developer and backEnd Developer it means that i work as a FullStack Developer not only this I am a Artificial Intelligence Engineer also"
let limitedtext = mytext.slice(0,35)
console.log(limitedtext);//I am Shubham Mahajan , I am a front

console.log(mytext.length);//175 this is actual length of my written paragraph
console.log(limitedtext.length);//35  while this is limites and restricted length according to condition aS required in checkbox


/* 2️⃣The SubString() Method 
- Substring is similar to Slice().
- The difference is only that the Substring() cannot accept negative indexes.
- If we give negative values then the characters are counted from the 0th possiiton
*/

var Bangalore = "Microsoft,Amazon,Google";
// let officework = Bangalore.substring(5);
// console.log(officework);//soft,Amazon,Google
let officework = Bangalore.substring(-5);//- If we give negative values then the characters are counted from the 0th possiiton
console.log(officework);

/*3️⃣The substr() Method 
- Substr() is similar to slice()
- The difference is that the second parameter specifies the length of the extracted part.
-In case if subsstr if the second arguement is negative then there will not be any output there will be blANK space
*/

var str = "Microsoft,Amazon,Google";
let homework = str.substr(0,4);
console.log(homework);//Micr

var string = "Microsoft,Amazon,Google";
// let program = string.substr(7,-2);
// console.log(program);// Output is nothing , in caSE OF SubStr when there is 2 arguments and one is neagtive(-)


let program = str.substr(-5);
console.log(program);//oogle


/*💁‍♂️Replacing String Content()
"String.prototype.replace(searchFor,replacewith)"
- The replace() method replaces a specified value with the another value in string
*/
let loveme = "I love someone who is my soulmate";

console.log(loveme);//I love someone who is my soulmate
console.log(loveme.replace("someone","Mywife"));//I love Mywife who is my soulmate

let spiritualbond = loveme.replace('someone','mylifeline');
console.log(spiritualbond);//I love mylifeline who is my soulmate

// In case when sameword is more than one time and we have to replace all of them, then only firstone will be get replaced according to replace method()

let future = "I am the creator of my future as well as I can change my future";

console.log(future);//I am the creator of my future as well as I can change my future
console.log(future.replace('future','FUTURE'));//I am the creator of my FUTURE as well as I can change my future


/* - The replace() method does not change the string it is called on. It returns a new string
- By default, the replace() method replace, only the first match
- By default, the replace() method is case sensitive
*/


/*💁‍♂️Extracting the String Characters 
There are three methods for extracting String Character
1] charAt(position)
2] charCodeAt(position)
3] Property access [ ]

👉1) The CharAt() method 
- The CharAt() method returns the index at a specified index(POSITION) in a string
*/

let shubh = "Scientist Boy";
console.log(shubh.charAt(5));//t

console.log(shubh.charAt(10));//B

console.log(shubh.charAt(11));//O

console.log(shubh.charAt(12));//Y

/* 👉2) The charCodeAt() method
- The charCodeAt() mnethod returns the unicode of the character at a specified index in a string 
- This method returns a UTF-16 code (an integer between 0 and 65535)
*/

console.log(shubh.charCodeAt(5));//116


// ⏲️ Qus. :- Written the Unicode of the last character in the string
console.log(shubh.indexOf('y'));//12
console.log(shubh.charCodeAt('12'));//121

/*👉3) Property Access 
- ECMAscript 5 (2009) allows property access [ ] on strings 
*/
var vitthal = "Engineering";
console.log(vitthal[0]);//E

// 💁‍♂️Other Important Methods :- 
let mygoodName = "Shubham Mahajan";
console.log(mygoodName.toUpperCase());//SHUBHAM MAHAJAN
console.log(mygoodName.toLowerCase());//shubham mahajan

// 💁‍♂️Other Concat Methods :- 
// Concat() joins two or more methods

let firstname = "Shubham";
let lastname = "Mahajan";
let middlename = "Girdhar"
console.log(firstname + lastname);//ShubhamMahajan
console.log(firstname + lastname);//ShubhamMahajan

console.log(firstname.concat(lastname));//ShubhamMahajan
console.log(lastname.concat(firstname));//MahajanShubham 

console.log(firstname.concat("   ", middlename,lastname));//Shubham    GirdharMahajan 

//using EcmaScript Concept :- 
console.log(`${firstname} is a name and ${lastname} a surname`);//Shubham is a name and Mahajan a surname


/* 💁‍♂️ trim Method :- 
"String.trim()"
- The trim() method removes whitespace from both sides of a string
*/

let name = "                       *Shraddha Khapra *    " ;
console.log(name);//                       *Shraddha Khapra * 
console.log(name.trim());//*Shraddha Khapra *


/*💁‍♂️Split() method :- 
- Converting a String to an Array
- A string can be converted into an array with the split () method
*/

var text = "S,h,u,B,h,A,m";
console.log(text);//S,h,u,B,h,A,m

console.log(text.split(",")); // Split with Commas
/* [
  'S', 'h', 'u',
  'B', 'h', 'A',
  'm'
]
*/
console.log(text.split(" ")); // Split with Space    [ 'S,h,u,B,h,A,m' ]

console.log(text.split("|"));//[ 'S,h,u,B,h,A,m' ]

















