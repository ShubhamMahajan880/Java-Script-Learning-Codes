/*💁‍♂️section - 11) Time Based Events :- 
- The window objects allows execution of code at specified time intervals. These time intervals are called timing events.
- The two key method to use with JavaScipt are :

1) setTimeout(function,millisecond) // Executes a function, after waiting a specified number of milliseconds

2) setInterval(function,milliseconds) // same as setTimeout(), but repeats the execution of the function continuosly

3) clearTimeout()

4) clearInterval()

😶‍🌫️Example of setTimeOut() :-

    <div class="main-div" >
        <div>
            <h1>Would you like to know my name ?</h1>
            <p id="showMyName" > </p>
            <br>
            <button  id="button">Click to Show</button>
        </div>
    </div>
    <script>
        const myname = document.querySelector('#showMyName');
        const button = document.querySelector('#button');

        const showMyName = () => {
            myname.innerHTML = "Loading.......⏲️"
            setTimeout(() => {
                myname.innerHTML = "Shubham_Mahajan"
            },500)
        }
        button.addEventListener('click',showMyName);
   </script>

😶‍🌫️Example of clearTimeOut() :-   
<!-- For Stopping Name reprsentation we can use ClearTimeOut Function -->

<div class="main-div" >
<div>
    <p>Click on Try Now. Wai for 3 Seconds The Page will alert "Shubh" </p>
    <p>Click "Stop" to prevent the first Function to execute </p>

    <button onclick="myVar = setTimeout(myfunction,2000)"> Try Now </button>
    <button onclick="clearTimeout(myVar)" >Stop It.</button>
</div>
</div>
<script>
    function myfunction() {
        alert("Shubham Mahajan is Here");
    }
</script>

😶‍🌫️Example of SetInterval(Counting Timer) :-   


<div class="main-div" >
    <div>
        <p>Book your seat when it will reach to 100</p>
        <br>
        <button id="btn" >Click To Book Your Seat </button>        
    </div>
</div>
<script>
    const stopNum = document.querySelector('p');
    const btn = document.querySelector('#btn');
    let num = 0;
    const showMyNum = () => {
        stopNum.innerHTML = "Loading......🙂"
        setInterval(() => {
            stopNum.innerHTML = `${num}`;
            num++;
        },1000 )
    }
    btn.addEventListener('click',showMyNum)
</script>

😶‍🌫️Example of StopInterval(Counting Timer) :-   


<div class="main-div" >
    <div>
        <p>Book your seat when it will reach to 100</p>
        <br>
        <button id="btn" >Click To Book Your Seat </button>        
        <button id="btn2" >Stop Here</button>
    </div>
</div>
<script>
    const stopNum = document.querySelector('p');
    const btn = document.querySelector('#btn');
    const btn2 = document.querySelector('#btn2');
    let timeRef;
    let num = 0;

    const showMyName = () => {
        stopNum.innerHTML = "Loading......🙂"
        timeRef =  setInterval(() => {
            stopNum.innerHTML = `${num}`;
            num++;
        },1000 )
    }
    btn.addEventListener('click',showMyName)
    stopInterval.addEventListener('click',() => {
        clearInterval(timeRef);
    })
</script>




*/
