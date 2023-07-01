// Modern javascript
// ECMAScript - 2015 is knows as ES6
// LET vs CONST vs VAR
//var => Function Scope
// let and Const => Block Scope

// var myName = "Shubham Developer";
// console.log(myName);//Shubham Developer
// myName = "I am a web developer";
// console.log(myName);//Shubham Developer

// let myName = "Shubham Developer";
// console.log(myName);
// myName = "I am a web developer";
// console.log(myName);

// var ka scope globally hota he jabki let ka scope kevl curely brackets k ander hota h
// in case of CONST there will not any change in entire code 

//Array 1) Traversal in Array :- If we want to get single data at a time 
                            //   If we want to change the data
                            
var Shubham = ['Frontend','backend','Fullstack','100000','500000'];
console.log(Shubham[0]);//Frontend
console.log(Shubham.length);//5

for(var i=0; i<Shubham.length; i++) {
    console.log(Shubham[i]);// Frontend backend Fullstack 10000 5000000
}

//Concept of For in Loop :- For in loop is uses for return the index number

for(let elements in Shubham ){
    console.log(elements);// 0 1 2 3 4
}

//Concept of For of Loop :- For of loop is uses for return the elements or all names of that indx

for(let elements of Shubham){
    console.log(elements);
}

//Concepts of ForEach loop :- NAMEOFARRAY.prototype.forEach(
//                            Calls a function for each statement in the array
Shubham.forEach(function(element,index,array){
    console.log(element + "index : " + index);
})








