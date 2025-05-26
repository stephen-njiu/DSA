function sortedSquared(array){
    const newArray = new Array(array.length).fill(0)
    for (let i=0;i<array.length;i++){
        newArray[i] = Math.pow(array[i],2)
    }
    newArray.sort((a,b) => a-b)
    return newArray
}

a = [1, 3, 4, 5, 6]
b = [-1, -5, 6, 5, 4]
c = []

console.log(sortedSquared(a)) // [1, 9, 16, 25, 36]
console.log(sortedSquared(b)) // [1, 16, 25, 36, 25]
console.log(sortedSquared(c)) // [0, 0, 0, 0, 0]
console.log(sortedSquared([0, 0, 0, 0, 0])) // [0, 0, 0, 0, 0]