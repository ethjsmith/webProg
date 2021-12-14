var count = 0;
function yes(){
    count++;
    if(count > 10){
        document.getElementById("agreeText").innerHTML = "Stop doing that.";
    }else{
        document.getElementById("agreeText").innerHTML = "That's because we are correct.";
    }
}

function no(){
    count++;
    if(count > 10){
        document.getElementById("agreeText").innerHTML = "Stop doing that.";
    }else{
        document.getElementById("agreeText").innerHTML = "Too bad.";
    }
}

function setButtons(){
    document.getElementById("yesButton").addEventListener("click", yes);
    document.getElementById("noButton").addEventListener("click", no);
}

setButtons();