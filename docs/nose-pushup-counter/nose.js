function pow(a, b){
	var total = 1;
    
    while(b){
    	total *= a;
        b--;
    }
    
    return total;
}

function factorial(n){
    if(n <= 1)
        return n;
    return n * factorial(n - 1);
}

function deg_to_rad(x){
    return x * 3.1415926 / 180;
}

function fadeToBlack(){
    //This does nothing yet
}

function vsin(n){
    return function(x){
        var total = x,
            temp1,
            temp2,
            i;

        for(i = 0; i <= n; i++){
            temp1 = 3 + (i * 4);
            temp2 = temp1 + 2
            total -= pow(x, temp1) / factorial(temp1);
            total += pow(x, temp2) / factorial(temp2);
        }
        
        return total;
    }
}

function drawSine(ctx, sinf, y, color){
    ctx.fillStyle = color;
    for(var i = 0; i < 360; i+=0.05){
        ctx.fillRect(i * 10,y-sinf(i) * 10, 2,2);
    }
}

function main(){
    var canvas = document.getElementById("canvas");
    canvas.width = 400;
    canvas.height = 400;
    var ctx = canvas.getContext("2d");
    var i;
    ctx.font = "60px Arial";
    ctx.fillText("Hello World",200,200);
    fadeToBlack();
}
