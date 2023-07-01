/*
ApI can be used by two ways
1) XMLHttpRequest();
2) FETCH;
*/

/* 1) XMLHttpRequest();

<div id="container" >

</div>
<script>
    const container = document.querySelector('#container')
    const request = new XMLHttpRequest();
    request.open('GET',"https://restcountries.com/v3.1/name/America");
    request.send();

    // To get the response 
    request.addEventListener('load',function(){
        // console.log(this.responseText);
        const [data] = JSON.parse(this.responseText);
        console.log(data);

    })

</script>

2) Using fetch() method :-
let p = fetch("https://goweather.herokuapp.com/weather/Mumbai")
p.then((value1) => {
    return value1.json()
} ).then((value2) => {
    console.log(value2)
} )

*/
/* O/p :- 
node /tmp/u61b3GnMkW.js
{
  temperature: '+29 °C',
  wind: '22 km/h',
  description: 'Haze, rain shower',
  forecast: [
    { day: '1', temperature: '33 °C', wind: '34 km/h' },
    { day: '2', temperature: '+28 °C', wind: '55 km/h' },
    { day: '3', temperature: ' °C', wind: '+28 km/h' }
  ]
}

*/