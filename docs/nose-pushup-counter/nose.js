var timer = setTimeout(updatePage, 10);
var bgColor = 255;

function updatePage(){
    //This does nothing yet
    var oldColor = document.body.style.backgroundColor;
    bgColor -= 1;
    document.body.style.backgroundColor = `rgb(${bgColor},${bgColor},${bgColor})`;
    var timer = setTimeout(updatePage, 5);
}

function nosePress(){
    //What happens when you touch the screen
    clearTimeout(timer);
    var counter = document.getElementById("counter");
    var num = parseInt(counter.innerHTML);
    num +=1;
    counter.innerHTML = num;
    document.body.style.backgroundColor = "#ffffff";
    bgColor = 255;
}