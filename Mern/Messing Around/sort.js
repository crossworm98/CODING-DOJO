function bubbleSort(arr){
    for(var i = 0; i < arr.length; i++){
        for(var j = 0; j < (arr.length - i - 1); j++){
            if(arr[j] > arr[j + 1]){
                var temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    console.log(arr);
}

function selectionSort(arr) { 
    let n = arr.length;
        
    for(let i = 0; i < n; i++) {
        // Finding the smallest number in the subarray
        let min = i;
        for(let j = i+1; j < n; j++){
            if(arr[j] < arr[min]) {
                min=j; 
            }
        }
        if (min != i) {
             // Swapping the elements
            let tmp = arr[i]; 
            arr[i] = arr[min];
            arr[min] = tmp;      
        }
    }
    return arr;
}

const combine = (leftArr, rightArr) => {
    let ar3 = []

    let l1 = leftArr.length - 1

    let l2 = rightArr.length - 1

    let i = j = k = 0

    while (i <= l1 && j <= l2) {
        if (leftArr[i] >= rightArr[j]) {
            ar3.push(rightArr[j++])

        } else {
            ar3.push(leftArr[i++])

        }
    }

    while (i <= l1) {
        ar3.push(leftArr[i]);
        i++;
    }

    while (j <= l2) {
        ar3.push(rightArr[j++]);
    }

    return ar3;
}

let arr = [5,4,2,6,8,14,1,3];
console.log(selectionSort(arr))
console.log(arr);
console.log(bubbleSort(arr));