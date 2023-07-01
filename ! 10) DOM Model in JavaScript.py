/* Dom vs BOM :- 
💁‍♂️The DOM is Document Object Model, Which deals with the document, the HTML element themselves, e.g. document and all traversal you would do in it.
For Example :- 
It can change the background color to "RED"
DOM property Example:- 
document.body.style.background = "red";


💁‍♂️ The BOM is the Browser Object Model, which deals with browser components aside from the document,like history,location,navigator and screen OR
In simple meaning all the window operations which comes under BOM are performed using BOM

BOM property Example :- 
innerHeight
innerWidth

Commands to Run :- 
1) document  :-  WILL Provide document information stored in local disk 
o/p - 
HTMLDocument file:///D:/Study%20Material/Never%20Stop%20Learning%20Something%20New/FullStack%20Web%20Development/Proper%20Learning/Course%20Content/++++JavaScript/NewOne/JavaScript%20Practical.html

2) document.head  :- Will provide all Head Commands inside the HTML code
o/p - 
<head>​
accessKey: ""​
accessKeyLabel: ""​
assignedSlot: null​
attributes: NamedNodeMap []​
autocapitalize: ""​
autofocus: false​
baseURI: "file:///D:/Study%20Material/Never%20Stop%20Learning%20Something%20New/FullStack%20Web%20Development/Proper%20Learning/Course%20Content/++++JavaScript/NewOne/JavaScript%20Practical.html"​
childElementCount: ​
childNodes: NodeList(9) [ #text, meta, #text, … ]​
children: HTMLCollection { 0: meta, 1: meta, length: 4, … }​
classList: DOMTokenList []​
className: ""​
clientHeight: 0​
clientLeft: 0​
clientTop: 0​
clientWidth: 0​
contentEditable: "inherit"
dataset: DOMStringMap(0)​
dir: ""​
draggable: false​
enterKeyHint: ""​
firstChild: #text "\n    "​
firstElementChild: <meta charset="UTF-8">​
hidden: false​
id: ""​
inert: false​
innerHTML: '\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Understanding of set &amp; Get Functions in Js</title>\n    <link rel="stylesheet" href="style.css">\n'​
innerText: "\n    \n    \n    Understanding of set & Get Functions in Js\n    \n"​
inputMode: ""​
isConnected: true​
isContentEditable: false​
lang: ""​
lastChild: #text "\n"​
lastElementChild: <link rel="stylesheet" href="style.css">​
localName: "head"​
namespaceURI: "http://www.w3.org/1999/xhtml"​
nextElementSibling: <body>​
nextSibling: #text "\n"​
nodeName: "HEAD"​
nodeType: 1​
nodeValue: null​
nonce: ""​
offsetHeight: 0​
offsetLeft: 0​
offsetParent: null​
offsetTop: 0​
offsetWidth: 0​
onabort: null​
onanimationcancel: null​
onanimationend: null​
onanimationiteration: null​
onanimationstart: null​
onauxclick: null​
onbeforeinput: null​
onblur: null​
oncanplay: null​
oncanplaythrough: null​
onchange: null​
onclick: null​
onclose: null​
oncontextmenu: null​
oncopy: null​
oncuechange: null​
oncut: null​
ondblclick: null​
ondrag: null​
ondragend: null​
ondragenter: null​
ondragexit: null​
ondragleave: null​
ondragover: null

3) document.body :- Will Provide all body commands

4) document.body.childNodes :- 
NodeList(3) [ #text, div.Understading.of.different.Child.and.class, #text
 ]​
0: #text "\n    "​
1: <div class="Understading of different Child and class">​
2: #text "\n    \n\n"​
length: 3

👉Practice TIme :-Que . 1) How to check wheather an elements has child nodes or not ?
Ans :- We can use command as "document.body.childNodes"  OR "haschildNodes()"

Que.2) How to find the child in DOM tree
firstchild vs firstElementChild
lastchild vs lastElementChild

5) document.body.firstElementChild :-  Uses for get the information of firstchild (That is main class created in first time )
5.1) document.body.firstElementChild.firstElementChild :- Then First class after the main class

6) document.body.parentNode  :- Is command uses for get the information aboout parent Node 

7) document.body.parentElement  :- Is command uses for information of all elements 

8) document.body.nextSibling :- Command uses for obtain the information about nextsibling, but is shows "null", in this case use bottom command

9) document.body.previousSibling :- By using this command now it will show earlier sibling
*/

/*
💁‍♂️How to Search Elements and References :- 
- console.log(document.getElementsByClassName('NAMEOFCLASS'); :- Is a command uses for elements information using class name

- console.log(document.getElementsByTagName('NAMEOFTAG')); :- Is a command uses for elements information using tag name like "paragraph","Heading"

- console.log(document.getElementById('NAMEOFID')) :- Is a command uses for getting Elements information using ID NAME

- console.log(document.getElementsByName('NAMEOFname')); :- is a command uses for getting elements information using "name" uses in form or select and other sections

- document.querySelector('#IDOFHEADING').innerHTML = "STATEMENTWHICHWEWANTTOSHOW"; :- is a command uses for chnge the heading through id tag(#) 


⏲️ Intervies Question :- Diffrence between getElementById and QuerrySelector ?
Ans :-
 getElementById() syntax :- 
element = document.getElementById('NAMEOFID');

It returns a reference to a element by its Id. If the element is not available with that specified id then it will return "null"

querySelector() syntax :- 
element = document.querySelector('#NAMEOFSELECTOR');
Returns tjhe first element within the document that matches the specified group of selectors, or NULL if no matches are found


*/
