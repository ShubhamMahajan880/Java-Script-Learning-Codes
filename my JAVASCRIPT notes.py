In javascript:-
    We use <script> tag for writing JAVASCRIPT 
1) Alert is uses for print required output in alert way (Like a pop up msg appears at current page)
2) in cosole.log we can print message on the console board

3) Javascript is a programming language while HTML is a markup language

4) name of class/id.innerHTML is uses for editing in console menu

5) Basic Commands in JavaScript:-

- document.getElementsByTagName('h1')[0].style.fontsize = "233px"

- document.write("This is a place for writing");

- console.warn("THis is a warning for you please don't click") and this is a warning command that's why yello troubleshoot board also appears

-console.error("You clicked now you have trapped"); and error msg therefore REDEXCLAMATION MARK appears

-console.clear() For clear the console board

-console.log(number1+number2) Uses for addition of two given Datatype numbers

#For Printing in JavaScript:- 

-alert("Shubham") :- this will print msg in form of alert information in chrome

-console.log() :- command is uses for print  content inside brackets

"""

console.log(num1)
455

console.log(num2)
566

console.log(str1)
Shubham is Learning 

console.log(str2)
Mahajan is also with him 

console.log(marks)
Object { FrontEndDvelopement: 100, BackEndDvelopement: 50, FullStackDvelopement: 75 }
"""
# Let in javascript is uses for create any string or any other function and etc.

-If the value of variable is not defined then this shows UNDEFINED and is value of any variable is given as undefined then also prints undefines

- UNDEFINED:- varibale bna kr chood diya h and usme kuchh daala nhi h

-NULL:- variable declare kr k baad isme kuchh likhna nhi h

- in JAVASCRIP also INDEXING started from zero

- in javascript Number prints in  BLUE DIGITS while character inside string written content prints with black color

- forEach also a method for printing all the values



"""
Array Operations :- 
"""

- NAMEOFARRAY.pop() command is uses for pop out the last element

- NAMEOFARRAY.push() command is uses for Push any element in array

- NAMEOFARRAY.shift() command is uses for remove first element from an Array

- NAMeOFARRAY.unshift("XYZ") command is uses for add XYZ named element at the first place of element

- const newLen = NAMEOFARRAY.unshift("XYZ") 
  console.log(newLen); // command is uses for print the  nw lenght of array 

- NAMEOFARRAY.toString(); command is uses for print array elements in String Format

- NAMEOFARRAY.sort(); command uses for sort the fucntion      




"""
String Operations:-
"""

- console.log(NAME OF STRING.length);

- console.log(Stringhere.indexOf("ANY WORD FROM STRING")) is commad uses for get thr indexing of particular word

- console.log(Stringhere.slice(0, 7)); uses for print initial 0 to 7 indexing values

- d = Stringhere.replace("Shubham", "Vitthal");
console.log(d,Stringhere) uses for replace any particular word from string.



"""
Date and Current Time Operations:- 
"""


let myDate = new Date();
console.log(myDate);  command is uses for print the current date

console.log(myDate.getTime()); gives time in seconds 
console.log(myDate.getFullYear()); gives going on year

console.log(myDate.getDay()); // 6 gives day which is present
console.log(myDate.getHours()); // 21 kitni bje h ya kitne ghnte huiye h


# DOM Manipulation featurs by

let element = document.getElementById('click');
console.log(element);

gEbI :- is the shortcut for printing GetElementBy Id

let elementClass = document.getElementsByClassName("container")
console.log(elementClass); 
elementClass[0].style.background = "Blue"; 
elementClass[1].style.background = "red";

.getElementsByName('button'); is a way to collect all the buttons of code
getElementsByTagName('div') is way to get all div sections


createdElement = document.createElement('p');  //  This is a command for creating element in DOM 
createdElement.innerText = "This is a latest Paragraph"; // Command uses for inserting inner txt 

tn[0].appendChild(createdElement); 
tn[0].replaceChild(createdElement2, createdElement);




""" in DOM (Document Object Model):-  """

