/* Section - 11 )💁‍♂️ Events in JavaScript

Html Events are "things" that happen to HTML element
When javascript is used in html pages, Javascript can react on these events

👉HTML Events :- 
An H T M L event can be someting the browser does, or something a user does.
here are some examples for html events
An html web page has finished loading
An extreme input was changed
An HTML button was clicked on
Html allows event handler attributeswhich javascript codes to be added to html
*/

/*👉🏻There are 4 Ways to writting Events in JavaScrpt :- 
1 : using inline events alerts()   
2 : By calling a function 
3 : using Inline Events (HTML onclick= "" property and element.oneclick)
4 : using Event Listeners

Method 1) alert('Do you really want to proceed')

Method 2) Using Calling a Function :-
<div class="Button" >
        <a href="#" class="Button" onclick="callingfunction()" >By clicking that icon </a>

    </div>
    <script>
        const callingfunction = () => {
            alert('Hey,What are you going to do');
        }
    </script>

*/

/*👉Section 2) Event Objects :- What is event Objects ?
Event object is the parent object of the event Object. Ex :- Mouse Event,Focus Event Keyboard Event

Ex :- 

    <div class="Button" >
        <a href="#" class="Button" id="Fourthway" > 4th Method Here </a>
    </div>
    <script>
        const Fourthway = documen.getElementById('Fourthway');

        const checkEvent = () => {
            alert('We are learning JavaScript from Basic to Advance Level');
            console.log(event);
            console.log(event.target);
            console.log(event.type);
        }
        Fourthway.addEventListener('click',checkEvent);
        // To get all the information about Event, We can use the event Object
    </script>
*/


/*👉🏻Section - 3) Mouse Event in JavaScropt
The Mouse Event Object
Events that occur when the mouse interacts with the HTML document belongs to the MouseEvent Objects

Example :- 
Comands 

    1) Mousedown :- Jb tk mouse se click kiya hua hoga(down)  tb tk Event Hota (color change) rhega
    2) Mouseup :- Jese hi ckicked mouse chhoda jaayga tb Event Run (color change) ho jayga


    <p id="myP" onmousedown="mousedown()" onmouseup="mouseup()" > Shubham Mahajan is an influencer and a well known Public Speaker. He did his schooling from his birth place names as Khargone Mdhya Pradesh. After completion of his schooling he moved toward Vadodar for Graduation and pursued B TECH in Computer Science along with Specialization in Artificial Intelligence. He is such a great Motivational Speaker and very Helpful for Studnets and conducting many NGO'S and donation Trust's </p>
    <script>
        function mousedown() {
            document.getElementById("myP").style.color = "red";
        }

        function mouseup(){
            document.getElementById("myP").style.color = "green"
        }

    </script>

    3) Mouseenter :- Jese kisi objec pr mouse jaayega(NOT clicked ONLY Moved) uska color Automaticaly change ho jaayega and jb tk mouse us prr rhega color chnaged hi rhega
    4) Mouseleave :- Jese hi us object pr se mouse hta diya jaayega color(Jo ki set Kiya h) change ho jayega 

    Code
    Css code :- .main-div{
width: 100vw;
height: 100vh;
display: grid;
place-items: center;
}

#box{
    width: 100px;
    height: 100px;
    background: gold;

}  
    HTML Code :- 
    JavaScript COde :-

    <div class="main-div" >
        <div id="box" ></div>
    </div>
    <script>
        const mouseenter = document.getElementById('box');
        mouseenter.addEventListener('mouseenter',() => {
            mouseenter.style.backgroundColor = 'RED';
            console.log('Mouse Entered Buddy');
        });
        const mouseleave = document.getElementById('box');
        mouseleave.addEventListener('mouseleave',() => {
            mouseleave.style.backgroundColor = 'Blue';
            console.log('Mouse Went Buddy');
        });
    </script>
*/
/*👉🏻Section - 4) KeyBoardEvent in JavaScript :- 
Events that occur when user presses a key on the keyboard,
belongs to the keyboard object.

<div class="main-div" >
        <div>
        <br>
            <p>A function is triggered when the user is pressing a key in the input field.</p>
            <br>
            <input type="text" onkeypress="keypress()" onkeydown="keydown()" onkeyup="keyup()" >
        </br>
        <p id="keys"></p>
        </div>
    </div>
<!-- 
    <script>
         const keypress= () => {
            document.getElementById("keys").innerHTML = 'you presses ${event.key} and its code is ${event.code}';
        }
    </script> -->

    <script>
            const keydown = () => {
                document.getElementById('keys').innerHTML = 'Key is down';
            }
            const keyup = () => {
                document.getElementById('keys').innerHTML = 'Key is up';
            }

        
    </script>




*/
