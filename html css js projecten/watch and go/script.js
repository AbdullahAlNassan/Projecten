// variables om de timeout & interval bij te houden
let countdown_event = null;
let timed_event = null;
 
let button = document.getElementById("control-button")
let subtitle = document.getElementById("control-title")
let counter = document.getElementById("countdown")
let rocket = document.getElementById("rocket")
let seconds2;
let countdown_timer;
 
 
 
// zet de mission control title, button en clear de countdown (interval & nummer) en timeout
function set_mission_control(title, buttonTitle, buttonOnclick) {
   
}
 
// verwijder alle states van de raket en voegt de juiste toe
function set_rocket_state(state) {
 
}
 
/* stage 1:
    set mission control: Prepare to Launch, button 'Start count down naar stage 2
    set rocket state: 1
*/
function set_stage_1() {
    subtitle.innerText = 'Perpare to lunch'
    button.classList.replace("hide", "show");
    button.innerText = "Start Countdown";
    counter.innerText = " ";
    rocket.className = "state1";
 
    clearInterval(countdown_timer);
    button.removeEventListener('click', set_stage_1);
    button.addEventListener('click',set_stage_2)
 
}
 
/* stage 2:
    set mission control: Counting down, button Abort click naar stage 1
    set rocket state: 2
    start timed event: na 5 seconden rocket state: 3
    start coundown event: na 10 seconden naar stage 3
*/
function set_stage_2() {
    seconds2 = 10;
    subtitle.innerText = 'Counting Down';
    button.innerText = "Abort";
    rocket.className = 'state2';
 
    countdown_timer = setInterval(start_countdown_event, 1000);
 
    button.removeEventListener('click', set_stage_2);
    button.addEventListener('click', set_stage_1);

    set_stage_3();
}
 
/* stage 3:
    set mission control: Lift off!
    set rocket state: 4
    start timed event: na 3 seconden naar stage 4
*/
function set_stage_3() {
    subtitle.innerText = 'Lift off';
    button.classList.replace('show','hide');
    counter.innerText = " ";
    rocket.className = "state4";

    setTimeout(set_stage_4,3000);
 
}
 
/* stage 4:
    set mission control: Add more power, button Boost rocket click naar stage 5
    set rocket state: 5
    start countdown event: na 2 seconden naar stage 6
*/
function set_stage_4(){
 
}
 
/* stage 4:
    set mission control: Rocket away
    set rocket state: 6
    start timed event: na 2 seconden rocket state 8 en een countdown van 3 seconden met Restarting in... die naar stage 1 gaat
*/
function set_stage_5() {
 
}
 
/* stage 6:
    set mission control: Rocket exploded
    set rocket state: 7
    start timed event: na 3 seconden zelfde titel, try again button naar stage 1
*/
function set_stage_6() {
 
}
 
// voer een functie (event) uit na x seconden, zonder count down
function start_timed_event(seconds, event) {
 
}
 
// voer een functie (event) uit na x seconden, met count down
function start_countdown_event(seconds, event){
    // alert('hello')
 
}
 
// set sage 1 on page load
set_stage_1();