1) document.location  // command  is uses for getting the address of documrn or location of document
Location file:///D:/Study%20Material/Never%20Stop%20Learning%20Something%20New/FullStack%20Web%20Development/Proper%20Learning/Course%20Content/++++JavaScript/index.html
​
2) document.URL // Document.url command has also the same work
"file:///D:/Study%20Material/Never%20Stop%20Learning%20Something%20New/FullStack%20Web%20Development/Proper%20Learning/Course%20Content/++++JavaScript/index.html"

3) document.scripts // command is uses for getting all the scripts
HTMLCollection { 0: script, 1: script, length: 2 } 

4) document.links // Command is uses for collect all the links
HTMLCollection { length: 0 }

5) document.forms // command is uses for getting all the forms 
HTMLCollection { length: 0 }

​
6) document.images // command is uses for getting all the images from the page
HTMLCollection { length: 0 }

7) document.domain // command is uses for getting the domain of webpage only




""" Selecting by Query Commands :- """

1) select = document.querySelector('.NAME OF CLASS/DIV/ID') // This command is uses for select any statement from code 
   console.log(select)​

2) select = document.querySelectorAll('NAME OF CLASS/DIV/ID') // This command is uses for select all statements from code
   console.log(select)



"""Events in JavaScript:- """

Events :- Movement of mourse for click purpose or any other is event

1)  function YouhaveClicked(){     // Click waala event
    console.log("You have Clicked at this button already") 
    } 

2) window.onload = function(){     //  Page Loading Event
        console.log("THe Document has been loaded Already")
    }

# addEventListener command is uses for kisi function ko perform kiya ja chuka h and uska use ho chuka h show krne k liye krte h

3) firstcontainer.addEventListener('click',function(){  // addEventListener command is uses for kisi function ko perform kiya ja chuka h and uska use ho chuka h show krne k liye krte h 
    in terms of .....   
   NAME OF ID.addEventListener('NAME OF EVENT',function(){ // Here click function ka mtlb h ki us pr cursor aaya h
       console.log('JO BHI PERFORMED HUA VH LIKHE')
       }) 

4) firstcontainer.addEventListener('mouseover',function(){ // mouse over function ks mtlb h ki iss  perticular class ya id pr mouse aaya
        console.log("Aap us pr mouse le jaa chuke h")
        })                                                           

5) firstcontainer.addEventListener('mouseout',function(){ // mouseout function stands for aapka mouse vapas bahar aa chuka  h
        console.log("Aaapka Mouse Bahar Aa Chuka He")
        })

6) firstcontainer.addEventListener('mouseup',function(){ ..mouseup function stands for aapne apne mouse se uss section pr click kr rk rkh h
        console.log("Aapne mouse Se Click kr k rkha h") 
        })



""" USe of Aerrow Function """
//  Generaly addition using Sum Function       
    function Sum(a,b){  
        return a+b;
    }

//  With the help of Aerrow Function : -
    sum = (a,b)=>{
        return a+b;
    }

""" SetTimeOut:- """
setTimeout(logkaro, 1000);
it stnads for:- 
setTimeout(NAME OF FUNCTION, AFTER MILLISECONDS)

"""SetInterval :- """
setInterval(Showtext,1000);
ir stands for :-   // yh usi chz ko baar baar utne time interval k baad apne aap show krte rhega
setInterval(NAME OF FUNCTION, AFTER MILLISECONDS)


""" ClearInterval :- """
clr =  setInterval(Showtext,1000);
clearInterval(clr)  # ClearInterval command is uses for stop the setinterval which is executing again and again



"""LocalStorage in JavaScript :- """

1)  localStorage.setItem('name','Shubham') // command is uses for set items
    undefined
    localStorage
    Storage { name: "Shubham", length: 1 }

1.1) localStorage.removeItem('name') // .removeItem is uses for remove a single function

2)  ​localStorage.clear()
    undefined  // command is uses for clear all the set items

3) localStorage.getItem('name') // Jo Data set kiya h uska output maango 
    "shubh"     
​






































    



