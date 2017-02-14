function updatePage(){
    //This does nothing yet
}

function nosePress(){
    //What happens when you touch the screen
    var counter = document.getElementById("counter");
    var num = parseInt(counter.innerHTML);
    num +=1;
    counter.innerHTML = num;
}