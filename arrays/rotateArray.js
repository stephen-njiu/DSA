const rotateArray = function(array, k) {
    const leng = array.length
    k = k%leng
    const temp = array.slice(leng-k)
    for(let i = leng-k-1;i>=0;i--){
        array[i+k] = array[i]
    }
    for (let i = 0; i< k; i++){
        array[i] = temp[i]
    }
    return array
}

const a = [1, 2, 3, 1, 2, 88, -1]
k=7
console.log(rotateArray(a, k))