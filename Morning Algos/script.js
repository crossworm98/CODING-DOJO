// addToFront(arr, value)
// add a given value to the front of the array and return that array
// the arguments [1, 2, 3] and 4 result in the array [4, 1, 2, 3]
var i = [1,2,3]
function addToFront(arr, value) {
    temp = [value];
    for (i = 0; i < arr.length; i++){
        temp.push(arr[i]);
    }
return temp;
}
console.log(i)

// removeFront(arr)
// remove the value from the front of the array and return that array
// [7, 1, 4, 9] as the argument should result in an output of [1, 4, 9]

function removeFront(array) {
    
}