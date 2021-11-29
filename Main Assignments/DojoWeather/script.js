function locations() {
    alert("What did you think was going to happen? Its only week 2");
}

function cookiebtn(element) {
    element.remove();
}

function convertcf(temp) {
    return Math.round(9 / 5 * temp + 32)
}

function convertfc(temp) {
    return Math.round(5 / 9 * (temp - 32))
}

function convert(element) {
    for (var i = 1; i < 9; i++) {
        var tempspan = document.querySelector("#temp" + i)
        var tempvalue = parseInt(tempspan.innerText)
        if (element.value == "C") {
            tempspan.innerText = convertfc(tempvalue)
        }
        else {
            tempspan.innerText = convertcf(tempvalue)
        }
    }
}

// function convert(element){
//     console.log(element.value);
//     var highs = document.getElementsByClassName("high")
//     var lows = document.getElementsByClassName("low")
//     console.log(highs)
//     console.log(lows)
//     if (element.value == "F"){
//         for(var i = 0; i < highs.length; i++){
//             console.log(highs[i].innerText)
//             highs[i].innerText = Math.floor((highs[i].innerText * 9/5) + 32)
//         }
//     }
//     else if (element.value == "C"){
//         for(var i = 0; i < highs.length; i++){
//             highs[i].innerText = Math.floor((highs[i].innerText -32) * 9/5)
//         }
//     }
// }

