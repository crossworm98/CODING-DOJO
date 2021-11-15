function reverse(arr){
    var left = 0;
    var right = arr.length - 1;
    while(left < right){
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
    //swap arr[0] with arr[5]
    //swap arr[1] with arr[4]
    //swap arr[2] with arr[3]
}

var myArr = [2,4,6,8,20,50, 17];
reverse(myArr);
//should print [20,8,6,4,2]
console.log(myArr);