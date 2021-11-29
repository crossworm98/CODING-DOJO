
function reverseString(str) {
    var newString = "";
    var oldString = "hello";
    for (var i = oldString.length - 1; i >= 0; i--)
    newString = newString += oldString[i];
    }
return newString;






function acronym(str) {
    let acro = str[0];
    for (let i = 1; i < str.length; i++) {
        if (str[i - 1] ==  " " && str[1] > "A") {
            acro += str[i];
        }
    }
    return acro;
}

console.log(acronym("free all rodents that like evil kittens"));
console.log(acronym("never obey older babies sarcastically"));