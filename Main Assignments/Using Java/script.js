console.log("hey there from the script")

function alertme(element){
    element.innerText = "i didnt say you could do that";
}
var header = document.getElementById("header");
var input = document.getElementById("input")

function changetext(){
    var text = input.value;
    header.innerText = text;
}
var count = 0
function alertme2(element){
    count++;
    element.innerText = count
}